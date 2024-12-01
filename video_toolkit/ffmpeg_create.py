from pydub import AudioSegment
from typing import Union,List,Tuple, Literal, Callable, Dict
from pathlib import Path

def export_audio(audio_segment:AudioSegment,
                 start_end_time_dict: Dict[int,Tuple[int,int]],
                 output_names:Dict[int,str],
                 output_folder:str = "",
                 progress_bar:bool = True,
                 ) -> None:
    
    # medium tested
    """
    Key feature: 
        1) Remove the invalid path in output_names automatically
    the timestamp should be in miliseconds units(for now)
    export multiple audio_segments
    make sure that index in output_names is also in start_end_time_dict
    
    example of start_end_time_dict
        start_end_time_dict = {
        6:  [14_633 , 15_933],
        7:  [24_455 , 25_534],
        8:  [25_700 , 27_550],
        9:  [27_899 , 30_000],
        10: [31_075 , 32_863],
        11: [33_439 , 36_188],
        12: [37_280 , 42_100],
        14: [42_865 , 47_224],
        
        }

    TOADD: replace => it would check if file already exists, if so depending on it's True or False, it would replace the file
    """
    import py_string_tool as pst
    clean_output_names = {}
    for inx, output_name in output_names.items():
        clean_output_names[inx] = pst.clean_filename(output_name)
    
    from tqdm import tqdm
    if progress_bar:
        loop_obj = tqdm(start_end_time_dict.items())
    else:
        loop_obj = start_end_time_dict.items()
    
    for inx, time_stamp in loop_obj:
        start_time, end_time = time_stamp
        try:
            output_name = clean_output_names[inx]
        except KeyError:
            raise KeyError(f"there's no index {inx} in your output_names(Dict). Please check your index again.")
        output_path = output_folder + "/" + output_name
        curr_audio = audio_segment[start_time:end_time]
        
        try:
            curr_audio.export(output_path)
        except PermissionError:
            raise KeyError(f"Please close the file {output_path} first.")


def merge_audio_to_video(
    input_video_path: Union[str, Path],
    input_audio_path: Union[List[Union[str, Path]], Union[str, Path]],
    audio_language_code_3alpha: Union[List[str], str],
    audio_title: Union[List[str], str],
    output_folder: Union[str, Path],
    output_name: str
) -> None:
    """
    Merges a video file with additional audio tracks, assigning metadata such as language and title to each audio track.

    Parameters
    ----------
    input_video_path : str or Path
        The path to the input video file.
    input_audio_path : list of str/Path or str/Path
        The path(s) to the input audio file(s). Can be a single path or a list of paths.
    audio_language_code_3alpha : list of str or str
        The language code(s) for the audio track(s) (e.g., 'fre' for French). Can be a single code or a list.
    audio_title : list of str or str
        The title(s) for the audio track(s) (e.g., 'French'). Can be a single title or a list.
    output_folder : str or Path
        The folder where the output video file will be saved.
    output_name : str
        The name of the output video file.

    Returns
    -------
    None
    """
    
    # medium tested for input_audio_path as list and single_string
    from pathlib import Path
    import subprocess
    
    # Ensure inputs are lists for consistent processing
    if isinstance(input_audio_path, (str, Path)):
        input_audio_path = [input_audio_path]
    if isinstance(audio_language_code_3alpha, str):
        audio_language_code_3alpha = [audio_language_code_3alpha]
    if isinstance(audio_title, str):
        audio_title = [audio_title]

    # Check for consistent lengths of inputs
    if not (len(input_audio_path) == len(audio_language_code_3alpha) == len(audio_title)):
        raise ValueError("The lengths of input_audio_path, audio_language_code_3alpha, and audio_title must match.")

    video_path = Path(input_video_path)
    output_path = Path(output_folder) / output_name

    # Construct the ffmpeg command
    command = ['ffmpeg', '-i', str(video_path)]

    # Add all audio inputs
    for audio in input_audio_path:
        command.extend(['-i', str(audio)])

    # Add mapping for video and audio
    command.append('-map')
    command.append('0')  # Map all streams from video
    for idx in range(len(input_audio_path)):
        command.append('-map')
        command.append(f'{idx + 1}:a')  # Map each audio file

    # Add metadata for each audio track
    for idx, (lang, title) in enumerate(zip(audio_language_code_3alpha, audio_title), start=2):
        command.extend(['-metadata:s:a:' + str(idx), f'language={lang}'])
        command.extend(['-metadata:s:a:' + str(idx), f'title={title}'])

    # Add codec settings and output file
    command.extend(['-c', 'copy', str(output_path)])

    # cmd_line is just for debugging
    cmd_line = ' '.join(command)

    # Execute the command
    result = subprocess.run(command, text=True, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error encountered:")
        print(result.stderr)
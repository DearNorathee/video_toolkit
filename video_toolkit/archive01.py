from typing import Union,List,Tuple, Literal, Callable, Dict
from pathlib import Path
from beartype import beartype


# @beartype
def extract_audio(
        video_folder:     Union[Path,str],
        output_folder:    Union[Path,str],
        video_extension:  Union[list,str] = VIDEO_ALL_EXTENSIONS,
        output_extension: Union[list,str] = ".mp3",
        overwrite_file:   bool = True,
        n_limit:          int = 150,
        output_prefix:    str = "",
        output_suffix:    str = "",
        alarm_done:       bool = True,

        one_output_per_lang: bool = True,
        languages: Union[List[str],None,str] = None,
):
    # extract_audio3 is highly tested now
    # this is from extract_audio3(it's already tested through time seems pretty stable)
    """
    the diff between 
    extract_audio1 - use manually code to loop through folder
    extract_audio2 - powered by _extract_media_setup while 
    extract_audio3 - use extract_audio_1file as a base(which is more general than extract_audio1 & extract_audio2), but need more testing to see if it works
    
    # after testing I would then rename extract_audio3 to just extract_audio
    
    """


    _extract_media_setup(
        input_folder = video_folder,
        output_folder = output_folder,
        input_extension = video_extension,
        output_extension = output_extension,
        extract_1_file_func = extract_audio_1file,
        overwrite_file = overwrite_file,
        n_limit = n_limit,
        output_prefix = output_prefix,
        output_suffix = output_suffix,
        alarm_done = alarm_done,

        one_output_per_lang = one_output_per_lang,
        languages = languages

    )


@beartype
def extract_subtitle(
        video_folder:     Union[Path,str],
        output_folder:    Union[Path,str],
        video_extension:  Union[list,str] = [".mp4",".mkv"],
        output_extension: Union[list,str,None] = None,
        overwrite_file:   bool = True,
        n_limit:          int = 150,
        output_prefix:    str = "",
        output_suffix:    str = "",
        languages: List[str] | None | str = None,
        alarm_done:       bool = True,
        verbose:int = 0,
):
    # write now language input has to be 3-str letter(BigBang FR)
    
    # ToAdd01: suffix with language code instead of index
    
    input_param = {
        'video_path': 6
    }
    
    _extract_media_setup(
        input_folder = video_folder,
        output_folder = output_folder,
        input_extension = video_extension,
        output_extension = output_extension,
        extract_1_file_func = extract_sub_1_video,
        overwrite_file = overwrite_file,
        n_limit = n_limit,
        output_prefix = output_prefix,
        output_suffix = output_suffix,
        languages=languages,
        alarm_done = alarm_done,
        verbose = verbose,
    )


@beartype
def change_audio_speed_1file(
    audio_path:str
    ,speedx:float
    ,output_name:str
    ,output_folder:str = ""
    ,errors:Literal["raise","warn"] = "raise"
    ,print_errors:bool = False
    ) -> None :
 

    
    import subprocess
    import numpy as np
    import os
    from send2trash import send2trash
    from pathlib import Path
    
    # medium tested
    # TOADD01: to add if the output file already exist just replace it?
    if not os.path.exists(audio_path):
        raise FileNotFoundError("Please check the path. It doesn't exist.")
        
    if (speedx < 0.5) or (speedx > 2):
        raise ValueError(f"Value of speedx should be between 0.5 and 2. Otherwise the function doesn't work.")
        
    
    filepath = Path(audio_path)
    folder_path = filepath.parent
    filename = filepath.stem
    
    if output_folder == "":
        output_folder_in = folder_path
    else:
        output_folder_in = Path(output_folder)
    output_path = output_folder_in.with_name(f"{output_name}")

    
    command = [
        "ffmpeg",
        "-i", str(filepath),
        "-filter:a", f"-atempo={speedx}", 
        str(output_path)
    ]

    command_line = " ".join(command)
    command_np = np.array(command)
    result = subprocess.run(command, text=True, stderr=subprocess.PIPE)
    
    
    if errors in ["warn"]:
        if result.returncode != 0:
            print("Error encountered:")
            print(result.stderr)
    elif errors in ["raise"]:
        if result.returncode != 0:
            if print_errors:
                raise Exception(result.stderr)
            else:
                raise Exception()

def extract_audio2(
        video_folder:     Union[Path,str],
        output_folder:    Union[Path,str],
        video_extension:  Union[list,str] = [".mp4",".mkv"],
        output_extension: Union[list,str] = ".mp3",
        overwrite_file:   bool = True,
        n_limit:          int = 150,
        output_prefix:    str = "",
        output_suffix:    str = "",
        alarm_done:       bool = True,
):
    """
    the diff between 
    extract_audio1 - use manually code to loop through folder
    extract_audio2 - powered by _extract_media_setup while 
    extract_audio3 - use extract_audio_1file as a base(which is more general than extract_audio1 & extract_audio2), but need more testing to see if it works
    
    # after testing I would then rename extract_audio3 to just extract_audio
    
    """
    input_param = {
        'video_path': 6
    }

    _extract_media_setup(
        input_folder = video_folder,
        output_folder = output_folder,
        input_extension = video_extension,
        output_extension = output_extension,
        extract_1_file_func = extract_1_audio,
        overwrite_file = overwrite_file,
        n_limit = n_limit,
        output_prefix = output_prefix,
        output_suffix = output_suffix,
        alarm_done = alarm_done,
    )


def extract_audio1(video_folder:     Union[Path,str],
                  output_folder:    Union[Path,str],
                  video_extension:  Union[list,str] = [".mp4",".mkv"],
                  output_extension: Union[list,str] = ".mp3",
                  output_prefix:    str = "",
                  output_suffix:    str = "",
                  alarm_done:       bool = True,
                  overwrite_file:   bool = True,
                  n_limit:          int = 150
                  ):
    # TODO 
    # add feature: support multiple languages
    # support multiple output eg [.wav,.mp3,.eac3]
    
    """

    the diff between 
    extract_audio1 - use manually code to loop through folder
    extract_audio2 - powered by _extract_media_setup while 
    extract_audio3 - use extract_audio_1file as a base(which is more general than extract_audio1 & extract_audio2), but need more testing to see if it works

    Extracts audio from video files in the specified `video_folder` and saves them in the `output_folder` in the specified audio format.
    
    Parameters
    ----------
    video_folder : Union[Path, str]
        The path to the folder containing video files.
        
    output_folder : Union[Path, str]
        The path where extracted audio files will be saved.
        
    video_extension : Union[list, str], optional
        List of video file extensions to consider for extraction. Defaults to [".mp4", ".mkv"].
        
    output_extension : Union[list, str], optional
        The audio file extension for the output files. Defaults to ".mp3".
        
    output_prefix : str, optional
        A prefix to be added to the output audio file names. Defaults to an empty string.
        
    output_suffix : str, optional
        A suffix to be added to the output audio file names. Defaults to an empty string.
        
    alarm_done : bool, optional
        Whether to play an alarm sound when the extraction is completed. Defaults to True.
        
    overwrite_file : bool, optional
        Whether to overwrite existing audio files with the same name in the `output_folder`. Defaults to True.
        
    n_limit : int, optional
        The maximum number of video files to process. Defaults to 150.
        
    Returns
    -------
    """
    
    import sys
    from pathlib import Path
    from playsound import playsound
    
    from time import time
    ts01 = time()
    
    
    import os_toolkit as ost
    import python_wizard as pw
    
    codec_dict = {'.mp3': "libmp3lame",
                  'mp3' : "libmp3lame",
                  '.wav': "pcm_s24le",
                  'wav' : "pcm_s24le"
                  }
    
    output_extension = [output_extension]
    output_extension_in = []
    
    # add . to extension in case it doesn't have .
    for extension in output_extension:
        if not "." in extension:
            output_extension_in.append("."+extension)
        else:
            output_extension_in.append(extension)
    
    video_name_list_ext = ost.get_filename(video_folder,video_extension)
    video_path_list = ost.get_full_filename(video_folder,video_extension)
    
    n_file = min(len(video_name_list_ext),n_limit)
    video_name_list_ext = video_name_list_ext[:n_file]
    video_path_list = video_path_list[:n_file]
    
    video_name_list = [filename.split('.')[0] for filename in video_name_list_ext]
    
    for i, video_name in enumerate(video_name_list):
        
            
        output_name = output_prefix + video_name_list[i] + output_suffix
        # original_stdout = sys.stdout
        # sys.stdout = open('nul', 'w') 
        
        for i, extension in enumerate(output_extension_in):
            extract_1_audio(
                video_path = video_path_list[i],
                output_folder = output_folder,
                output_name = output_name,
                file_extension = extension,
                alarm_done=False,
                overwrite_file=overwrite_file)
        
        # sys.stdout = original_stdout
        
    if alarm_done:
        playsound(alarm_done_path)
    ts02 = time()
    duration = ts02-ts01
    pw.print_time(duration)
    
    return video_name_list

del Union,List,Tuple, Literal, Callable, Dict, Path
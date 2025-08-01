from pydub import AudioSegment
from typing import Union,List,Tuple, Literal, Callable, Dict, Any, Optional
from pathlib import Path
from video_toolkit.ffmpeg_extract import *
import pandas as pd
from beartype import beartype
import pkg_resources
from video_toolkit.utils_vt import VIDEO_ALL_EXTENSIONS, AUDIO_ALL_EXTENSIONS, SUBTITLE_ALL_EXTENSIONS, CODEC_DICT, MEDIA_ALL_EXTENSIONS

alarm_done_path = pkg_resources.resource_filename(__name__, 'assets/Sound Effect positive-logo-opener.wav')
sound_error_path = pkg_resources.resource_filename(__name__, 'assets/Sound Effect Error.wav')


def cut_front_audio(
    filepaths: Union[str, Path,list[str|Path]]
    ,sec: Union[int, float]
    ,output_folder: Union[str, Path] = ""
    # handle_multi_input parameter
    
    ,progress_bar: bool = True
    ,verbose: int = 0
    ,alarm_done: bool = True
    ,alarm_error: bool = True
    ,input_extension: str|None = AUDIO_ALL_EXTENSIONS
) -> None:
    """
    Cuts out the first `sec` seconds from an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds to remove from the start.
    output_name : str or None, optional
        Filename for the output. If None, original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. If empty, saves alongside the input file.
    """
    
    # little tested
    # ffmpeg version is much faster than pydub
    import inspect_py as inp

    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
        ,"output_name":None
        ,"sec":sec
    }

    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(cut_front_1audio)
    result = func_temp(**path_input)

def add_front_audio(
    filepaths: Union[str, Path,list[str|Path]]
    ,sec: Union[int, float]
    ,output_folder: Union[str, Path] = ""
    # handle_multi_input parameters
    
    ,progress_bar: bool = True
    ,verbose: int = 0
    ,alarm_done: bool = True
    ,alarm_error: bool = True
    ,input_extension: str|None = AUDIO_ALL_EXTENSIONS
) -> None:
    """
    Cuts out the first `sec` seconds from an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds to remove from the start.
    output_name : str or None, optional
        Filename for the output. If None, original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. If empty, saves alongside the input file.
    """
    
    # not tested
    # ffmpeg version is much faster than pydub
    import inspect_py as inp

    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
        ,"output_name":None
        ,"sec":sec
    }

    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(add_front_1audio)
    result = func_temp(**path_input)

def cut_back_audio(
    filepaths: Union[str, Path,list[str|Path]]
    ,sec: Union[int, float]
    ,output_folder: Union[str, Path] = ""
    # handle_multi_input parameters
    
    ,progress_bar: bool = True
    ,verbose: int = 0
    ,alarm_done: bool = True
    ,alarm_error: bool = True
    ,input_extension: str|None = AUDIO_ALL_EXTENSIONS
) -> None:
    """
    Cuts out the first `sec` seconds from an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds to remove from the start.
    output_name : str or None, optional
        Filename for the output. If None, original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. If empty, saves alongside the input file.
    """
    
    # not tested
    # ffmpeg version is much faster than pydub
    import inspect_py as inp

    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
        ,"output_name":None
        ,"sec":sec
    }

    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(cut_back_1audio)
    result = func_temp(**path_input)

def add_back_audio(
    filepaths: Union[str, Path,list[str|Path]]
    ,sec: Union[int, float]
    ,output_folder: Union[str, Path] = ""
    # handle_multi_input parameters
    
    ,progress_bar: bool = True
    ,verbose: int = 0
    ,alarm_done: bool = True
    ,alarm_error: bool = True
    ,input_extension: str|None = AUDIO_ALL_EXTENSIONS
) -> None:
    """
    Cuts out the first `sec` seconds from an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds to remove from the start.
    output_name : str or None, optional
        Filename for the output. If None, original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. If empty, saves alongside the input file.
    """
    
    # not tested
    # ffmpeg version is much faster than pydub
    import inspect_py as inp

    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
        ,"output_name":None
        ,"sec":sec
    }

    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(add_back_1audio)
    result = func_temp(**path_input)


def cut_front_1audio(
    audio_path: Union[str, Path],
    sec: Union[int, float],
    output_name: Optional[str] = None,
    output_folder: Union[str, Path] = ""
) -> None:
    """
    Cuts out the first `sec` seconds from an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds to remove from the start.
    output_name : str or None, optional
        Filename for the output. If None, original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. If empty, saves alongside the input file.
    """
    
    # medium tested
    # ffmpeg version is much faster than pydub
    import subprocess
    from pathlib import Path
    import os


    if not os.path.exists(audio_path):
        raise FileNotFoundError("Please check the path. It doesn't exist.")
    
    inp = Path(audio_path)
    out_dir = Path(output_folder) if output_folder else inp.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    name = output_name or inp.name
    out_path = out_dir / name

    # Use ffmpeg to seek past the first `sec` seconds and copy streams
    command = [
        "ffmpeg",
        "-y",              # overwrite if exists
        "-ss", str(sec),   # seek to `sec`
        "-i", str(inp),    # input file
        "-c", "copy",      # copy codecs (no re-encode)
        str(out_path)      # output file
    ]
    subprocess.run(command, check=True)


def add_front_1audio(
    audio_path: Union[str, Path],
    sec: Union[int, float],
    output_name: Optional[str] = None,
    output_folder: Union[str, Path] = ""
) -> None:
    """
    Prepends `sec` seconds of silence to an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds of silence to add at the front.
    output_name : str or None, optional
        Filename for the output. If None, the original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. Defaults to the same folder as the input.
    """
    import subprocess
    from pathlib import Path
    import os


    if not os.path.exists(audio_path):
        raise FileNotFoundError("Please check the path. It doesn't exist.")

    # not tested
    inp = Path(audio_path)
    out_dir = Path(output_folder) if output_folder else inp.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    name = output_name or inp.name
    out_path = out_dir / name

    # milliseconds of silence
    ms = int(sec * 1000)
    # adelay accepts a single value to apply to all channels
    delay_arg = f"{ms}"

    cmd = [
        "ffmpeg",
        "-y",                # overwrite if exists
        "-i", str(inp),      # input file
        "-af", f"adelay={delay_arg}",  # prepend silence
        str(out_path)        # output file
    ]
    subprocess.run(cmd, check=True)


def cut_back_1audio(
    audio_path: Union[str, Path],
    sec: Union[int, float],
    output_name: Optional[str] = None,
    output_folder: Union[str, Path] = ""
) -> None:
    """
    Cuts out the last `sec` seconds from an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds to remove from the end.
    output_name : str or None, optional
        Filename for the output. If None, original filename is used.
    output_folder : str or Path, optional
        Directory to save the output. Defaults to the same folder as the input.

    Returns
    -------
    None
    """
    
    # not tested
    import subprocess
    import json
    from pathlib import Path
    import os


    if not os.path.exists(audio_path):
        raise FileNotFoundError("Please check the path. It doesn't exist.")

    inp = Path(audio_path)
    out_dir = Path(output_folder) if output_folder else inp.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    name = output_name or inp.name
    out_path = out_dir / name

    # Get duration via ffprobe
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", str(inp)],
        capture_output=True, text=True, check=True
    )
    duration = float(json.loads(probe.stdout)["format"]["duration"])
    # Calculate the new duration
    keep_duration = max(duration - sec, 0)

    # FFmpeg command to cut to the new duration
    cmd = [
        "ffmpeg",
        "-y",                 # overwrite
        "-i", str(inp),
        "-t", str(keep_duration),
        "-c", "copy",
        str(out_path)
    ]
    subprocess.run(cmd, check=True)


def add_back_1audio(
    audio_path: Union[str, Path],
    sec: Union[int, float],
    output_name: Optional[str] = None,
    output_folder: Union[str, Path] = ""
) -> None:
    """
    Appends `sec` seconds of silence to the end of an audio file using ffmpeg.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file.
    sec : int or float
        Number of seconds of silence to add at the end.
    output_name : str or None, optional
        Filename for the output. If None, uses the original filename.
    output_folder : str or Path, optional
        Directory to save the output file. Defaults to the same folder as the input.
    """
    import subprocess
    from pathlib import Path
    import os


    if not os.path.exists(audio_path):
        raise FileNotFoundError("Please check the path. It doesn't exist.")

    # not tested
    inp = Path(audio_path)
    out_dir = Path(output_folder) if output_folder else inp.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    name = output_name or inp.name
    out_path = out_dir / name

    # Use ffmpeg's apad filter to append silence
    cmd = [
        "ffmpeg",
        "-y",                # overwrite output if exists
        "-i", str(inp),      # input file
        "-af", f"apad=pad_dur={sec}",  # append silence for `sec` seconds
        "-c:a", "libmp3lame",  # re-encode to MP3
        str(out_path)         # output file
    ]
    subprocess.run(cmd, check=True)


@beartype
def change_title_from_filename(
    filepaths: Union[str, Path, list[str|Path]]
    ,output_folder: str|Path

    # input below would get import automatically
    ,replace: bool = True
    ,prefix: str = ""
    ,suffix: str = ""
    ,errors:Literal["warn","raise"] = "raise"
    ,print_errors:bool = False

    # handle_multi_input parameters
    ,progress_bar: bool = True
    ,verbose: int = 1
    ,alarm_done: bool = False
    ,alarm_error: bool = False
    ,input_extension: str|None = [".mp3",".mp4",".wav",".srt",".mkv",".avi"]
    ):
    
    """
    Update file title metadata in batch using filenames.

    This function processes one or multiple media files by updating their title metadata to match their filename.
    Internally, it leverages the `handle_multi_input` mechanism to support a flexible range of inputs,
    such as single file paths, lists of files, or entire directories. The actual processing is delegated to
    the function `vt.change_title_from_filename_1file`.

    Parameters
    ----------
    filepaths : str or Path
        A single file path, a folder path, or a list of file paths to be processed.
    output_folder : str or Path
        Directory where the output files with the updated title metadata will be saved.

    replace : bool, default True
        If True, the original file is replaced by the updated file. Otherwise, a new file is created.
    prefix : str, default ""
        Optional prefix to add to the filename when creating a new file (applicable when `replace` is False).
    suffix : str, default ""
        Optional suffix to add to the filename when creating a new file (applicable when `replace` is False).
    errors : {"warn", "raise"}, default "raise"
        Specifies whether to issue a warning or raise an exception if an error occurs during processing.
    print_errors : bool, default False
        If True, prints detailed error messages when processing fails.

    progress_bar : bool, default True
        Whether to display a progress bar during batch processing.
    verbose : int, default 1
        Verbosity level: 0 for minimal output, higher values for more detailed processing information.
    alarm_done : bool, default False
        If True, plays a notification sound after successful completion.
    alarm_error : bool, default False
        If True, plays a notification sound when an error occurs.
    input_extension : list of str or None, default [".mp3", ".mp4", ".wav", ".srt", ".mkv"]
        A list of file extensions to filter by when the input is a folder. If None or "all", all files are processed.

    Returns
    -------
    None
        The function performs in-place updates or creates new files with the updated title metadata in the
        specified output folder.

    Notes
    -----
    - This function uses the `handle_multi_input` decorator (via `inp.handle_multi_input`) to extend single-file
    processing to multiple files or folders.
    - The title metadata is set based on the original filename (without extension) of each file.
    - Requires that the underlying function `vt.change_title_from_filename_1file` and the `ffmpeg` tool are properly installed
    and accessible.

    Examples
    --------
    Update title metadata for a single file:
    >>> change_title_from_filename("video.mp4", "./output", replace=True)

    Process all media files in a folder with custom filename modifications:
    >>> change_title_from_filename("media_folder", "./updated", replace=False, prefix="new_", suffix="_v2")
    """

    import inspect_py as inp

    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
    }

    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(change_title_from_filename_1file)
    result = func_temp(**path_input)
    return result


@beartype
def change_title_from_filename_1file(
    filepath: str | Path
    , replace: bool = True
    , prefix: str = ""
    , suffix: str = ""
    ,errors:Literal["warn","raise"] = "raise"
    ,print_errors:bool = False
    ) -> None:
    
    """
    Update the title metadata of a media file using its filename.
    
    This function sets the title metadata of a single media file (e.g., video or audio) 
    based on its filename. It optionally renames the output file and allows for prefix/suffix customization.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the media file whose title metadata will be updated.
    
    replace : bool, default True
        If True, replaces the original file with the modified one.
        If False, creates a new file with an updated name.
    
    prefix : str, default ""
        Optional prefix to prepend to the new filename if `replace` is False.
    
    suffix : str, default ""
        Optional suffix to append to the new filename if `replace` is False.
    
    errors : {"warn", "raise"}, default "raise"
        Behavior when an error occurs:
        - "raise": Raise the exception.
        - "warn": Display a warning message and continue.
    
    print_errors : bool, default False
        If True, prints detailed error messages during processing.
    
    Returns
    -------
    None
        The function performs in-place metadata editing or creates a new file, depending on `replace`.
    
    Raises
    ------
    FileNotFoundError
        If the provided `filepath` does not exist.
    
    Notes
    -----
    - The title metadata is set to the filename (without extension).
    - When `replace` is False and no prefix or suffix is provided, `_new` is appended to the filename.
    - Internally, this function delegates the title-setting operation to `change_filetitle_1file`.
    
    Examples
    --------
    >>> change_title_from_filename_1file("video.mp4", replace=True)
    
    >>> change_title_from_filename_1file("movie.mkv", replace=False, prefix="eng_", suffix="_hd")
    """

    
    import subprocess
    import numpy as np
    import os
    from send2trash import send2trash
    from pathlib import Path

    if not os.path.exists(filepath):
        raise FileNotFoundError("Please check the path. It doesn't exist.")
    
    filepath = Path(filepath)
    filename = filepath.stem
    new_title = filename 
    
    if replace:
        new_name = f"{filename}_temp" 
    else:
       if prefix != "" or suffix != "":
           new_name = f"{prefix}{filename}{suffix}"
       else:
           new_name = f"{filename}_new"
            
    output_path = filepath.with_name(f"{new_name}{filepath.suffix}")

    change_filetitle_1file(
        filepath
        ,new_title = new_title
        ,replace = replace
        ,prefix =prefix
        ,suffix =suffix
        ,errors = errors
        ,print_errors = print_errors
        )





@beartype
def change_filetitle_1file(
        filepath: str | Path
        ,new_title: str
        , replace: bool = False
        , prefix: str = ""
        , suffix: str = ""
        ,errors:Literal["warn","raise"] = "raise"
        ,print_errors:bool = False
        ) -> None:
    
    """
    Set or update the title metadata of a media file.
    
    This function modifies the title metadata of a single media file (e.g., audio or video)
    without re-encoding. The output can either replace the original file or be saved as a new file
    with optional prefix/suffix modifications to the name.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the input media file.
    
    new_title : str
        The new title to be embedded in the file's metadata.
    
    replace : bool, default False
        If True, replaces the original file with the updated one.
        If False, creates a new file with the updated title metadata.
    
    prefix : str, default ""
        Optional prefix for the output filename if `replace` is False.
    
    suffix : str, default ""
        Optional suffix for the output filename if `replace` is False.
    
    errors : {"warn", "raise"}, default "raise"
        Error handling behavior:
        - "warn": Print a warning message if an error occurs.
        - "raise": Raise an exception if an error occurs.
    
    print_errors : bool, default False
        If True, prints detailed error output when an error is raised.
    
    Returns
    -------
    None
        The function modifies or creates a file with the updated title metadata.
    
    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    
    Exception
        If the ffmpeg command fails and `errors="raise"` is set.
    
    Notes
    -----
    - Requires `ffmpeg` to be installed and accessible via the system PATH.
    - If `replace` is True, the original file is moved to trash and replaced by the new one.
    - Metadata is updated without re-encoding (`-codec copy`).
    
    Examples
    --------
    >>> change_filetitle_1file("movie.mp4", new_title="My Movie", replace=False)
    
    >>> change_filetitle_1file("video.mkv", new_title="English Version", replace=True, errors="warn")
    """

    
    import subprocess
    import numpy as np
    import os
    from send2trash import send2trash
    from pathlib import Path
    # medium tested
    
    if not os.path.exists(filepath):
        raise FileNotFoundError("Please check the path. It doesn't exist.")
    
    filepath = Path(filepath)
    filename = filepath.stem
    
    if replace:
        new_name = f"{filename}_temp" 
    else:
       if prefix != "" or suffix != "":
           new_name = f"{prefix}{filename}{suffix}"
       else:
           new_name = f"{filename}_new"
            
    output_path = filepath.with_name(f"{new_name}{filepath.suffix}")

    
    command = [
        "ffmpeg",
        "-i", str(filepath),
        "-metadata", f"title={new_title}",
        "-codec", "copy",
        str(output_path)
    ]

    command_line = " ".join(command)
    command_np = np.array(command)
    result = subprocess.run(command, text=True, stderr=subprocess.PIPE)
    
    
    if replace:
        send2trash(filepath)
        output_path.rename(filepath)
    
    
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

@beartype
def _create_media_dict_info(df: pd.DataFrame) -> List[Dict[str, Any]]:
    info_dict_list: List[Dict[str, Any]] = []
    group_cols = ["input_video_name", "input_video_path", "output_folder", "output_name"]

    for keys, grp in df.groupby(group_cols):
        input_video_name, input_video_path, output_folder, output_name = keys
        media_df = grp[["media_type", "input_media_path", "title", "lang_code_3alpha"]]

        info_dict: Dict[str, Any] = {
            "input_video_name": input_video_name,
            "input_video_path": input_video_path,
            "output_folder": output_folder,
            "output_name": output_name,
            "media": media_df
        }

        info_dict_list.append(info_dict)

    return info_dict_list

@beartype
def merge_media_to_video(info_df:pd.DataFrame,errors:Literal["raise","warn","ignore"] = "warn") -> None:
    
    """
    SIGNATURE FUNCTION
    
    Merge additional media streams into multiple video files.
    
    This function merges audio and subtitle tracks into a video file, preserving the existing video streams. 
    The metadata (language code and title) for the added media streams can also be specified.
    
    Parameters
    ----------

    
    input_info_df : pd.DataFrame
        A DataFrame containing information about the media streams to be added.\n
        The DataFrame must have the following columns:\n
        - `input_video_name` (str): Input video file name.(Not used in the function, just for debugging purposes) \n
        - `input_video_path` (str): Path to the input video file to which the media streams will be added. \n
        - `media_type` (str): The type of media stream, either 'audio' or 'subtitle'. Any other value will raise an error.\n
        - `input_media_path` (str): The file path of the media stream to be added.\n
        - `title` (str): The title of the media stream (e.g., language or description).\n
        - `lang_code_3alpha` (str): The 3-letter language code for the media stream (e.g., "eng", "spa").\n
        - `output_folder` (str): Path to the folder where the output video file will be saved..\n
        - `output_name` (str): The name of the output video file. If not specified, the original video's name is retained.\n
        
        Misspelling of column names or invalid values in `media_type` will result in an error.\n
    
    Returns
    -------
    None
        The merged video file is saved to the specified output folder.
    
    Raises
    ------
    ValueError
        If the DataFrame `input_info_df` is missing required columns or contains invalid values for `media_type`.
    
    Notes
    -----
    - The input video file is retained as-is, and the additional media streams are appended.
    - Metadata such as language and title for each media stream is applied during the merging process.
    - The function uses `ffmpeg` for processing; ensure it is installed and available in the system's PATH.
    
    """
    # medium tested
    # took about 30 min to write and tested
    
    
    
    from tqdm import tqdm
    info_dict_list = _create_media_dict_info(info_df)
    
    for i, curr_info_dict in tqdm(enumerate(info_dict_list), total=len(info_dict_list), desc="Creating Videos"):
        try:
            merge_media_to1video(
                input_video_path = curr_info_dict["input_video_path"]
                , input_info_df = curr_info_dict["media"]
                , output_folder = curr_info_dict["output_folder"]
                ,output_name = curr_info_dict["output_name"]
                ,errors = "raise"
                ,print_errors=False
                )
        except (TypeError,UnboundLocalError) as e:
            print(f"There's an error in while processing: {curr_info_dict['input_video_path']}\n")
            print(e)
            print()
        except FileNotFoundError as e:
            print(e)
            print(f"There's no file in path: {curr_info_dict['input_video_path']}\n")
        except Exception as e:
            print("This is new Error Type")
            print(e)
            print(type(e))
            print(f"There's an error in while processing: {curr_info_dict['input_video_path']}\n")

@beartype
def merge_media_to1video(
    input_video_path: Union[str, Path],
    input_info_df:pd.DataFrame,
    output_folder: str,
    output_name: Union[str, Path] = "",
    errors:Literal["raise","warn","ignore"] = "warn",
    print_errors:bool = True
) -> None:
    import numpy as np
    # toAdd01: Add Useful OSError when any of paths aren't found
    
    """
    Merge additional media streams into a video file.
    
    This function merges audio and subtitle tracks into a video file, preserving the existing video streams. 
    The metadata (language code and title) for the added media streams can also be specified.
    
    Parameters
    ----------
    input_video_path : str or Path
        Path to the input video file to which the media streams will be added.
    
    input_info_df : pd.DataFrame
        A DataFrame containing information about the media streams to be added.\n
        The DataFrame must have the following columns:\n
        - `media_type` (str): The type of media stream, either 'audio' or 'subtitle'. Any other value will raise an error.\n
        - `input_media_path` (str): The file path of the media stream to be added.\n
        - `title` (str): The title of the media stream (e.g., language or description).\n
        - `lang_code_3alpha` (str): The 3-letter language code for the media stream (e.g., "eng", "spa").\n
        Misspelling of column names or invalid values in `media_type` will result in an error.\n
    
    output_folder : str
        Path to the folder where the output video file will be saved.
    
    output_name : str or Path, optional, default ""
        The name of the output video file. If not specified, the original video's name is retained.
    
    Returns
    -------
    None
        The merged video file is saved to the specified output folder.
    
    Raises
    ------
    ValueError
        If the DataFrame `input_info_df` is missing required columns or contains invalid values for `media_type`.
    
    Notes
    -----
    - The input video file is retained as-is, and the additional media streams are appended.
    - Metadata such as language and title for each media stream is applied during the merging process.
    - The function uses `ffmpeg` for processing; ensure it is installed and available in the system's PATH.
    
    Examples
    --------
    >>> input_video_path = "example.mp4"
    >>> input_info_df = pd.DataFrame({
    ...     "media_type": ["audio", "subtitle"],
    ...     "input_media_path": ["example_audio.mp3", "example_subtitle.srt"],
    ...     "title": ["English Audio", "English Subtitles"],
    ...     "lang_code_3alpha": ["eng", "eng"]
    ... })
    >>> output_folder = "./output"
    >>> output_name = "merged_video.mp4"
    >>> merge_media_to1video(input_video_path, input_info_df, output_folder, output_name)
    """

    # tested with 1 video

    import subprocess
    from pathlib import Path
    import os 
    import warnings

    video_path = Path(input_video_path)
    video_name = video_path.stem
    if output_name == "":
        output_path = Path(output_folder) / f"{video_name}.mkv"
    else:
        output_path = Path(output_folder) / output_name

    
    
    if not os.path.exists(video_path):
        if errors in ["raise"]:
            raise FileNotFoundError(f"Please check your input video path for {video_path}")
        elif errors in ["warn"]:
            warnings.warn(f"Please check your input video path for {video_path}",category=UserWarning)

    command = ['ffmpeg', '-i', str(video_path)]

    files_not_found = 0
    file_not_found_text = ""
    for _, row in input_info_df.iterrows():
        if not os.path.exists(str(row['input_media_path'])):
            files_not_found += 1
            file_not_found_text += f"\nPath media doesn't exist: {str(row['input_media_path'])}"

        command.extend(['-i', str(row['input_media_path'])])

    if files_not_found > 0:
        if errors in ["raise"]:
            raise FileNotFoundError(file_not_found_text)
        elif errors in ["warn"]:
            warnings.warn(f"Please check your input video path for {video_path}",category=UserWarning)
        else:
            return

    command.append('-map')
    command.append('0')

    audio_count = count_audio(input_video_path) 
    sub_count = count_subtitle(input_video_path) 
    total_media = len(input_info_df)

    # Mapping
    for idx, row in enumerate(input_info_df.itertuples(), start=1):
        if row.media_type == 'audio':
            command.append('-map')
            command.append(f'{idx}:a')
        elif row.media_type == 'subtitle':
            command.append('-map')
            command.append(f'{idx}:s')

    # Metadata
    for row in input_info_df.itertuples():
        lang = row.lang_code_3alpha
        title = row.title
        if row.media_type == 'audio':
            command.extend([f'-metadata:s:a:{audio_count}', f'language={lang}'])
            command.extend([f'-metadata:s:a:{audio_count}', f'title={title}'])
            audio_count += 1
        elif row.media_type == 'subtitle':
            command.extend([f'-metadata:s:s:{sub_count}', f'language={lang}'])
            command.extend([f'-metadata:s:s:{sub_count}', f'title={title}'])
            sub_count += 1

    command.extend(['-c', 'copy', str(output_path)])
    # command_line, command_np is for debugging
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

# unlock bear type for now because I want to support list[int] as well
# @beartype
def export_audio(audio_segment:AudioSegment,
                 start_end_time_dict: Dict[int,Tuple[int,int]|List[int]],
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

    """
    # TOADD_01: replace => it would check if file already exists, if so depending on it's True or False, it would replace the file
    # TOADD_02: replace => when there's more filenames then timestamp

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

@beartype
def merge_sub_to_video(
    input_video_path: Union[str, Path],
    input_subtitle_path: Union[List[Union[str, Path]], Union[str, Path]],
    sub_lang_code_3alpha: Union[List[str], str],
    sub_title: Union[List[str], str],
    output_name: str,
    output_folder: Union[str, Path] = "",
    replace:bool = False,
) -> None:
    """
    Merges a video file with additional subtitle tracks, assigning metadata such as language and title to each subtitle track.

    Parameters
    ----------
    input_video_path : str or Path
        The path to the input video file.
    input_subtitle_path : list of str/Path or str/Path
        The path(s) to the input subtitle file(s). Can be a single path or a list of paths.
    subtitle_lang_code_3alpha : list of str or str
        The language code(s) for the subtitle track(s) (e.g., 'fre' for French). Can be a single code or a list.
    subtitle_title : list of str or str
        The title(s) for the subtitle track(s) (e.g., 'French'). Can be a single title or a list.
    output_folder : str or Path
        The folder where the output video file will be saved.
    output_name : str
        The name of the output video file.

    Returns
    -------
    None
    """
    import subprocess
    # Ensure inputs are lists for consistent processing
    # tested input_subtitle_path as list and single string, 
    # tested replace = True
    if isinstance(input_subtitle_path, (str, Path)):
        input_subtitle_path = [input_subtitle_path]
    if isinstance(sub_lang_code_3alpha, str):
        sub_lang_code_3alpha = [sub_lang_code_3alpha]
    if isinstance(sub_title, str):
        sub_title = [sub_title]

    # Check for consistent lengths of inputs
    if not (len(input_subtitle_path) == len(sub_lang_code_3alpha) == len(sub_title)):
        raise ValueError("The lengths of input_subtitle_path, subtitle_lang_code_3alpha, and subtitle_title must match.")

    video_path = Path(input_video_path)
    output_path = Path(output_folder) / output_name

    # Construct the ffmpeg command
    if replace:
        command = ['ffmpeg', '-y', '-i', str(video_path)]
    else:
        command = ['ffmpeg', '-i', str(video_path)]

    # Add all subtitle inputs
    for subtitle in input_subtitle_path:
        command.extend(['-i', str(subtitle)])

    # Add mapping for video and subtitles
    command.append('-map')
    command.append('0')  # Map all streams from video
    for idx in range(len(input_subtitle_path)):
        command.append('-map')
        command.append(f'{idx + 1}:s')  # Map each subtitle file

    # Add metadata for each subtitle track
    start_index = get_sub_index_latest(input_video_path) + 1
    
    for idx, (lang, title) in enumerate(zip(sub_lang_code_3alpha, sub_title), start=start_index):
        command.extend(['-metadata:s:s:' + str(idx), f'language={lang}'])
        command.extend(['-metadata:s:s:' + str(idx), f'title={title}'])

    # Add codec settings and output file
    command.extend(['-c', 'copy', str(output_path)])

    # cmd_line is just for debugging
    cmd_line = ' '.join(command)

    # Execute the command
    result = subprocess.run(command, text=True, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error encountered:")
        print(result.stderr)

@beartype
def merge_audio_to_video(
    input_video_path: Union[str, Path],
    input_audio_path: Union[List[Union[str, Path]], Union[str, Path]],
    audio_lang_code_3alpha: Union[List[str], str],
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
    if isinstance(audio_lang_code_3alpha, str):
        audio_lang_code_3alpha = [audio_lang_code_3alpha]
    if isinstance(audio_title, str):
        audio_title = [audio_title]

    # Check for consistent lengths of inputs
    if not (len(input_audio_path) == len(audio_lang_code_3alpha) == len(audio_title)):
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
    for idx, (lang, title) in enumerate(zip(audio_lang_code_3alpha, audio_title), start=2):
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

del Union,List,Tuple, Literal, Callable, Dict, Any, Path
del AudioSegment
del beartype, pkg_resources
# the diff between fix_bug vs cant_use is that:
#   fix_bug: you can still use some functionality of it, it's that there's some parameter like(alarm path) that still have the problem
#   cant_use: the main functionality is not correct, or may not work entirely

from pydub import AudioSegment
from typing import Union,List,Tuple, Literal, Callable, Dict, Any, Optional
from pathlib import Path
from video_toolkit.ffmpeg_extract import *
import pandas as pd
from beartype import beartype
import pkg_resources

def reset_start_timestamp_1audio(
        filepath: str | Path
        , new_start_ts: float|int = 0
        , outfilename: str = None
        , output_folder: str | Path = ""):
    
    """
    Reset the start timestamp of a single-audio file by rewriting its PTS.

    Parameters
    ----------
    filepath : str or Path
        Path to the input audio file.
    new_start_ts : float, optional
        Desired start timestamp in seconds (default is 0).
    outfilename : str, optional
        Filename for the output file. If None, uses the original filename prefixed with 'fixed_'.
    output_folder : str or Path, optional
        Directory to save the output file. If empty, saves alongside the input file.

    Returns
    -------
    Path
        Path to the output audio file.
    """
    import subprocess
    from pathlib import Path

    input_path = Path(filepath)
    output_dir = Path(output_folder) if output_folder else input_path.parent
    output_name = outfilename if outfilename else f"{input_path.name}"
    output_path = output_dir / output_name

    # filter_expr = f"asetpts=PTS-STARTPTS+{new_start_ts}/TB"

    filter_expr = f"asetpts=PTS-STARTPTS"
    # cmd = [
    #     "ffmpeg",
    #     "-i", str(input_path),
    #     "-af", filter_expr,
    #     "-c:a", "copy" if new_start_ts == 0 else "aac",
    #     str(output_path)
    # ]

    filter_expr = f"asetpts=PTS-STARTPTS+{new_start_ts}/TB"

    cmd = [
        "ffmpeg",
        "-y",                       # overwrite
        "-fflags", "+genpts",       # regenerate PTS on input
        "-i", str(input_path),      # input
        "-af", filter_expr,         # shift timestamps
        "-c:a", "libmp3lame",       # re-encode to MP3
        "-avoid_negative_ts", "make_zero",  # zero-out the first ts
        str(output_path)
    ]

    subprocess.run(cmd, check=True)
    return output_path


# def reset_start_timestamp_1audio(
#     filepath: str | Path,
#     outfilename: str|None = None,
#     new_start_ts: float|int = 0,
#     output_folder: str | Path = ""
# ) -> Path | None:
#     """
#     Resets the start timestamp of an audio file using ffmpeg.

#     This function creates a copy of the audio file with a new start timestamp.
#     It works by adjusting the container's muxing delay, which avoids re-encoding
#     the audio stream and therefore preserves the original quality.

#     Note: This method is generally effective for container formats like MP4, MOV,
#     and MKV. Its behavior might differ with other formats.

#     Args:
#         filepath: The path to the input audio file.
#         outfilename: The name for the new output audio file.
#         new_start_ts: The desired new start timestamp in seconds. Defaults to 0.
#         output_folder: The directory where the output file will be saved.
#                        If empty, it defaults to the current working directory.

#     Returns:
#         A Path object pointing to the newly created audio file if successful,
#         otherwise None.
#     """

#     # this doesn't work from Gemini
#     import logging
#     import subprocess
#     from pathlib import Path

#     # try:
#     #     check_ffmpeg()
#     # except FileNotFoundError as e:
#     #     logging.error(e)
#     #     return None

#     input_path = Path(filepath)
#     if not input_path.is_file():
#         logging.error(f"Error: Input file not found at '{input_path}'")
#         return None

#     # Determine the output directory and create it if it doesn't exist
#     output_dir = Path(output_folder) if output_folder else Path.cwd()
#     output_name = outfilename if outfilename else f"{input_path.name}"
#     output_dir.mkdir(parents=True, exist_ok=True)
#     output_path = output_dir / output_name


#     # Prevent overwriting the source file by mistake
#     if input_path.resolve() == output_path.resolve():
#         logging.error("Error: Input and output file paths cannot be the same.")
#         return None

#     # The ffmpeg command to copy the stream and set a new start time via muxing delay
#     command = [
#         "ffmpeg",
#         "-i", str(input_path),
#         "-c", "copy",              # Copy the codec to avoid re-encoding
#         "-muxpreload", str(new_start_ts), # Set preload time for the container
#         "-muxdelay", str(new_start_ts),   # Set delay, effectively changing the start time
#         "-y",                      # Automatically overwrite the output file if it exists
#         str(output_path),
#     ]

#     logging.info(f"Executing command: {' '.join(command)}")

#     try:
#         # Run the ffmpeg command
#         process = subprocess.run(
#             command,
#             check=True,  # This will raise a CalledProcessError for non-zero exit codes
#             capture_output=True,
#             text=True,
#             encoding='utf-8'
#         )
#         logging.info(f"Successfully created new audio file at '{output_path}'")
#         # Log stderr as ffmpeg often writes progress and info there
#         logging.debug(f"ffmpeg output:\n{process.stderr}")
#         return output_path
#     except subprocess.CalledProcessError as e:
#         logging.error("ffmpeg failed to execute.")
#         logging.error(f"Return Code: {e.returncode}")
#         logging.error(f"ffmpeg stderr:\n{e.stderr}")
#         return None


def reset_start_timestamp(
    filepaths: Union[str, Path, list[str|Path]]
    ,output_folder: str|Path

    # input below would get import automatically
    ,new_start_ts: float|int = 0

    # handle_multi_input parameters
    ,progress_bar: bool = True
    ,verbose: int = 1
    ,alarm_done: bool = False
    ,alarm_error: bool = False
    ,input_extension: str|None = [".mp3",".mp4",".wav",".srt",".mkv",".avi"]
    ) -> None:
    

    """
    Reset the start timestamp of media files.

    Parameters
    ----------
    filepaths : str or Path or list[str|Path]
        Filepath(s) of the media file(s) to process.
    output_folder : str or Path
        Folder to save the output media file(s) to.
    new_start_ts : float or int, optional
        New start timestamp to set for the media file(s). Defaults to 0.
    progress_bar : bool, optional
        Whether to show a progress bar when processing folders/lists. Defaults to True.
    verbose : int, optional
        Verbosity level (0=quiet, 1=normal, 2=detailed output). Defaults to 1.
    alarm_done : bool, optional
        Play success sound after completion. Defaults to False.
    alarm_error : bool, optional
        Play error sound if processing fails. Defaults to False.
    input_extension : str or None, optional
        File extension(s) to limit the processing to. If None, all files in the folder(s) will be processed. Defaults to [".mp3",".mp4",".wav",".srt",".mkv",".avi"].

    Returns
    -------
    None
    """
    import inspect_py as inp

    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
        ,"outfilename":None
    }

    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(reset_start_timestamp_1audio)
    result = func_temp(**path_input)
    return result
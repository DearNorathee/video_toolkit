from video_toolkit.utils_vt import *
from pydub import AudioSegment
import os_toolkit as ost


def test_clean_netflix_srt_1file():
    sub_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
    output_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original_no_speakers"
    clean_Netflix_srt_1file(sub_path, output_folder)

def test_clean_netflix_srt():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original"
    output_folder01 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_01"

    sub_path02 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
    output_folder02 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_02"

    sub_path03 = [
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt",
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E02.srt",
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E03.srt",
        
        ]
    output_folder03 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_03"

    sub_path04 = [
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original"
    ]
    output_folder04 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_04"

    clean_Netflix_srt(sub_path01, output_folder01)
    clean_Netflix_srt(sub_path02, output_folder02)
    clean_Netflix_srt(sub_path03, output_folder03)
    # list of folders are not yet implemented in inp.handle_multi_input
    # clean_Netflix_srt(sub_path04, output_folder04)  

def test_change_audio_speed():
    audio_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\French"
    test_output = r"C:\C_Video_Python\video_toolkit_test\test_change_audio_speed"
    test_output_paths = [None for _ in range(100)]

    for i, curr_path in enumerate(test_output_paths):
        test_output_paths[i] = Path(test_output) / f"test_{str(i).zfill(2)}"

    for i in range(1,2):
        ost.delete_files_in_folder(test_output_paths[i],verbose=0)
    
    change_audio_speed(audio_paths = audio_path01,speedx=0.96,output_folder=test_output_paths[1])

def test_change_audio_speed_1file():
    # I use this function to create 1 audio per episode
    audio_path01 = r"C:\C_Video_Python\video_toolkit_test\change_audio_speed_1file\BigBang season1 French\BigBang FR S01E13_FR.mp3"
    output_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\French_adj_speed"
    SPEEDX = 0.95903619926980600
    change_audio_speed_1file(audio_path01,SPEEDX,"BigBang FR S01E13_FR_cs_v2.mp3",output_folder = output_folder)

def test_change_subtitle_speed():
    test_input01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base"
    test_output = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\video_toolkit_test\test_change_subtitle_speed"
    test_output_paths = [None for _ in range(100)]

    for i, curr_path in enumerate(test_output_paths):
        test_output_paths[i] = Path(test_output) / f"test_{str(i).zfill(2)}"

    for i in range(1,5):
        ost.delete_files_in_folder(test_output_paths[i],verbose=0)

    change_subtitle_speed(test_input01,speedx=0.96,output_folder=test_output_paths[1] )             
    change_subtitle_speed(test_input01,speedx=0.96,prefix="prefix",output_folder=test_output_paths[2] )                    
    change_subtitle_speed(test_input01,speedx=0.96,suffix="0.96x",output_folder=test_output_paths[3] )       
    change_subtitle_speed(test_input01,speedx=0.96,prefix="shift2sec",suffix="0.96x",output_folder=test_output_paths[4],shift_forward_sec=2 )   

def test_change_subtitle_speed_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    output_folder01 = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_subtitle_speed_1file"
    change_subtitle_speed_1file(sub_path01,2, output_folder01, suffix="speedx_2")
    change_subtitle_speed_1file(sub_path01,0.96, output_folder01, suffix="speedx_0.96")
    change_subtitle_speed_1file(sub_path01,0.959, output_folder01, suffix="speedx_0.959")

def test_change_subtitle_speed_df_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    df_sub_modified = change_subtitle_speed_df_1file(sub_path01,2)

def test_adjust_speed():
    time01 = datetime.time(0,2,0)
    time02 = datetime.time(0,1,30)
    
    expect01_01 = datetime.time(0,1,0)
    expect01_02 = datetime.time(0,1,10)
    expect02_01 = datetime.time(0,0,45)
    
    actual01_01 = adjust_speed(time_obj = time01, speedx = 2)
    actual01_02 = adjust_speed(time_obj = time01, speedx = 2, shift_forward_sec=10)
    actual02_01 = adjust_speed(time_obj = time02, speedx = 2)


    
    #write assert
    assert expect01_01 == actual01_01
    assert expect01_02 == actual01_02
    assert expect02_01 == actual02_01

def test_change_title_from_filename():
    # passed for all inputs types
    input_01_path = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_title_from_filename\input_01"
    output_01_path = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_title_from_filename\output_01"

    input_02_path = [
        r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_title_from_filename\input_02\01 Tears of Gold.mp3"
        ,r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_title_from_filename\input_02\08 Faouzia  Puppet.mp3"
        ,r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_title_from_filename\input_02\12 Faouzia  Desert Rose.mp3"
    ]

    input_03_path = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_title_from_filename\input_02\05 Reflection Christina Aguilera.mp3"
    
    change_title_from_filename(filepaths=input_01_path,output_folder=output_01_path,replace=False,verbose=0)
    change_title_from_filename(filepaths=input_02_path,output_folder=output_01_path,replace=False)
    change_title_from_filename(filepaths=input_03_path,output_folder=output_01_path,replace=False)

def test_split_audio_by_sub():
    media_paths: list[str] = [
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E03 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E04 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E05 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E06 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E07 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E08 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E09 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E10 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E11 PT_PT.mp3",

    ]
    sub_paths: list[str] = [
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E03 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E04 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E05 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E06 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E07 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E08 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E09 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E10 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E11 PT_PT.srt",
    ]
    main_output_folder = r"H:\D_Video_Python\Portuguese\The Ark_PT\Splited Audio PT_test"
    ost.delete_files_in_folder(main_output_folder)
    split_audio_by_sub(media_paths=media_paths,sub_paths=sub_paths,output_folder=main_output_folder,modify_sub=True)

def test_ass_to_df():
    filepath = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle ori Extracted\BigBang FR S02E01_1.ass"
    actual01 = ass_to_df(filepath)
    print()

def test_export_audio():
    filepath = r"G:\My Drive\G_Videos\Learn French\Learn to speak French in 5 minutes - a dialogue for beginners!.mp3"
    audio = AudioSegment.from_file(filepath) 

    OUTPUT_FOLDER:str = r"G:\My Drive\G_Videos\Learn French\Pydub Export test01"

    start_time = 35 * 1000  # Start at 35 seconds
    end_time = (1*60 + 35) * 1000    # End at 1 minute and 35 seconds
    
    manual_edit = {
        6:  [14_633 , 15_933],
        7:  [24_455 , 25_534],
        8:  [25_700 , 27_550],
        9:  [27_899 , 30_000],
        10: [31_075 , 32_863],
        11: [33_439 , 36_188],
        12: [37_280 , 42_100],
        14: [42_865 , 47_224],
        
        }
    
    # output_names01 has no index 10
    output_names01 = {
        6:  "01.01_I'm....mp3",
        7:  "01.02_Pleased to meet you.mp3",
        8:  "01.03_That's a nice name.mp3",
        9:  "01.05_Can I ask you a question?.mp3",
        11: "01.06_What do you like to do on a weekend?.mp3",
        12: "01.07_I like to learn French and read and you?.mp3",
        14: "01.08_I like to watch television.mp3",
        
        }
    
    output_names02 = {
        6:  "01.01_I'm....mp3",
        7:  "01.02_Pleased to meet you.mp3",
        8:  "01.03_That's a nice name.mp3",
        9:  "01.05_Can I ask you a question?.mp3",
        10: "01.07_Yes, of course.mp3",
        11: "01.08_What do you like to do on a weekend?.mp3",
        12: "01.09_I like to learn French and read and you?.mp3",
        14: "01.10_I like to watch television.mp3",
        
        }
    
    output_names03 = {
        6:  "01.01_I'm....wav",
        7:  "01.02_Pleased to meet you.wav",
        8:  "01.03_That's a nice name.wav",
        9:  "01.05_Can I ask you a question?.wav",
        10: "01.07_Yes, of course.mp3",
        11: "01.08_What do you like to do on a weekend?.wav",
        12: "01.09_I like to learn French and read and you?.wav",
        14: "01.10_I like to watch television.wav",
        
        }
    
    # Extract the segment from the audio
    segment = audio[start_time:end_time]
    try:
        export_audio(segment, manual_edit, output_names01,output_folder=OUTPUT_FOLDER)
    except Exception as error:
        assert isinstance(error, KeyError)
        
    export_audio(segment, manual_edit, output_names02,output_folder=OUTPUT_FOLDER)
    export_audio(segment, manual_edit, output_names03,output_folder=OUTPUT_FOLDER)

def test_text_to_milisecond():
    import inspect_py as inp
    actual01 = text_to_milisecond("4.32") # Output: 272000
    actual02 = text_to_milisecond("1.40.32")  # Output: 6032000
    actual03 = text_to_milisecond(5000)  # Output: 5000
    
    expect01 = 272_000
    expect02 = 6032000
    expect03 = 5000
    
    assert actual01 == expect01, inp.assert_message(actual01, expect01)
    assert actual02 == expect02, inp.assert_message(actual02, expect02)
    assert actual03 == expect03, inp.assert_message(actual03, expect03)

def test_extract_audio_1file():
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    chosen_video_name = "The Big Bang Theory_S06E01.mkv"
    chosen_video_path = folder_FR_bigbang / chosen_video_name
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    
    output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_01_all"
    output_folder02 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_02_only_French"
    output_folder03 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_03_Matrix_some_misspelled"
    output_name = "BigBang_FR_S06E01"
    
    
    
    matrix_video_path = r"G:/My Drive/G_Videos/Polyglot/The Matrix Resurrections 2021.mkv"
    # extract_audio_1file(video_path = chosen_video_path,
    #                     output_folder = output_folder01,
    #                     output_name = output_name,
    #                     alarm_done_path = alarm_done_path)
    
    # extract_audio_1file(video_path = chosen_video_path,
    #                     output_folder = output_folder02,
    #                     alarm_done_path = alarm_done_path,
    #                     languages="french"
    #                     )
    
    extract_audio_1file(video_path = matrix_video_path,
                        output_folder = output_folder03,
                        alarm_done = alarm_done_path,
                        languages=["french","portugus","spanish","englih"]
                        )

def test_extract_audio3():
    import video_toolkit as vt
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio3\test_01"
    vt.extract_audio(folder_FR_bigbang, output_folder01)
    print("test_extract_audio3")

def test_extract_1_audio():
    
    folder = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06")
    video_name = "The Big Bang Theory French S06E01.mp4"
    video_path = folder / video_name
    output_folder = Path(r"C:\Users\Heng2020\OneDrive\Python NLP\NLP 06_ffmpeg")
    output_name = "The Big Bang Theory French S06E01.mp3"
    output_path = output_folder / output_name
    
    extract_1_audio(video_path,output_folder,output_name)
    extract_1_audio(video_path,output_folder,output_name,overwrite_file = False)

def test_extract_audio():
    
    from pathlib import Path
    French_bigbang = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06")
    output_folder = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06\Audio")
    extract_audio1(French_bigbang,output_folder,n_limit=10)
    return True

def test_crop_video():
    from pathlib import Path
    video_path = r"C:\Users\Heng2020\OneDrive\Python NLP\InputData\Westworld S04E01 Portuguese.mkv"
    t1 = "0:02:25"
    t2 = "0:06:00"
    
    crop_video(video_path,t1,t2)

def test_create_subtitle():
    import whisper
    from whisper.utils import get_writer
    from playsound import playsound
    from time import time
    
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    
    ts01 = time()
    
    input_path = r"C:\Users\Heng2020\OneDrive\Python NLP\InputData\Westworld S04E01 Portuguese_01.mkv"
    
    model = whisper.load_model("base")
    result = model.transcribe(input_path)
    
    output_directory = r"C:\Users\Heng2020\OneDrive\Python NLP\InputData\Westworld S04E01 Portuguese_01.srt"
    
    writer = get_writer("srt", str(output_directory))
    # writer(result, output_name)
    ts02 = time()
    
    duration = ts02 - ts01 
    print(duration)

test_split_audio_by_sub()
# test_ass_to_df()
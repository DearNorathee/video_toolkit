from video_toolkit.whisper import *
import whisper
# pip install -U stable-ts
import stable_whisper
def test_transcribe_to_subtitle_1file():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    model = stable_whisper.load_model('base')
    BigBangFR_S02E01 = r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle"
    audio_to_sub_1file(model,BigBangFR_S02E01,output_folder = output_folder)


def test_transcribe_to_subtitle():
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    bigBang_FR_season2 = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle"
    faster_model_base = stable_whisper.load_faster_whisper('base')
    audio_to_sub(faster_model_base,bigBang_FR_season2,output_folder = output_folder)


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
    writer(result, output_name)
    ts02 = time()
    
    duration = ts02 - ts01 
    print(duration)
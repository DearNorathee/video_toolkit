from video_toolkit.ffmpeg_create import *

def test_merge_media_to1video():
    input_video_path = r"C:\C_Video_Python\Merge Language Video\BigBang PT Season 06\BigBang PT S06E02.mkv"
    output_folder = r"C:\C_Video_Python\Merge Language Video\tests\outputs"
    output_name = "BigBang All S06E02_v02.mkv"
    
    info_df = pd.DataFrame({
        'media_type': ['subtitle','audio','subtitle'],
        'input_media_path': [
            r'C:\C_Video_Python\Merge Language Video\BigBang PT Season 06\BigBang PT S06E02.srt',
            r'C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\Season 06 Audio\BigBang FR S06E02_FR.mp3',
            r'C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\Season 06 Audio\French Subtitle\BigBang FR S06E02_FR.srt',
            ],
        'title': ['Portuguese_Brazilian_whisper','French','French_whisper'],
        'lang_code_3alpha': ['por','fre','fre']
        
        })
    
    merge_media_to1video(input_video_path,info_df,output_folder,output_name)
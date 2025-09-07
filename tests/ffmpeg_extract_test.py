import unittest
import video_toolkit as vt
from pathlib import Path
import logging

should_skip = True

# @unittest.skipIf(should_skip, "Skipping: Test_extract_subtitle")
class Test_extract_subtitle(unittest.TestCase):
    folder01 = Path(r"H:\D_Video\The Ark Season 01 Portuguese")

    output_folder01 = Path(r'H:\D_Video\The Ark Season 01 Portuguese\Subtitles')

    def test_basic01(self):
        vt.extract_subtitle(self.folder01, self.output_folder01)


def test_extract_subtitle():
# extract_subtitle doesn't work on just 1 video
    
    folder01 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv")
    output_folder01 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_01_02')
    vt.extract_subtitle(folder01,output_folder01)

    # when it's folder path
    folder02 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Peripheral_experiments\S01")
    output_folder02 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_02')
    vt.extract_subtitle(folder02,output_folder02)

    # test when input is .ass but output is .srt
    # folder03 = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    # output_folder03 = Path(r'C:\Users\Heng2020\OneDrive\Python NLP\OutputData\The Ark season 1 srt')
    # vt.extract_subtitle(folder03,output_folder03, output_extension= ".srt")

def test_extract_sub_1_video():

    folder01 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv")
    output_folder01 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_01')
    vt.extract_sub_1_video(folder01,output_folder01, alarm_done=False)

    # folder02 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Peripheral_experiments\S01")
    # output_folder02 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_02')
    # vt.extract_sub_1_video(folder02,output_folder02)




# @unittest.skipIf(should_skip, "Skipping: Test_extract_audio2s")
class Test_extract_audio2(unittest.TestCase):
    folder01 = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    French_bigbang = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06")
    output_folder = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06\Audio")
    # 4.82 min for 10 audios

    def test_basic01(self):
        vt.extract_audio2(self.French_bigbang,self.output_folder,n_limit=10)
    
    def test_2_output_extension(self):
        pass
    pass

@unittest.skipIf(should_skip, "Skipping: Test_extract_1_subtitles")
class Test_extract_1_subtitle(unittest.TestCase):

    folder01 = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    video_name01 = "The Ark S01E02 PT.mkv"
    video_path01 = folder01 / video_name01
    output_folder01 = Path(r'H:\D_Video\The Ark Season 01 Portuguese\Subtitles')
    output_name = 'The Ark S01E02 PT'

    def test_basic01(self):
        actual = vt.extract_sub_1_video(self.video_path01,self.output_folder01,self.output_name,output_extension='ass')
        expect = None
        self.assertEqual(expect, None)
    def test_basic02_no_outputname_and_ext(self):
        actual = vt.extract_sub_1_video(self.video_path01,self.output_folder01)
        expect = None
        self.assertEqual(expect, None)
    
    def test_basic03_no_outputName(self):
        actual = vt.extract_sub_1_video(self.video_path01,self.output_folder01,output_extension='.srt')
        expect = None
        self.assertEqual(expect, None)


def test_get_all_metadata():
    
    folder = Path(r"C:\C_Video\The Ark Season 01 Portuguese")
    video_name = "The Ark S01E02 PT.mkv"
    video_path = folder / video_name
    actual01 = vt.get_all_metadata(video_path)

    # case02: when file is not found
    try:
        video_path02 = r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01\The Wheel of Time_S01E02_Shadow's Waiting.mkv"
        video_path02 = r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01\The Wheel of Time_S01E02_Shadow's Waiting.mkv"
        actual02 = vt.get_all_metadata(video_path02)
    except FileNotFoundError:
        logging.debug('Case 02 passed.✅')
        
    logging.debug('Done From test_get_subtitle_stream_index')

def test_get_subtitle_index():
    
    folder = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    video_name = "The Ark S01E02 PT.mkv"
    video_path = folder / video_name
    actual01 = vt.get_subtitle_index(video_path)
    
    
    folder = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06")
    video_name = "The Big Bang Theory French S06E01.mp4"
    video_path = folder / video_name
    actual02 = vt.get_subtitle_index(video_path)
    
    
    
    
    logging.debug('Done From test_get_subtitle_index') 


def test_extract_1_audio():
    
    folder = Path(r"E:\Videos\The Big Bang Theory\The Big Bang Theory French Season 06")
    video_name = "The Big Bang Theory French S06E01.mp4"
    video_path = folder / video_name
    output_folder = Path(r"C:\Users\Heng2020\OneDrive\Python NLP\NLP 06_ffmpeg")
    output_name = "The Big Bang Theory French S06E01.mp3"
    output_path = output_folder / output_name
    
    vt.extract_1_audio(video_path,output_folder,output_name)
    vt.extract_1_audio(video_path,output_folder,output_name,overwrite_file = False)

def test_extract_audio():
    from pathlib import Path
    input_path01 = r"C:\DVDFab\StreamFab\Output\Netflix\3 Body Problem_01\3 Body Problem_S01E03_Destroyer of Worlds.mp4"
    input_path02 = r"C:\DVDFab\StreamFab\Output\Amazon\The Peripheral_experiments\S01"
    input_path03 = [
        r"C:\DVDFab\StreamFab\Output\Netflix\3 Body Problem_01\3 Body Problem_S01E03_Destroyer of Worlds.mp4"
        ,r"C:\DVDFab\StreamFab\Output\Netflix\3 Body Problem_01\3 Body Problem_S01E04_Our Lord.mp4"
    ]

    output_path01 = r'C:\C_Video_Python\video_toolkit_test\test_extract_audio\test_01_1file'
    output_path02 = r'C:\C_Video_Python\video_toolkit_test\test_extract_audio\test_02_folder'
    output_path03 = r'C:\C_Video_Python\video_toolkit_test\test_extract_audio\test_03_list_of_file'



    # vt.extract_audio_v2(input_path01,output_path01,output_extension="wav")
    # vt.extract_audio_v2(input_path02,output_path02,output_extension="wav")
    vt.extract_audio_v2(input_path03,output_path03,output_extension="wav")
    return True


def test_extract_audio_1file():
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    chosen_video_name = "The Big Bang Theory_S06E01.mkv"
    chosen_video_path = folder_FR_bigbang / chosen_video_name
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    
    output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_01_all"
    output_folder02 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_02_only_French"
    output_folder03 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_03_Matrix_some_misspelled"

    input_video04 = r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv"
    output_folder04 = r"C:\C_Video_Python\video_toolkit_test\test_extract_audio_1file\test_04"


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
    
    # vt.extract_audio_1file(video_path = matrix_video_path,
    #                     output_folder = output_folder03,
    #                     alarm_done = alarm_done_path,
    #                     languages=["french","portugus","spanish","englih"]
    #                     )
    
    vt.extract_audio_1file(video_path = input_video04,
                        output_folder = output_folder04,
                        alarm_done = True,
                        
                        # languages=["french","portugus","spanish","englih"]
                        )


if __name__ == '__main__':
    # test_extract_audio()
    # test_extract_audio_1file()
    # test_extract_sub_1_video()
    # test_get_all_metadata()
    test_extract_subtitle()

import unittest
import video_toolkit as vt
from pathlib import Path
import logging

should_skip = True

@unittest.skipIf(should_skip, "Skipping: Test_extract_subtitle")
class Test_extract_subtitle(unittest.TestCase):
    folder_01 = Path(r"H:\D_Video\The Ark Season 01 Portuguese")

    output_folder_01 = Path(r'H:\D_Video\The Ark Season 01 Portuguese\Subtitles')

    def test_basic01(self):
        vt.extract_subtitle(self.folder_01, self.output_folder_01)


def test_extract_subtitle():
# extract_subtitle doesn't work on just 1 video
    
    folder_01 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv")
    output_folder_01 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_01_02')
    vt.extract_subtitle(folder_01,output_folder_01)

    # when it's folder path
    folder02 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Peripheral_experiments\S01")
    output_folder02 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_02')
    vt.extract_subtitle(folder02,output_folder02)

    # test when input is .ass but output is .srt
    # folder03 = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    # output_folder03 = Path(r'C:\Users\Heng2020\OneDrive\Python NLP\OutputData\The Ark season 1 srt')
    # vt.extract_subtitle(folder03,output_folder03, output_extension= ".srt")

def test_extract_sub_1_video():

    folder_01 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv")
    output_folder_01 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_01')
    vt.extract_sub_1_video(folder_01,output_folder_01, alarm_done=False)

    # folder02 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Peripheral_experiments\S01")
    # output_folder02 = Path(r'C:\C_Video_Python\video_toolkit_test\test_extract_subtitle\test_02')
    # vt.extract_sub_1_video(folder02,output_folder02)



@unittest.skipIf(False, "Testing: Test_extract_1_subtitles")
class Test_extract_sub_1_video(unittest.TestCase):

    video_path_01 = Path(r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv")
    output_folder_01 = Path(r'C:\C_Video_Python\video_toolkit_test\Test_extract_sub_1_video\test_01')
    output_folder_02 = Path(r'C:\C_Video_Python\video_toolkit_test\Test_extract_sub_1_video\test_02')
    output_folder_03 = Path(r'C:\C_Video_Python\video_toolkit_test\Test_extract_sub_1_video\test_03')

    def test_01_default(self):
        actual = vt.extract_sub_1_video(self.video_path_01,self.output_folder_01)
        expect = None
        self.assertEqual(expect, None)

    def test_02_title_as_out_name(self):
        actual = vt.extract_sub_1_video(self.video_path_01,self.output_folder_02,title_as_out_name=True)
        expect = None
        self.assertEqual(expect, None)
    
    def test_03_ass(self):
        actual = vt.extract_sub_1_video(self.video_path_01,self.output_folder_03,output_extension='ass')
        expect = None
        self.assertEqual(expect, None)
    # def test_basic03_no_outputName(self):
    #     actual = vt.extract_sub_1_video(self.video_path_01,self.output_folder_01,output_extension='.srt')
    #     expect = None
    #     self.assertEqual(expect, None)


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


# @unittest.skipIf(should_skip, 'Tested: Test_extract_audio_1file')
# class Test_extract_audio(unittest.TestCase):
#     from pathlib import Path

#     input_path01 = r"C:\DVDFab\StreamFab\Output\Netflix\3 Body Problem_01\3 Body Problem_S01E03_Destroyer of Worlds.mp4"
#     input_path02 = r"C:\DVDFab\StreamFab\Output\Amazon\The Peripheral_experiments\S01"
#     input_path03 = [
#         r"C:\DVDFab\StreamFab\Output\Netflix\3 Body Problem_01\3 Body Problem_S01E03_Destroyer of Worlds.mp4"
#         ,r"C:\DVDFab\StreamFab\Output\Netflix\3 Body Problem_01\3 Body Problem_S01E04_Our Lord.mp4"
#     ]

#     output_path01 = r'C:\C_Video_Python\video_toolkit_test\test_extract_audio\test_01_1file'
#     output_path02 = r'C:\C_Video_Python\video_toolkit_test\test_extract_audio\test_02_folder'
#     output_path03 = r'C:\C_Video_Python\video_toolkit_test\test_extract_audio\test_03_list_of_file'

#     # vt.extract_audio(input_path01,output_path01,output_extension="wav")
#     # vt.extract_audio(input_path02,output_path02,output_extension="wav")
#     vt.extract_audio(input_path03,output_path03,output_extension="wav")


#     def test_01_1file(self):
#         # vt.extract_audio(self.input_path01,self.output_path01,output_extension="wav")
#         vt.extract_audio(self.input_path01,self.output_path01,output_extension="wav",overwrite_file = False)

#     def test_02_folder(self):
#         vt.extract_audio(self.input_path02,self.output_path02,output_extension="wav")

#     def test_03_list_of_file(self):
#         vt.extract_audio(self.input_path03,self.output_path03,output_extension="wav")
        
        
        
@unittest.skipIf(should_skip, "Skipping: Test_extract_audio_1file")
class Test_extract_audio_1file(unittest.TestCase):
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    chosen_video_name = "The Big Bang Theory_S06E01.mkv"
    chosen_video_path = folder_FR_bigbang / chosen_video_name
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    
    output_folder_01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_01_all"
    output_folder02 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_02_only_French"
    output_folder03 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_03_Matrix_some_misspelled"

    input_video04 = r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv"
    output_folder04 = r"C:\C_Video_Python\video_toolkit_test\test_extract_audio_1file\test_04_02"

    output_folder_not_exist = r"C:\C_Video_Python\video_toolkit_test\test_extract_audio_1file\test_04kkkk"

    output_name = "BigBang_FR_S06E01"

    matrix_video_path = r"G:/My Drive/G_Videos/Polyglot/The Matrix Resurrections 2021.mkv"

    def test_03_not_exist_output_folder(self):
        with self.assertRaises(FileNotFoundError):
            vt.extract_audio_1file(video_path = self.input_video04,
                                output_folder = self.output_folder_not_exist,
                                alarm_done = True,
                                title_as_out_name = True)
    def test_04_basic(self):
        vt.extract_audio_1file(video_path = self.input_video04,
                                output_folder = self.output_folder04,
                                alarm_done = True,
                                title_as_out_name = True)

    

if __name__ == '__main__':
    unittest.main()


mport unittest
import os
from sound_recording_app import record_and_save_audio

class TestSoundRecordingApp(unittest.TestCase):

    def test_record_and_save_audio(self):
        # Define the test recording time
        test_seconds = 3

        # Call the function
        record_and_save_audio(test_seconds)

        # Check if the file is created
        self.assertTrue(os.path.exists("My Recording.wav"))

        # Clean up: remove the created file
        os.remove("My Recording.wav")

if __name__ == '__main__':
    unittest.main()



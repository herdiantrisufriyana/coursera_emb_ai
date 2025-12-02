# Import function to be tested and unittest
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Create the unit test class
class TestEmotionDetector(unittest.TestCase):
    # Define 5 unit tests
    def test_emotion_detector(self):
        # Test case for joy as dominant_emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Test case for anger as dominant_emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Test case for disgust as dominant_emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        # Test case for sadness as dominant_emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        # Test case for fear as dominant_emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

# Call the unit tests
unittest.main()
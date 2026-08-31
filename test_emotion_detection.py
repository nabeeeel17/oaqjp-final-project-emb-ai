from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionAnalyzer(unittest.TestCase):
    """Test cases for the emotion detector."""

    def test_joy(self):
        """Test joy emotion."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test anger emotion."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Test disgust emotion."""
        result = emotion_detector(
            'I feel disgusted just hearing about this'
        )
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Test sadness emotion."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Test fear emotion."""
        result = emotion_detector(
            'I am really afraid that this will happen'
        )
        self.assertEqual(result['dominant_emotion'], 'fear')


unittest.main()
import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        response = unittest.mock.Mock()
        response.status_code = 200
        response.json.side_effect = [
            {"emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.01, "fear": 0.01,
                "joy": 0.96, "sadness": 0.01}}]},
            {"emotionPredictions": [{"emotion": {
                "anger": 0.96, "disgust": 0.01, "fear": 0.01,
                "joy": 0.01, "sadness": 0.01}}]},
            {"emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.96, "fear": 0.01,
                "joy": 0.01, "sadness": 0.01}}]},
            {"emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.01, "fear": 0.01,
                "joy": 0.01, "sadness": 0.96}}]},
            {"emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.01, "fear": 0.96,
                "joy": 0.01, "sadness": 0.01}}]},
        ]
        mock_post.return_value = response

        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()

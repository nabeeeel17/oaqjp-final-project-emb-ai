'''Deploy the Emotion Detector web application.'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze the emotion of the provided text."""
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)

    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    response_str = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},
    'joy': {joy} and 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""

    return response_str


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
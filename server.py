"""
This module implements a Flask web application for emotion detection.
It provides a route to render the main page and a route to run
emotion analysis on user-provided text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main index page of the application."""
    return render_template('index.html')


@app.route("/emotionDetector")
def emot_detector():
    """
    Analyze the emotion of the text provided via query parameter
    and return a formatted string describing the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)
    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': "
        f"{result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
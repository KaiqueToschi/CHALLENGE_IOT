from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)['compound']
    if sentiment_score >= 0.5:
        return "Satisfeito (dificilmente o cliente cancelará ou não renovará o contrato novamente)"
    elif -0.5 < sentiment_score < 0.5:
        return "Neutro (existe a chance do cliente cancelar ou não renovar o contrato novamente)"
    else:
        return "Insatisfeito (provavelmente o cliente cancelará ou não renovará o contrato novamente)"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    message = data.get('message', '')
    sentiment = analyze_sentiment(message)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)

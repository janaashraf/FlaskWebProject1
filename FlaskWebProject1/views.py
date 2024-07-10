# from flask import Flask, request, jsonify
# from transformers import pipeline
# app = Flask(__name__)
# classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
#
# @app.route('/classify', methods=['POST'])
# def classify():
#     data = request.json
#     text = data['text']
#     labels = data['labels']
#     result = classifier(text, candidate_labels=labels)
#     return jsonify(result)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=62765)  # Specify the port here
from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

# Load the text classification pipeline
classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion',
                      return_all_scores=True)


# Define a route for classification endpoint
@app.route('/classify-journal', methods=['POST'])
def classify_text():
    # Get the JSON data from the request body
    data = request.json
    text = data['text']

    # Perform classification
    prediction = classifier(text)

    # Return JSON response with prediction
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True)


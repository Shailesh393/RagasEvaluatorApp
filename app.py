# app.py
from flask import Flask, request, jsonify, render_template
import os
from ragasEvaluator import load_document, evaluate_answer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        # Get input
        file = request.files['file']
        question = request.form['question']
        answer = request.form['answer']
        
        # Save and process file
        temp_path = 'temp_' + file.filename
        file.save(temp_path)
        
        # Evaluate
        doc = load_document(temp_path)
        document_content = ' '.join([page.page_content for page in doc])
        scores = evaluate_answer(question, answer, document_content)
        
        # Cleanup
        os.remove(temp_path)
        
        return jsonify(scores)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

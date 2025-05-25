# RAGAS Document Evaluation Tool

A web application that evaluates the faithfulness of answers to questions based on document content using RAGAS metrics.

## Features

- Upload PDF or TXT documents
- Automatic document chunking
- Question and answer input
- RAGAS-based faithfulness evaluation
- Clean and modern UI

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Upload a document (PDF or TXT) using the file upload interface
2. Wait for the document to be processed and chunked
3. Enter your question and the answer to evaluate
4. Click "Evaluate" to get the faithfulness score
5. Review the score and its interpretation

## Requirements

- Python 3.8 or higher
- Google Gemini API key
- Modern web browser

## Note

Make sure to keep your Google Gemini API key secure and never commit it to version control.

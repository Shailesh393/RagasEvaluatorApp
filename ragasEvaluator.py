# ragasEvaluator.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables
load_dotenv()

# Initialize models
gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def load_document(file_path):
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    return loader.load()

def get_similarity(text1, text2):
    emb1 = embeddings.embed_query(text1)
    emb2 = embeddings.embed_query(text2)
    return float(cosine_similarity([emb1], [emb2])[0][0])

def evaluate_answer(question, answer, document_content):
    # Calculate basic metrics
    answer_relevance = get_similarity(question, answer)
    context_relevance = get_similarity(answer, document_content)
    
    # Get faithfulness score
    prompt = f"""
    Question: {question}
    Answer: {answer}
    Context: {document_content}
    
    Rate how faithful the answer is to the context (0-1).
    Return only a number.
    """
    
    try:
        faithfulness = float(gemini.invoke(prompt).content.strip())
    except:
        faithfulness = 0.5
    
    # Calculate overall score
    overall = (answer_relevance + context_relevance + faithfulness) / 3
    
    return {
        'answer_relevance': answer_relevance,
        'context_relevance': context_relevance,
        'faithfulness': faithfulness,
        'overall_score': overall
    }

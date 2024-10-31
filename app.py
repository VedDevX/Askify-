# app.py
import os
import nltk
from flask import Flask, render_template, request, jsonify
from nltk import word_tokenize, pos_tag, ne_chunk, WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tree import Tree
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Download NLTK data
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Initialize Flask app and lemmatizer
app = Flask(__name__)
lemmatizer = WordNetLemmatizer()

def extract_named_entities(ne_tree):
    entities = []
    for subtree in ne_tree:
        if isinstance(subtree, Tree):
            entity = " ".join([word for word, _ in subtree.leaves()])
            entities.append((entity, subtree.label()))
    return entities

def analyze_sentence(sentence):
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags, binary=True)
    entities = extract_named_entities(named_entities)
    return tokens, pos_tags, entities

def generate_contextual_questions(paragraph, num_questions):
    sentences = sent_tokenize(paragraph)
    questions_with_answers = []
    for sentence in sentences:
        tokens, pos_tags, named_entities = analyze_sentence(sentence)
        prompt = f"Generate {num_questions} context-relevant questions based on the paragraph: '{paragraph}'."
        response = model.generate_content(prompt)
        
        if response and hasattr(response, '_result') and response._result.candidates:
            questions_text = response._result.candidates[0].content.parts[0].text.strip()
            questions = questions_text.split('\n')
            
            for question in questions:
                question = question.strip()
                if question:
                    answer = extract_full_answer(paragraph, question)
                    questions_with_answers.append((question, answer))
    return questions_with_answers

def extract_full_answer(paragraph, question):
    prompt = f"Answer the question '{question}' based on the paragraph: '{paragraph}'."
    response = model.generate_content(prompt)
    if response and hasattr(response, '_result') and response._result.candidates:
        return response._result.candidates[0].content.parts[0].text.strip()
    else:
        return "Could not generate an answer."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/terms-of-service")
def terms_of_service():
    return render_template("terms.html")

@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy_policy.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    paragraph = data.get("paragraph")
    num_questions = int(data.get("num_questions"))
    questions_with_answers = generate_contextual_questions(paragraph, num_questions)
    return jsonify({"questions": questions_with_answers})

if __name__ == "__main__":
    app.run(debug=True)

import os
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
# from dotenv import load_dotenv  # No longer needed
import google.generativeai as genai
from letter_analyzer import LetterAnalyzer
from file_processor import FileProcessor

# ---
# IMPORTANT: Set the Gemini API key as an environment variable before running the app.
# For example, in PowerShell:
#   $env:GOOGLE_API_KEY = "your_actual_api_key_here"
# Or in bash:
#   export GOOGLE_API_KEY=your_actual_api_key_here
# Or ensure it's set in your .env file and loaded by your environment.
# ---
import os

# Set your Gemini API key
os.environ["GEMINI_API_KEY"] = 'AIzaSyDDomIGM7rf41xk9Jsmx63rGMj85Uh3QKY'
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key')
app.config['MAX_CONTENT_LENGTH'] = int(os.environ.get('MAX_FILE_SIZE', 10485760))
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER', 'uploads')

# Configure Google Gemini using the environment variable directly
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

# Initialize components
letter_analyzer = LetterAnalyzer()
file_processor = FileProcessor()

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Extract text from file
            text_content = file_processor.extract_text(filepath)
            
            # Analyze the letter
            analysis_result = letter_analyzer.analyze_letter(text_content)
            
            # Send to n8n webhook if configured
            n8n_webhook_url = os.environ.get('N8N_WEBHOOK_URL')
            if n8n_webhook_url:
                try:
                    n8n_payload = {
                        'filename': filename,
                        'content': text_content,
                        'analysis': analysis_result,
                        'timestamp': str(datetime.now())
                    }
                    requests.post(n8n_webhook_url, json=n8n_payload, timeout=10)
                except Exception as e:
                    print(f"Failed to send to n8n webhook: {e}")
            
            return jsonify({
                'success': True,
                'filename': filename,
                'analysis': analysis_result
            })
            
        except Exception as e:
            return jsonify({'error': f'Analysis failed: {str(e)}'}), 500
        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        analysis_result = letter_analyzer.analyze_letter(data['text'])
        return jsonify({
            'success': True,
            'analysis': analysis_result
        })
    except Exception as e:
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'fake-letter-detection'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
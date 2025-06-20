# Fake Internship & Job Offer Letter Detection System

This project is an AI-powered web application for detecting fake internship and job offer letters using Google Gemini 1.5 Flash. It features a modern web interface, file and text analysis, and optional n8n workflow integration for automation and notifications.

---

## Features
- **AI-Powered Analysis**: Uses Gemini 1.5 Flash for deep letter authenticity checks
- **Multi-Format Support**: Analyze PDF, DOC, DOCX, and TXT files
- **Modern Web UI**: Drag-and-drop file upload and text input
- **n8n Integration**: Optional workflow automation and notifications
- **Security**: No files are stored after analysis; API keys are kept secure

---

## Setup

### 1. Clone the Repository
```bash
# Clone and enter the project directory
cd "fake offer letter"
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
You can set environment variables in your shell or add them at the top of `app.py` as shown below:

```python
import os
os.environ["GEMINI_API_KEY"] = 'your_actual_gemini_api_key_here'
```

**Required variables:**
- `GEMINI_API_KEY` (your Gemini 1.5 Flash API key)
- `FLASK_SECRET_KEY` (any random string for Flask sessions)
- `FLASK_ENV` (usually `development`)
- `N8N_WEBHOOK_URL` (optional, for n8n integration)
- `MAX_FILE_SIZE` (default: 10485760)
- `UPLOAD_FOLDER` (default: uploads)

You can also use a `.env` file if your environment loads it automatically.

---

## Usage

### 1. Start the Application
```bash
python app.py
```

### 2. Open the Web Interface
Go to [http://localhost:5000](http://localhost:5000) in your browser.

### 3. Analyze a Letter
- **Upload a file** (PDF, DOC, DOCX, TXT) or
- **Paste text** into the provided area
- View the AI-powered analysis, including authenticity score, risk level, red/green flags, and recommendations

---

## n8n Integration (Optional)
- Import `n8n_workflow.json` into your n8n instance
- Set the webhook URL in your environment as `N8N_WEBHOOK_URL`
- Configure Telegram, email, or database nodes as needed

---

## Security Notes
- Files are deleted after analysis
- API keys are never exposed in the UI
- No data is stored unless n8n integration is enabled

---

## License
MIT License

---

## Credits
- Powered by Google Gemini 1.5 Flash
- Built with Flask, Bootstrap, and n8n

---

For questions or support, please open an issue in this repository.

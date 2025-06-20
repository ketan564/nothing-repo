# Quick Start Guide

Get the Fake Letter Detection System up and running in 5 minutes!

## 🚀 Quick Setup

### 1. Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### 2. One-Command Setup
```bash
python setup.py
```

### 3. Configure API Key
Edit the `.env` file and add your Google Gemini API key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Test the System
```bash
python test_system.py
```

### 5. Start the Application
```bash
python app.py
```

### 6. Open in Browser
Navigate to: http://localhost:5000

## 🧪 Test with Sample Data

The system includes sample letters for testing:

- **Fake Letter**: `sample_data/fake_letter.txt`
- **Legitimate Letter**: `sample_data/legitimate_letter.txt`

## 📱 Using the Web Interface

1. **Upload a File**
   - Drag and drop or click to upload
   - Supports PDF, DOC, DOCX, TXT files

2. **Paste Text**
   - Switch to "Paste Text" tab
   - Copy and paste letter content
   - Click "Analyze Text"

3. **View Results**
   - Authenticity score (0-100)
   - Risk assessment
   - Red flags and green flags
   - Recommendations

## 🔧 n8n Integration (Optional)

1. **Install n8n**
   ```bash
   npm install n8n -g
   n8n start
   ```

2. **Import Workflow**
   - Open n8n at http://localhost:5678
   - Import `n8n_workflow.json`
   - Configure credentials

3. **Update Webhook URL**
   - Copy webhook URL from n8n
   - Update `N8N_WEBHOOK_URL` in `.env`

## 🐛 Troubleshooting

### Common Issues

**"API Key Error"**
- Verify your Google Gemini API key is correct
- Check API quota limits

**"Module not found"**
- Run: `pip install -r requirements.txt`
- Activate virtual environment first

**"Port already in use"**
- Change port in `app.py` or kill existing process
- Use: `python app.py --port 5001`

### Getting Help

1. Check the full [README.md](README.md)
2. Run the test script: `python test_system.py`
3. Check logs for error messages

## 🎯 What to Expect

### Fake Letter Detection
- Low authenticity score (0-40)
- High risk assessment
- Multiple red flags
- Suspicious content warnings

### Legitimate Letter Detection
- High authenticity score (70-100)
- Low risk assessment
- Green flags for professional content
- Positive indicators

## 🔒 Security Notes

- Files are automatically deleted after processing
- No data is stored permanently (unless n8n is configured)
- API keys are kept secure in environment variables

## 📞 Support

- Check the [README.md](README.md) for detailed documentation
- Review the troubleshooting section
- Test with sample data first

---

**Ready to detect fake letters? Start with `python setup.py`!** 
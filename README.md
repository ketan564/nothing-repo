# Fake Letter Detection System

A comprehensive AI-powered system for detecting fake internship and job offer letters using Google Gemini 1.5 Flash and n8n workflow automation.

## 🚀 Features

- **AI-Powered Analysis**: Uses Google Gemini 1.5 Flash for intelligent letter analysis
- **Multi-Format Support**: Handles PDF, DOC, DOCX, and TXT files
- **Web Interface**: Modern, responsive web UI for easy interaction
- **n8n Integration**: Automated workflow with notifications and data storage
- **Real-time Alerts**: Telegram and email notifications for high-risk letters
- **Comprehensive Analysis**: Detailed red flags, green flags, and recommendations

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Interface │    │   Flask Backend │    │  Gemini 1.5 AI  │
│   (HTML/CSS/JS) │◄──►│   (Python)      │◄──►│   (Analysis)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   n8n Workflow  │
                       │   (Automation)  │
                       └─────────────────┘
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
        ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
        │   Telegram  │ │    Email    │ │  Database   │
        │  Notifications│ │  Alerts     │ │  Storage    │
        └─────────────┘ └─────────────┘ └─────────────┘
```

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key
- n8n instance (optional)
- Telegram Bot Token (optional)
- Email service credentials (optional)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fake-offer-letter-detection
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env_example.txt .env
   # Edit .env file with your API keys and configuration
   ```

5. **Configure API keys**
   - Get Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set up Telegram bot (optional) - [BotFather](https://t.me/botfather)
   - Configure email service (optional)

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Google Gemini API Configuration
GOOGLE_API_KEY=your_gemini_api_key_here

# Flask Configuration
FLASK_SECRET_KEY=your_secret_key_here
FLASK_ENV=development

# n8n Configuration
N8N_WEBHOOK_URL=http://localhost:5678/webhook/fake-letter-detection

# File Upload Configuration
MAX_FILE_SIZE=10485760  # 10MB
UPLOAD_FOLDER=uploads
```

### n8n Workflow Setup

1. **Import the workflow**
   - Open n8n interface
   - Import `n8n_workflow.json`
   - Configure credentials for Telegram, Email, and Database nodes

2. **Configure webhook URL**
   - Copy the webhook URL from n8n
   - Update `N8N_WEBHOOK_URL` in your `.env` file

3. **Set up credentials**
   - Telegram Bot Token
   - Email service credentials
   - Database connection (Firestore/PostgreSQL)

## 🚀 Usage

### Starting the Application

```bash
python app.py
```

The web interface will be available at `http://localhost:5000`

### Using the Web Interface

1. **File Upload**
   - Drag and drop or click to upload letter files
   - Supported formats: PDF, DOC, DOCX, TXT
   - Maximum file size: 10MB

2. **Text Analysis**
   - Paste letter text directly into the text area
   - Click "Analyze Text" for instant analysis

3. **View Results**
   - Authenticity score (0-100)
   - Risk assessment (Low/Medium/High)
   - Detailed red flags and green flags
   - Specific recommendations

### API Endpoints

- `GET /` - Web interface
- `POST /upload` - File upload and analysis
- `POST /analyze-text` - Text analysis
- `GET /api/health` - Health check

## 🔍 Analysis Features

### What the AI Analyzes

1. **Company Information**
   - Company name consistency
   - Address verification
   - Contact information validation

2. **Language and Writing Style**
   - Grammar and spelling
   - Professional tone
   - Formatting consistency

3. **Content Red Flags**
   - Suspicious salary offers
   - Unusual job requirements
   - Payment requests
   - Urgency tactics

4. **Contact Information**
   - Email domain verification
   - Phone number validation
   - Address authenticity

5. **Document Formatting**
   - Professional letterhead
   - Signature verification
   - Layout consistency

### Analysis Output

```json
{
  "authenticity_score": 75,
  "confidence_level": "high",
  "letter_type": "job_offer",
  "red_flags": [
    {
      "category": "contact",
      "description": "Uses free email service for company communication",
      "severity": "medium"
    }
  ],
  "green_flags": [
    {
      "category": "company_info",
      "description": "Company has legitimate online presence",
      "severity": "high"
    }
  ],
  "recommendations": [
    "Verify company contact information independently",
    "Check company website for job posting"
  ],
  "summary": "Letter appears mostly legitimate with minor concerns",
  "risk_assessment": "medium"
}
```

## 🔧 n8n Workflow Features

### Automated Actions

1. **High-Risk Alerts**
   - Email notifications for high-risk letters
   - Telegram alerts with detailed information
   - Immediate escalation for suspicious content

2. **Data Storage**
   - Automatic storage of all analyses
   - Historical tracking and reporting
   - Audit trail for compliance

3. **Integration Options**
   - Slack notifications
   - CRM integration
   - Custom webhook endpoints

## 📊 Sample Test Data

### Fake Letter Example
```
Dear Candidate,

Congratulations! You have been selected for a prestigious internship position at TechCorp International.

Position: Senior Software Engineer Intern
Salary: $15,000 per month
Duration: 3 months

Please send your personal information including:
- Bank account details
- Social Security Number
- Passport copy
- $500 processing fee

Reply urgently to: hr.techcorp@gmail.com

Best regards,
HR Department
TechCorp International
```

### Legitimate Letter Example
```
Dear [Candidate Name],

We are pleased to offer you the position of Software Engineering Intern at Google LLC.

Position: Software Engineering Intern
Location: Mountain View, CA
Duration: 12 weeks (Summer 2024)
Compensation: $8,000/month + benefits

Please review the attached offer letter and respond within 5 business days.

For questions, contact: recruiting@google.com

Best regards,
Google Recruiting Team
Google LLC
1600 Amphitheatre Parkway
Mountain View, CA 94043
```

## 🛡️ Security Features

- File type validation
- File size limits
- Secure file handling
- API key protection
- Input sanitization
- Rate limiting (configurable)

## 🔄 Workflow Automation

The n8n workflow provides:

1. **Real-time Processing**
   - Instant analysis results
   - Automated notifications
   - Data persistence

2. **Risk-based Actions**
   - High-risk letter escalation
   - Standard notification for all letters
   - Custom alert thresholds

3. **Integration Capabilities**
   - Multiple notification channels
   - Database storage
   - Custom webhook endpoints

## 📈 Performance Optimization

- Async file processing
- Caching for repeated analyses
- Efficient text extraction
- Optimized AI prompts

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify Google Gemini API key is valid
   - Check API quota and limits

2. **File Upload Issues**
   - Ensure file format is supported
   - Check file size limits
   - Verify file permissions

3. **n8n Integration**
   - Confirm webhook URL is correct
   - Check n8n instance is running
   - Verify credentials are configured

### Debug Mode

Enable debug logging by setting:
```env
FLASK_ENV=development
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the documentation

## 🔮 Future Enhancements

- Machine learning model training
- OCR for image-based letters
- Multi-language support
- Advanced fraud detection patterns
- Integration with HR systems
- Real-time company verification
- Blockchain-based verification
- Mobile application

---

**Note**: This system is designed to assist in letter verification but should not be the sole basis for decision-making. Always verify important information through official channels. 
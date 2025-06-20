#!/usr/bin/env python3
"""
Setup script for Fake Letter Detection System
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['uploads', 'logs', 'sample_data']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def setup_virtual_environment():
    """Set up virtual environment"""
    if not os.path.exists('venv'):
        print("🔄 Creating virtual environment...")
        if not run_command('python -m venv venv', 'Creating virtual environment'):
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Activate virtual environment and install dependencies
    if os.name == 'nt':  # Windows
        activate_cmd = 'venv\\Scripts\\activate'
        pip_cmd = 'venv\\Scripts\\pip'
    else:  # Unix/Linux/macOS
        activate_cmd = 'source venv/bin/activate'
        pip_cmd = 'venv/bin/pip'
    
    print("🔄 Installing dependencies...")
    if not run_command(f'{pip_cmd} install -r requirements.txt', 'Installing dependencies'):
        return False
    
    return True

def create_env_file():
    """Create .env file from template"""
    if not os.path.exists('.env'):
        if os.path.exists('env_example.txt'):
            shutil.copy('env_example.txt', '.env')
            print("✅ Created .env file from template")
            print("⚠️  Please edit .env file with your API keys")
        else:
            print("❌ env_example.txt not found")
            return False
    else:
        print("✅ .env file already exists")
    return True

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'flask', 'google-generativeai', 'python-dotenv', 'requests',
        'PyPDF2', 'python-docx', 'Pillow'
    ]
    
    print("🔄 Checking dependencies...")
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - not installed")
            return False
    return True

def create_sample_files():
    """Create sample test files"""
    sample_dir = Path('sample_data')
    sample_dir.mkdir(exist_ok=True)
    
    # Create sample fake letter
    fake_letter_content = """Dear Candidate,

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
TechCorp International"""
    
    with open(sample_dir / 'fake_letter.txt', 'w') as f:
        f.write(fake_letter_content)
    
    # Create sample legitimate letter
    legitimate_letter_content = """Dear [Candidate Name],

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
Mountain View, CA 94043"""
    
    with open(sample_dir / 'legitimate_letter.txt', 'w') as f:
        f.write(legitimate_letter_content)
    
    print("✅ Created sample test files")

def main():
    """Main setup function"""
    print("🚀 Setting up Fake Letter Detection System")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Set up virtual environment
    if not setup_virtual_environment():
        print("❌ Failed to set up virtual environment")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("❌ Failed to create .env file")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Some dependencies are missing")
        print("🔄 Try running: pip install -r requirements.txt")
        sys.exit(1)
    
    # Create sample files
    create_sample_files()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your Google Gemini API key")
    print("2. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("3. Run the application:")
    print("   python app.py")
    print("4. Open http://localhost:5000 in your browser")
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main() 
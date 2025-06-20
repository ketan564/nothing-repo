#!/usr/bin/env python3
"""
Test script for Fake Letter Detection System
"""

import os
import sys
from dotenv import load_dotenv
from letter_analyzer import LetterAnalyzer
from file_processor import FileProcessor

def test_letter_analyzer():
    """Test the letter analyzer with sample data"""
    print("🧪 Testing Letter Analyzer...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ GOOGLE_API_KEY not found in environment variables")
        print("Please set your Google Gemini API key in the .env file")
        return False
    
    try:
        # Initialize analyzer
        analyzer = LetterAnalyzer()
        print("✅ Letter analyzer initialized successfully")
        
        # Test with fake letter
        fake_letter = """
        Dear Candidate,
        
        CONGRATULATIONS! You have been selected for an EXCLUSIVE internship opportunity!
        
        Position: Senior Software Engineer Intern
        Salary: $25,000 per month
        Duration: 6 months
        
        Please send your personal information including:
        - Bank account details
        - Social Security Number
        - $750 processing fee
        
        Reply urgently to: hr.techcorp@gmail.com
        
        Best regards,
        HR Department
        TechCorp International
        """
        
        print("🔄 Analyzing fake letter...")
        fake_result = analyzer.analyze_letter(fake_letter)
        
        print(f"📊 Fake Letter Analysis:")
        print(f"   Authenticity Score: {fake_result.get('authenticity_score', 'N/A')}")
        print(f"   Risk Level: {fake_result.get('risk_assessment', 'N/A')}")
        print(f"   Confidence: {fake_result.get('confidence_level', 'N/A')}")
        print(f"   Summary: {fake_result.get('summary', 'N/A')}")
        
        # Test with legitimate letter
        legitimate_letter = """
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
        """
        
        print("\n🔄 Analyzing legitimate letter...")
        legitimate_result = analyzer.analyze_letter(legitimate_letter)
        
        print(f"📊 Legitimate Letter Analysis:")
        print(f"   Authenticity Score: {legitimate_result.get('authenticity_score', 'N/A')}")
        print(f"   Risk Level: {legitimate_result.get('risk_assessment', 'N/A')}")
        print(f"   Confidence: {legitimate_result.get('confidence_level', 'N/A')}")
        print(f"   Summary: {legitimate_result.get('summary', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing letter analyzer: {e}")
        return False

def test_file_processor():
    """Test the file processor"""
    print("\n🧪 Testing File Processor...")
    
    try:
        processor = FileProcessor()
        print("✅ File processor initialized successfully")
        
        # Test with sample text file
        sample_content = "This is a test letter content."
        test_file_path = "test_letter.txt"
        
        with open(test_file_path, 'w') as f:
            f.write(sample_content)
        
        # Test text extraction
        extracted_text = processor.extract_text(test_file_path)
        print(f"✅ Text extraction successful: {len(extracted_text)} characters")
        
        # Test file info
        file_info = processor.get_file_info(test_file_path)
        print(f"✅ File info retrieved: {file_info['filename']}")
        
        # Clean up
        os.remove(test_file_path)
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing file processor: {e}")
        return False

def test_sample_files():
    """Test with sample files in sample_data directory"""
    print("\n🧪 Testing with sample files...")
    
    sample_dir = "sample_data"
    if not os.path.exists(sample_dir):
        print(f"❌ Sample data directory not found: {sample_dir}")
        return False
    
    try:
        processor = FileProcessor()
        analyzer = LetterAnalyzer()
        
        # Test fake letter
        fake_file = os.path.join(sample_dir, "fake_letter.txt")
        if os.path.exists(fake_file):
            print("🔄 Testing fake letter file...")
            content = processor.extract_text(fake_file)
            result = analyzer.analyze_letter(content)
            print(f"   Score: {result.get('authenticity_score', 'N/A')}")
            print(f"   Risk: {result.get('risk_assessment', 'N/A')}")
        
        # Test legitimate letter
        legitimate_file = os.path.join(sample_dir, "legitimate_letter.txt")
        if os.path.exists(legitimate_file):
            print("🔄 Testing legitimate letter file...")
            content = processor.extract_text(legitimate_file)
            result = analyzer.analyze_letter(content)
            print(f"   Score: {result.get('authenticity_score', 'N/A')}")
            print(f"   Risk: {result.get('risk_assessment', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing sample files: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Fake Letter Detection System")
    print("=" * 50)
    
    # Test letter analyzer
    if not test_letter_analyzer():
        print("❌ Letter analyzer test failed")
        sys.exit(1)
    
    # Test file processor
    if not test_file_processor():
        print("❌ File processor test failed")
        sys.exit(1)
    
    # Test sample files
    if not test_sample_files():
        print("❌ Sample files test failed")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed successfully!")
    print("\n✅ System is ready to use!")
    print("Run 'python app.py' to start the web interface")

if __name__ == "__main__":
    main() 
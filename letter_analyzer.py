import google.generativeai as genai
import json
import re
from typing import Dict, List, Any
import os

class LetterAnalyzer:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.analysis_prompt = self._get_analysis_prompt()
        
    def _get_analysis_prompt(self) -> str:
        return """
        You are an expert in detecting fake internship and job offer letters. Analyze the following letter and provide a comprehensive assessment.

        Please analyze the letter for the following indicators of authenticity:

        1. **Company Information Analysis:**
           - Check if the company name, address, and contact information are consistent
           - Verify if the company exists and has a legitimate online presence
           - Look for suspicious or generic company names

        2. **Language and Writing Style:**
           - Identify overly formal or generic language
           - Look for grammatical errors or inconsistencies
           - Check for unusual formatting or structure

        3. **Content Red Flags:**
           - Suspicious salary offers (too high or too low)
           - Unusual job requirements or responsibilities
           - Requests for personal information or payments
           - Urgency or pressure tactics
           - Generic job descriptions

        4. **Contact Information:**
           - Verify email domains match company domains
           - Check for free email services (Gmail, Yahoo, etc.) from company representatives
           - Look for suspicious phone numbers or addresses

        5. **Document Formatting:**
           - Check for professional letterhead and formatting
           - Look for inconsistencies in fonts, spacing, or layout
           - Verify signature authenticity

        Provide your analysis in the following JSON format:
        {
            "authenticity_score": 0-100,
            "confidence_level": "low/medium/high",
            "letter_type": "internship/job_offer/other",
            "red_flags": [
                {
                    "category": "company_info/language/content/contact/formatting",
                    "description": "Description of the issue",
                    "severity": "low/medium/high"
                }
            ],
            "green_flags": [
                {
                    "category": "company_info/language/content/contact/formatting",
                    "description": "Description of positive indicator",
                    "severity": "low/medium/high"
                }
            ],
            "recommendations": [
                "List of recommendations for verification"
            ],
            "summary": "Brief summary of findings",
            "risk_assessment": "low/medium/high"
        }

        Letter to analyze:
        """

    def analyze_letter(self, letter_text: str) -> Dict[str, Any]:
        """
        Analyze a letter for authenticity using Gemini 1.5 Flash
        """
        try:
            # Prepare the prompt with the letter text
            full_prompt = self.analysis_prompt + letter_text
            
            # Generate response from Gemini
            response = self.model.generate_content(full_prompt)
            
            # Extract JSON from response
            analysis_text = response.text
            
            # Try to extract JSON from the response
            json_match = re.search(r'\{.*\}', analysis_text, re.DOTALL)
            if json_match:
                analysis_json = json.loads(json_match.group())
            else:
                # Fallback: create a basic analysis structure
                analysis_json = self._create_fallback_analysis(letter_text, analysis_text)
            
            # Add metadata
            analysis_json['metadata'] = {
                'model_used': 'gemini-1.5-flash',
                'analysis_timestamp': str(datetime.now()),
                'text_length': len(letter_text)
            }
            
            return analysis_json
            
        except Exception as e:
            return self._create_error_analysis(str(e))
    
    def _create_fallback_analysis(self, letter_text: str, raw_response: str) -> Dict[str, Any]:
        """Create a fallback analysis when JSON parsing fails"""
        return {
            "authenticity_score": 50,
            "confidence_level": "low",
            "letter_type": "unknown",
            "red_flags": [
                {
                    "category": "analysis",
                    "description": "Unable to parse AI response properly",
                    "severity": "medium"
                }
            ],
            "green_flags": [],
            "recommendations": [
                "Manual review recommended",
                "Verify all company information independently"
            ],
            "summary": "Analysis incomplete due to parsing error",
            "risk_assessment": "medium",
            "raw_response": raw_response
        }
    
    def _create_error_analysis(self, error_message: str) -> Dict[str, Any]:
        """Create an error analysis when the AI call fails"""
        return {
            "authenticity_score": 0,
            "confidence_level": "low",
            "letter_type": "unknown",
            "red_flags": [
                {
                    "category": "system_error",
                    "description": f"Analysis failed: {error_message}",
                    "severity": "high"
                }
            ],
            "green_flags": [],
            "recommendations": [
                "System error occurred during analysis",
                "Please try again or contact support"
            ],
            "summary": "Analysis failed due to system error",
            "risk_assessment": "high",
            "error": error_message
        }
    
    def extract_company_info(self, letter_text: str) -> Dict[str, str]:
        """Extract company information from the letter"""
        company_info = {
            'name': '',
            'address': '',
            'email': '',
            'phone': '',
            'website': ''
        }
        
        # Extract company name (usually in header or signature)
        company_patterns = [
            r'(?:from|at|with)\s+([A-Z][A-Za-z\s&.,]+(?:Inc|LLC|Corp|Company|Ltd))',
            r'([A-Z][A-Za-z\s&.,]+(?:Inc|LLC|Corp|Company|Ltd))',
        ]
        
        for pattern in company_patterns:
            match = re.search(pattern, letter_text, re.IGNORECASE)
            if match:
                company_info['name'] = match.group(1).strip()
                break
        
        # Extract email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, letter_text)
        if emails:
            company_info['email'] = emails[0]
        
        # Extract phone numbers
        phone_pattern = r'(\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4})'
        phones = re.findall(phone_pattern, letter_text)
        if phones:
            company_info['phone'] = phones[0]
        
        return company_info
    
    def get_risk_level(self, authenticity_score: int) -> str:
        """Convert authenticity score to risk level"""
        if authenticity_score >= 80:
            return "low"
        elif authenticity_score >= 60:
            return "medium"
        else:
            return "high"

# Import datetime for timestamp
from datetime import datetime 
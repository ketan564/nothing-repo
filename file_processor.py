import PyPDF2
import docx
import os
from typing import Optional

class FileProcessor:
    def __init__(self):
        self.supported_formats = {'.pdf', '.doc', '.docx', '.txt'}
    
    def extract_text(self, file_path: str) -> str:
        """
        Extract text from various file formats
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {file_extension}")
        
        try:
            if file_extension == '.pdf':
                return self._extract_from_pdf(file_path)
            elif file_extension == '.docx':
                return self._extract_from_docx(file_path)
            elif file_extension == '.doc':
                return self._extract_from_doc(file_path)
            elif file_extension == '.txt':
                return self._extract_from_txt(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
        except Exception as e:
            raise Exception(f"Error extracting text from {file_path}: {str(e)}")
    
    def _extract_from_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                
                return text.strip()
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")
    
    def _extract_from_docx(self, file_path: str) -> str:
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(file_path)
            text = ""
            
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            return text.strip()
        except Exception as e:
            raise Exception(f"Error reading DOCX file: {str(e)}")
    
    def _extract_from_doc(self, file_path: str) -> str:
        """Extract text from DOC file (basic implementation)"""
        # Note: This is a basic implementation. For better DOC support,
        # you might want to use additional libraries like python-docx2txt
        try:
            # Try to read as text file first
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                if content.strip():
                    return content.strip()
            
            # If that fails, try with different encoding
            with open(file_path, 'r', encoding='latin-1', errors='ignore') as file:
                return file.read().strip()
        except Exception as e:
            raise Exception(f"Error reading DOC file: {str(e)}")
    
    def _extract_from_txt(self, file_path: str) -> str:
        """Extract text from TXT file"""
        try:
            # Try UTF-8 first
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except UnicodeDecodeError:
            # Fallback to other encodings
            encodings = ['latin-1', 'cp1252', 'iso-8859-1']
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        return file.read().strip()
                except UnicodeDecodeError:
                    continue
            
            raise Exception("Unable to decode text file with any supported encoding")
        except Exception as e:
            raise Exception(f"Error reading TXT file: {str(e)}")
    
    def get_file_info(self, file_path: str) -> dict:
        """Get basic information about the file"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_stats = os.stat(file_path)
        
        return {
            'filename': os.path.basename(file_path),
            'file_size': file_stats.st_size,
            'file_extension': os.path.splitext(file_path)[1].lower(),
            'is_supported': os.path.splitext(file_path)[1].lower() in self.supported_formats
        }
    
    def validate_file(self, file_path: str) -> bool:
        """Validate if the file can be processed"""
        try:
            file_info = self.get_file_info(file_path)
            return file_info['is_supported']
        except Exception:
            return False 
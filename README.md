# NLP Text Processing Console Application

A Python-based console application that demonstrates practical Natural Language Processing (NLP) techniques. This interactive tool allows users to input text and receive both Named Entity Recognition (NER) analysis and AI-generated summaries.

## 🚀 Features

- **Interactive Console Interface:** Simple text-based interface for easy text input and processing
- **Named Entity Recognition:** Identifies and categorizes people, organizations, and locations in text using spaCy
- **Text Summarization:** Generates concise summaries of input text using Hugging Face transformers
- **Real-time Processing:** Immediate results for quick analysis and experimentation

## 🛠️ Tech Stack

- **Python 3.8+**
- **spaCy** with `en_core_web_md` for entity recognition
- **Hugging Face Transformers** with `facebook/bart-large-cnn` for summarization
- **PyTorch** as the machine learning backend

## 💡 How It Works

1. Run the application: `python nlp_console.py`
2. Enter your text when prompted
3. View the processed results:
   - Extracted entities (people, organizations, locations)
   - AI-generated summary
4. Repeat with new text or exit

### Example Session:
Enter your text: Satya Nadella, CEO of Microsoft, announced a new partnership with OpenAI during an event in San Francisco. The collaboration focuses on advancing AI research and development.

--- Named Entity Recognition Results ---
PERSONS: 'Satya Nadella'
ORGANIZATIONS: 'Microsoft', 'OpenAI'
LOCATIONS: 'San Francisco'

--- Text Summary ---
Microsoft CEO Satya Nadella announced a partnership with OpenAI at a San Francisco event, focusing on AI research and development.


## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Auction-s/Search.git
   cd Search
   python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_md
python nlp_console.py

📚 What I Learned
Building this application provided hands-on experience with:
Integrating multiple NLP libraries (spaCy + Hugging Face) in a single pipeline
Processing user input and handling different text formats
Working with transformer models for text generation tasks
Structuring console applications for better user experience
Managing model dependencies and deployment requirements

🚀 Future Enhancements
Add support for file input (process text documents)
Implement batch processing for multiple texts
Expand to support multiple languages
Add sentiment analysis capability
Create a web interface using Streamlit
Optimize model loading for faster startup


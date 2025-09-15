# Search (NLP Console Project)

This project is a simple **Python console application** that demonstrates the use of **Natural Language Processing (NLP)** to process and search text.  
It is part of my **Week 1 Google Project series**, focusing on building small, functional prototypes.
- Name Entity Recognition (NER) with **spaCy**
- Text summarization with **Hugging Face Transformers**
- Question Answering (QA) with **Hugging Face Transformers**
  
-----

## Features
- Accepts user inputs from the console
- Process text using basic NLP techniques
- Provide search functionlaity ove sample data
- Easy to extend and customize

-----
 Clone:
```bash
git clone https://github.com/Auction-s/Search.git
cd Search

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install spacy transformers torch
python -m spacy download en_core_web_sm
python nlp_console.py

Final tips & quick checks

If you get ModuleNotFoundError for transformers or spacy, install them with pip install transformers spacy torch.

If the summarizer model download is slow, you can swap to a smaller summarizer or test QA/NER first. The sshleifer/distilbart-cnn-6-6 you used is a good smaller model.

Add sample text files under examples/ later to show demo inputs/outputs.

Tech Stack

Python 3.8+ – Programming language

spaCy – For Named Entity Recognition (NER)

Hugging Face Transformers – For summarization and question answering

Pip / Virtualenv – For dependency management

Console (CLI) – Simple interface for user interaction

Lessons Learned

Gained hands-on experience with spaCy and Hugging Face libraries.

Learned how to build a text-processing pipeline (NER → Summarization → QA).

Practiced structuring a console application instead of hardcoding text.

Improved understanding of how to document and publish a project on GitHub.

Future Improvements

Add a GUI interface (e.g., Tkinter or Streamlit) for better usability.

Expand to support multiple languages (not just English).

Integrate with a search API (e.g., Google Custom Search or Wikipedia) for real-time text sources.

Optimize summarization with faster models or on-device deployment.

Containerize the project with Docker for easier setup.

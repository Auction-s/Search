# ============ nlp_console.py =============
import spacy
from transformers import pipeline
print('spacy imported successfully')
print('pipleline imported successfully')

# =========== Load spacy ==================
print('Loading spacy')
nlp = spacy.load('en_core_web_sm')
print('spacy successfully loaded')

# =========== Load Hugging face =============
print('Loading Huggin face')
summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-6-6')  # Smaller version
qa = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')  # Smaller & faster to download
print('Hugging face successfully loaded')

# =========== Example ==================
text = """
          Google was founded by Larry Page and Sergay Brian wile they were Ph.D students st Stanford University.
          Since then it has grown into a global technology leader in search,, advertising, cloud computing and AI reserch. 
          """
          
# =========== Check ==================== 
print('\n--- Named Entities ------')
doc = nlp(text)
for ent in doc.ents:
    print(f'{ent.text} ({ent.label_})')
    
print('\n Summary')
summary = summarizer(text, max_length=60, min_length=25, do_sample=False)[0]['summary_text']
print(summary)

print('\n--- Q&A ----')
question = 'When was Google founded'
answer = qa(question = question, context=text)
print(f'Q: {question}')
print(f'A: {answer['answer']}')    
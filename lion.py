from docx import Document as dc
import string, nltk
from nltk.probability import FreqDist

doc = dc('lion.docx')
text = []
spec_chars = string.punctuation + '\n\xa0«»\t—…,.—' 

for docparagraph in doc.paragraphs:
    text.append(docparagraph.text)

tt = ''.join(text)

tt = tt.lower
tt = "".join([ch for ch in text if ch not in spec_chars])# Делаем всебуквы маленькими и избовляемся от символов

from nltk import word_tokenize
text_tokens = word_tokenize(tt)

tt = nltk.Text(text_tokens)
fdist = FreqDist(tt)

print(fdist.most_common(30))

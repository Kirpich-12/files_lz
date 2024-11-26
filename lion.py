from collections import Counter as ct
from docx import Document as dc
from string import punctuation as pcc

doc = dc('lion.docx')
text_f = []
text_s = []
text_p = []

pc = pcc + '—'

for docparagraph in doc.paragraphs:
    text_s.append(docparagraph.text)

text_s = ''.join(text_s)
text_s = text_s.lower()

for i in text_s:
    if i not in pc:
        text_p.append(i)
    else:
        text_p.append(' ')
text_p = ''.join(text_p)

text_f = text_p.split()

ans = ct(text_f)

for i, j in ans.items():

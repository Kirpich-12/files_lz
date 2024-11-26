from collections import Counter as ct
from docx import Document as dc
from string import punctuation as pcc
import matplotlib.pyplot as plt

doc = dc('lion.docx')# Создание переменной с файлом
text_f = []# финальная версия набора слов из документа
text_s = []#Изначальная версия
text_p = []#Промежуточная версия 

'''Частотный список'''

pc = pcc + '—'#создание строки с неугодными знаками припенания 

for docparagraph in doc.paragraphs:#файл  в список
    text_s.append(docparagraph.text)

text_s = ''.join(text_s)#список в строку
text_s = text_s.lower()#твсе слова с маленькой буквы для правильного подсчёта 

for i in text_s:
    if i not in pc:
        text_p.append(i)# фильруем на неуодные знаки припенания 
    else:
        text_p.append(' ')#вместо них пробелы

text_p = ''.join(text_p)# в строку 

text_f = text_p.split()#Делим по пробелу(для избежания ошибок в определении слов)

text_len = len(text_f)#Кол-во всех слов

ish = ct(text_f)

'''Представление в виде таблицы'''


out = dc()
out_t = out.add_table(rows = 1, cols = 3)

for nas, zn in ish.items():
    prc = (zn / text_len) * 100 #процент 
    rad = out_t.add_row() # 
    rad.cells[0].text = nas # ряд названий
    rad.cells[1].text = str(zn) # ряд значений
    rad.cells[2].text = str(prc) + '%' # ряд проц. соотношения 

out.save('out.docx')



'''График'''

let = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц','ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
ish_let = {}

str_f = ''.join(text_f)
ish_f = ct(str_f)

for i, j in ish_f.items():
    if i in let:
        ish_let[i] = j

sort_let = sorted(ish_let.keys())
plot_v = [ish_let[letter] for letter in sort_let]

#создание графика
plt.figure(figsize=(12, 6))
plt.bar(sort_let, plot_v, color='coral')
plt.xlabel('Буквы')
plt.ylabel('Количество')
plt.title('График частоты встречи букв')
plt.grid(axis='y')

# Отображаем график
plt.tight_layout()
plt.show()

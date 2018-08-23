'''Spell-check при помощи исчисления и распределения триграм.'''

file = open("file1.py")
text = file.read()
file.close()


import re
from collections import Counter, namedtuple


# Очищает текст от знаков препинания и сплитит его весь.

def text_to_wordlist(sentence):
    regexp = "[^а-яА-ЯёЁ]|" # любая не-буква
    sentence = re.sub(regexp, " ", sentence)
    result = sentence.lower().split()
    return result
    
# Найдем все уникальные триграммы для слова. 

# Сохраним в специальном кортеже все базовые данные о триграммах в слове. Такой кортеж нужен, чтобы на выходе функции было несколько данных, к которым можно было бы обращаться потом (см. строку 50)

def get_trigrams(word):
	'''Return a namedtuple of 
	1 - all trigrams (with blanks)
	2 - all unique trigrams'''  
	word = '##' + word.lower() + '##'
	trigrams = []
	for i in range(len(word)-3):
		trigrams.append(word[i:i+3])
	unique = sorted(set(trigrams), key = trigrams.index) # Сортируем новый лист по старому
	TrigramData = namedtuple("TrigramData", ['trigrams','unique'])
	return TrigramData(trigrams, unique)

# Найдем все триграммы, представленные во всех словах в тексте. 
# Сделаем частотный словарь этих триграм (объект Counter).

def all_trigrams(text):
	'''Get all trigrams from text'''
	tokens = [ "##" + word + "##" for word in text_to_wordlist(text)]
	counter = Counter() # Подтип словаря: целочисленный ассоциативный массив
	for token in tokens:
		for i in range(len(token)-3):
			counter[token[i:i+3]] += 1 # Добавляет в словарь триграмму и обновляет её счётчик
	return counter	
	
counter = dict(all_trigrams(text)) 
s = sum(counter.values())
counter = {key:float(value)/s for key, value in counter.items()}  # Вер-ть триграммы, доли

# Осуществим спелл-чекинг. Узнаем, правильно ли написано введенное слово.

def indict(word, threshold): # threshold - порог стат.значимости.
	'''Figure out whether a word is spelled correctly. 
	Wrong spelling is when a trigram is less likely to occur than a threshold value.'''
	trigrams = get_trigrams(word).unique # словарь триграм (= уникальные триграмы)
	for trig in trigrams:
		if trig not in counter:
			return False
		if counter[trig] < threshold:
			return False
	return True

print(indict(input(), 0.0000001))






	


	

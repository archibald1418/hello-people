# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:13:05 2018

@author: oleg

ИЗМЕНЕНО:

1 - добавлен в транскрипцию кружочек лабиализация 
2 - добавлено удаление диакритических знаков-ударений над гласными 

"""

import re

HEM = re.compile(r"(([iaeuptšsčcхkχ])ː)", re.I)  
FAR = re.compile(r'(((?<=[^aouei]|\w)[iua])ˁ)', re.I)
ABR = re.compile(r"(([qkpčtc])[’'])", re.I)

J_VJ = re.compile(r'j[ua]', re.I)  # контексты, где ja -> я
E = re.compile(r'\be|e(?=[aouei])', re.I)  # контексты, где e -> э

# Убрать диакритику
VOWELS = ('a', 'e', 'i', 'o', 'u')
STRESSED_VOWELS = ['á'] + list(chr(ord(v) + 132) for v in VOWELS[1:])
DIACRITICS = dict(zip(STRESSED_VOWELS, VOWELS))


drg_cyr = {'a': 'а',
           'aˁ': 'я',
           'b': 'б',
           'c': 'ц',
           'd': 'д',
           'e': 'е',  # В начале слова и перед гласной это будет э
           'f': 'ф',
           'g': 'г',
           'i': 'и',
           'j': 'й',  # Йоты сделать
           'k': 'к',
           'l': 'л',
           'm': 'м',
           'n': 'н',
           'o': 'о',
           'p': 'п',
           'r': 'р',
           's': 'с',
           't': 'т',
           'u': 'у',
           'w': 'в',
           'ʷ': 'в',
           '˳': 'в',
           'z': 'з',
           'č': 'ч',
           'š': 'ш',
           'ž': 'ж',
           'ʁ': 'гъ',
           'ʕ': 'гг',
           'ʡ': 'г1',
           'χ': 'х',
           'q': 'хъ',
           'q:': 'къ',
           'q’': 'кь',
           "q'": 'кь',
           'x': 'хь',
           'ʁ': 'гъ',
           'ʕ': 'гг',
           'ʡ': 'г1',
           'uˁ': 'ю',
           'ħ': 'х1',
           'h': 'гь'}


def transcr(drg_text):
    J = {'ja': 'я',
         'ju': 'ю'}

    digr = ('ь', 'ъ')
	
	# Гласные с йотом
    drg_text = J_VJ.sub(lambda match: J[match.group()], drg_text)
    
    # Начальное е
    drg_text = E.sub(r'э', drg_text)
    
    drg_text = FAR.sub(lambda match: drg_cyr.get(match.groups()[0],
                                                 match.group(2) + '1'), drg_text)
    drg_text = ABR.sub(lambda match: drg_cyr.get(match.groups()[0],
                                                 match.group(2) + '1'), drg_text)
    drg_text = HEM.sub(lambda match: drg_cyr[match.group(2)] * 2, drg_text)

    for sv in STRESSED_VOWELS:
        # Снятие диакритик-ударений с гласных 
        drg_text = drg_text.replace(sv, DIACRITICS[sv])
    
    
    # Преобразование основных символов
    cyr = ''
    i = 0
    while i < len(drg_text) - 1:
        
        s = drg_text[i]
        if (not s.isalpha()) or (s in drg_cyr.values()) or (s in J.values()) or s in digr:
            cyr += drg_text[i]
        else:
            letter = drg_text[i]
            next_letter = drg_text[i + 1]
            if next_letter not in {"'", '’', ':', 'ˤ'}:
                next_letter = ''
            else:
                i += 1
            cyr += drg_cyr[letter + next_letter]
        i += 1
    cyr += drg_cyr.get(drg_text[-1], drg_text[-1]) if drg_text[-1].isalnum() else ''
    # isalnum для случаев типа к1#'
    return cyr


# print(drg)


text = "ʡáˤpːásí"


print(transcr(text.lower()))




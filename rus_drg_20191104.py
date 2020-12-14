# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 01:45:33 2018

@author: oleg
"""

import time

import re

HEM = re.compile(r'(([иаеупткшсчцх]|хь)\2)', re.I)  # Проверять через finditer
ABR = re.compile(r'(([кпчтпц])[1|])', re.I)
PALKA = re.compile(r'(?<=[кпчцхгпт])[I1|l]', re.I)
LAB = re.compile(r"(([кпчхгтпцъьaː])в)", re.I)
# GLOT = re.compile(r'\bъ(?=[аоуеэи])',re.I)
FAR = re.compile(r'(?<=[ауэеи])[1|]', re.I)  # Фарингализация незадних - бывает не во всех диалектах

J_VJ = re.compile(r'(?<=[аоуеиэюя])[яю]|\b([яю])', re.I)  # контексты, где я -> ja

regular = {HEM:'ː',
           ABR: "’",
           FAR: 'ˤ',
           LAB: 'ʷ'}

digr = {'гъ': 'ʁ',
        'гь': 'h',
        'г1': 'ʡ',
        'гг': 'ʕ',
        'къ': 'qː',
        'кь': 'q’',
        'х1': 'ħ',
        'хъ': 'q',
        'хь': 'x'}

cyr_drg = {'а': 'a',
           'б': 'b',
           'в': 'w',
           'г': 'g',
           'д': 'd',
           'е': 'e',
           'ж': 'ž',
           'з': 'z',
           'и': 'i',
           'й': 'j',
           'к': 'k',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
           'у': 'u',
           'ф': 'f',
           'х': 'χ',
           'ц': 'c',
           'ч': 'č',
           'ш': 'š',  # фаринг гласных - глсн + 1
           'э': 'e',
           'ю': 'uˤ',  # Встречаются ли ю, ё, есть ли контексты с йотом??? ю редко будет в фарингализации
           'я': 'aˤ',
           'ы': 'ы',
           'ь': 'ь'}  # я - фарингализация. Какие гласные фаринг?

J = {'я': 'ja',
     'ю': 'ju'}


def transcr(cyr_text):

    for pat in regular.keys():  # Замена в регулярных для фон знаков конетекстах
        fon_znak = regular[pat]
        one = lambda match: match.group(2) + fon_znak
        cyr_text = pat.sub(one, cyr_text)

    for d in digr.keys():
        cyr_text = cyr_text.replace(d, digr[d])

    cyr_text = PALKA.sub('1', cyr_text)
    cyr_text = J_VJ.sub(lambda match: J[match.group()], cyr_text)

    drg = ''
    i = 0
    while i < len(cyr_text) - 1:

        s = cyr_text[i]

        if s in digr.values() or (not s.isalpha()) or (s in cyr_drg.values()) or (s in regular.values()):
            drg += cyr_text[i]
        else:
            letter = cyr_text[i].lower()
            drg += cyr_drg[letter]
        i += 1
    drg += cyr_drg.get(cyr_text[-1], cyr_text[-1])
    return drg

#text = 'Гьел бик1уле саби: к|аор болотный тьма «Ца – бик1уле саб – давлачевсе дурх1я тев, – бик1уле саби – левкьунне ггяшшала рурссилишшу ссукни». '
#print(transcr(text.lower()))





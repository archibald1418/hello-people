# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 19:36:38 2018

@author: 1
"""

'''05.01.2018. Revisiting Roman numberals algorithm. 
Works for digits from 1 to 3999'''

def razryady (n):
	'''Recursively decomposes a number into decimal digits'''
	ostatok = n % 10
	digits.append (ostatok)
	if ostatok == n:
		return digits
	else:
		return razryady (n // 10)

def roman (digits):
	'''Converts digits of a number starting from units'''
	assoc = dict (zip ([0, 1, 5, 10, 50, 100, 500, 1000], # Basic terms mapping
			   ['', 'I','V','X','L','C','D','M'])) 
	output = ''
	for i in range (len (digits)):# i denoting the current decimal place 
		razryad = digits[i] 
		scale = 10 ** i 			# Scaling 10 so it matches a given term from the notation
		if razryad in (4, 5, 9):		# Special notation for 4 and 9. 5 needed to make distinction between 4 and 9.
			output += assoc[scale * (razryad + int (10 % razryad != 0))] + 
			(int ((razryad + 1) % 5 == 0)) * assoc[scale]
			# The boolean magic determines whether we should get 5 or 10 from the dict
		else:
			output += assoc[scale] * (razryad % 5) + assoc[scale * (razryad - (razryad % 5))]
	return output[::-1]

n = int(input("Pick a number from 1 to 3999: "))

digits = []

razryady(n)

print(roman(digits))

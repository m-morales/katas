# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:18:05 2020

@author: XRU1127
"""


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

print (digital_root(456))

def is_isogram(word):
    if isinstance(word,str):
        w = word.lower() # Ignorar si son mayúsculas o minúsculas
        return len(w) == len(set(w)) if w else True
    else:
        raise TypeError('Argumento debería ser string')
        
def solution(number):
   #print ("Hi")
    cnumb = number - 1
    suma = 0
    for i in range(cnumb,0,-1): 
          #print (i, suma)
          if (i % 5) == 0:
              suma = suma + i
          else:
              if (i % 3) == 0:
                  suma = suma + i
    return suma

def alphabet_position(text):
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = ""
    li = list(alpha) 
    di = { li[i] : str(i+1) for i in range(0, len(li) ) }
    for letra in text:
        #l = di.get(letra)
        if letra in di:
            #print (letra)
            num = num + (di.get(letra))
            num = num + " "
        else:
            pass
        print ("--->" + num)
    num = num[:-1]
    return num
    
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



import string

def is_pangram(s):
    s = s.lower()
    letras = "abcdefghijklmnopqrstuvwxyz"
    cont_letras = ""
    for cara in s:
        if cara in letras:
            cont_letras = cont_letras + cara
        else:
            pass
    cont_letras = set(cont_letras)
    cont_letras = ''.join(cont_letras)
    if len(cont_letras) == 26:
        return True
    else:
        return False
   

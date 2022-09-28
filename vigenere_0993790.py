student = [('0993790', 'Mohammed Tarkhany', 'INF1J')]
alphabet = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o':14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O':14,
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' , 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def group_info():
    return student

def split(string):
    return[i for i in string]

def encrypt_vigenere(plaintext, key):
    lenword = len(plaintext)
    lenkey = len(key)
    word = split(plaintext)
    key = split(key)
    theword = ''
    b = 0
    c = 0

    while b < lenword:
        if c == len(key):
            c = 0

        letter = word[b]

        if letter not in alphabet:
            theword = theword + letter

        else:
            LETTER = alphabet[letter]
            keyletter = key[c]
            KEY = alphabet[keyletter]
            shiftletter = LETTER + KEY

            if shiftletter >= 26:
                shiftletter = shiftletter - 26
            if letter in alpha:
                theletter = alpha[shiftletter]
            if letter in Alpha:
                theletter = Alpha[shiftletter]
            c = c + 1
            theword = theword + theletter
        b = b + 1
    return theword

def decrypt_vigenere(ciphertext, key):
    lenword = len(ciphertext)
    lenkey = len(key)
    word = split(ciphertext)
    key = split(key)
    theword = ''
    b = 0
    c = 0

    while b < lenword:
        if c == len(key):
            c = 0

        letter = word[b]

        if letter not in alphabet:
            theword = theword + letter

        else:
            LETTER = alphabet[letter]
            keyletter = key[c]
            KEY = alphabet[keyletter]
            shiftletter = LETTER - KEY
            if shiftletter < 0:
                shiftletter = shiftletter + 26
            if letter in alpha:
                theletter = alpha[shiftletter]
            if letter in Alpha:
                theletter = Alpha[shiftletter]
            c = c + 1
            theword = theword + theletter
        b = b + 1
    return theword

from english_quadgrams import quadgram_score

def quadgram_fitness(text):
    theword = text
    theword = split(theword)
    lenword = len(theword)
    woordje = ''
    a = 0
    b = 0

    while a < lenword:
        if theword[b] in alpha:
            woordje = woordje + theword[b]
        elif theword[b] in Alpha:
            woordje = woordje + theword[b].lower()
        a += 1
        b += 1

    woordje = split(woordje)
    lenwoordje = len(woordje)
    fourword = ''
    a = 0
    b = 0
    c = 0
    valueword = 0
    lenwoordje = lenwoordje-3
    while a < lenwoordje:
        fourword = woordje[a] + woordje[a+1] + woordje[a+2] + woordje[a+3]
        a += 1
        if fourword in quadgram_score:
            valueword = valueword + (quadgram_score[fourword])
        else:
            valueword = valueword + 23
    return valueword

import random

def solve_vigenere(ciphertext, keylen):
    splitkey = []
    for i in range(keylen):
        letter = random.choice(alpha)
        splitkey.append(letter)
    text = decrypt_vigenere(ciphertext, splitkey)
    oldscore = quadgram_fitness(text)
    save_key = splitkey
    bestscore = 1000000000
    newscore = 1000000000
    for i in range(1000*keylen*keylen):
        splitkey = list(save_key)
        pos = random.randrange(len(splitkey))
        splitkey[pos] = random.choice(alpha)
        text = decrypt_vigenere(ciphertext, splitkey)
        newscore = quadgram_fitness(text)


        if newscore < oldscore:
            save_key = list(splitkey)
            oldscore = newscore


        if newscore < bestscore:

            bestscore = newscore
            the_result = text
            the_key = save_key
            the_real_key = ''
            for i in range(len(the_key)):
                the_real_key += the_key[i]

        a = random.randrange(1,100)
        if a == 1:
            save_key = list(splitkey)
            oldscore = newscore


    return the_real_key, the_result

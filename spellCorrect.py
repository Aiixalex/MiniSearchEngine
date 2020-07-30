import re
import time

from collections import Counter


f_big = open('big.txt', 'r')
WORDS = Counter(re.findall(r'\w+', f_big.read()))
f_big.close()


def correction(word, DICT):
    max = 0
    result = ''
    sum_dict = sum(DICT.values())
    if word != 'AND' and word != 'OR' and word != 'NOT':
        word=word.lower()
    for candidate in candidates(word):
        Probability = DICT[candidate] / sum_dict
        if Probability > max:
            result = candidate
            max = Probability
    return result


def candidates(word):
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    return set(w for w in words if w in WORDS)


def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def correctSentence(input):
    # words = input.split(' ')
    res = []
    for word in input:
        if '*' in word or '?' in word:
            res.append(word)
        elif word == '(' or word == ')':
            res.append(word)
        else:
            res.append(correction(word, WORDS))
    return res

if __name__ == '__main__':
    time_start = time.time()
    print(candidates('approxmtely'))
    print(correction('approxmtely', WORDS))
    time_end = time.time()
    print('time cost',time_end-time_start,'s')
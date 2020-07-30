import queue
import nltk

from nltk.corpus import wordnet
from spellCorrect import correctSentence
from phrase_search import searchPhrase
from topK_search import topK_search


def getSynonyms(index, words):
    stem = ''
    for word in words :
        stem += word.lower()
    result = [words]
    for synset in wordnet.synsets(stem):
        for lemma in synset.lemmas():
            wordlist = lemma.name().split('_')
            if wordlist not in result:
                result.append(wordlist)
    return result


def searchSynonym(index, word, model_path, docID_path, K) :
    wordlist = getSynonyms(index, word)
    file_list = open(docID_path, 'r')
    docID_list = eval(file_list.read())
    file_list.close()
    print("synonym")
    print("-----------------------------------------------------")
    for resultWord in wordlist :
        outWord = ""
        for w in resultWord :
            outWord += w + " "
        print(outWord)
    print("")
    resultList = {}
    print("result")
    print("-----------------------------------------------------")
    for phraseList in wordlist :
        # print(phraseList)
        wordset = set(phraseList)
        list = searchPhrase(index, wordset, phraseList)
        phrase = ''
        for w in phraseList :
            phrase += w + " "
        if len(list) > 0 :
            print(phrase[:-1], ":")
            for key in list.keys() :
                docList = [key for key in list.keys()]
            topK_search(phraseList, docList, model_path, len(docID_list), K)
            print("")
            resultList[phrase] = list

    return resultList


def synonym_search(args) :
    args_dict = vars(args)
    tokens = args_dict['query']
    model_path = 'vsm.txt'
    docID_path = 'docID_list.txt'
    K = args_dict['Kvalue']
    index_path = 'inverted_index.txt'
    file_index = open(index_path, 'r')
    inverted_index = eval(file_index.read())
    file_index.close()

    search_sentence = ''
    for token in tokens :
        search_sentence += token + ' '
    tokens = search_sentence.split()
    print("Query Statement")
    print(tokens)
    print("Spelling Correcting")
    tokens = correctSentence(tokens)
    print(tokens)
    print("")
    resultlist = searchSynonym(inverted_index, tokens, model_path, docID_path, K)


if __name__ == '__main__' :
    synonym_search('')

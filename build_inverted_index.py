import json
import os
import re
import time
from collections import Counter

import nltk

from spellCorrect import correction


def build_inverted_index(args):
    time_start = time.time()

    args_dict = vars(args)
    document_folder_path = args_dict['folder']
    index_path = 'inverted_index.txt'
    docID_path = 'docID_list.txt'

    # load the dictionary for spell correction
    f_big = open('big.txt', 'r')
    WORDS = Counter(re.findall(r'\w+', f_big.read()))
    f_big.close()

    inverted_index = {}
    pathDir = os.listdir(document_folder_path)
    docID_list = [int(eachDir.replace('.html', '')) for eachDir in pathDir]
    # docID_list.sort() # Process files in docID order
    for docID in docID_list:
        file_doc = open(document_folder_path + '/' + str(docID) + '.html', 'r')
        text = file_doc.read().lower()                 # convert to lowercase letters
        words = re.sub("[^a-zA-Z]", " ", text).split() # clear all punctuations and numbers
        word_num = 1
        for word in words:
            if word in nltk.corpus.stopwords.words('english'): # if not stop words
                word_num += 1
                continue
            if word not in inverted_index.keys(): # if word is not already in inverted_index
                inverted_index[word] = {}
                if docID not in inverted_index[word].keys():
                    inverted_index[word][int(docID)] = []
                    inverted_index[word][docID].append(word_num)
                else:
                    inverted_index[word][docID].append(word_num)

            else: # if word is already in inverted_index
                if docID not in inverted_index[word].keys() :
                    inverted_index[word][docID] = []
                    inverted_index[word][docID].append(word_num)
                else :
                    inverted_index[word][docID].append(word_num)

            word_num += 1

        file_doc.close()

    # add document frequency e.g. {'test': {2:[1,3,5], 3:{1, 3, 5}}}} -> {'test': [2, {2:[1,3,5], 3:{1, 3, 5}}]}
    for term, posting_list in zip(inverted_index.keys(), inverted_index.values()):
        inverted_index[term] = [len(posting_list), posting_list]

    file_docID_list = open(docID_path, 'w')
    file_docID_list.write(str(docID_list))
    file_docID_list.close()

    file_index = open(index_path, 'w')
    # write inverted index into the file
    # js = json.dumps(inverted_index)
    # file_index.write(js)
    # file_index.close()
    file_index.write(str(inverted_index))
    print('The inverted index of the document set in folder \'{0}\' has been built and written to \'{1}\'.'
          .format(document_folder_path, index_path))

    time_end = time.time()
    print('time cost',time_end-time_start,'s')

if __name__ == '__main__':
    print('1')
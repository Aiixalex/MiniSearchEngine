import queue
import nltk
from spellCorrect import correctSentence
from topK_search import topK_search


def andTwoList(list1, list2):
    list = []
    len1 = len(list1)
    len2 = len(list2)
    n1 = 0
    n2 = 0
    while n1 < len1 and n2 < len2:
        if list1[n1] < list2[n2]:
            n1 += 1
        elif list1[n1] > list2[n2]:
            n2 += 1
        else:
            list.append(list1[n1])
            n1 += 1
            n2 += 1
    return list


def searchWord(index, word):
    if word not in index:
        return []
    else:
        # 将所有文档id变为数字
        docList = [int(key) for key in index[word][1].keys()]
        # 将文档的id排序
        docList.sort()
        return docList


def searchPhrase(index, words, inputList):
    if len(words) == 0:
        return []
    docQueue = queue.Queue()
    for word in words:
        if word not in nltk.corpus.stopwords.words('english'):
            docQueue.put(searchWord(index, word))

    while docQueue.qsize() > 1:
        list1 = docQueue.get()
        list2 = docQueue.get()
        docQueue.put(andTwoList(list1, list2))
    doclist = docQueue.get()

    resultList = {}

    if len(inputList) == 1:
        for doc in doclist:
            resultList[doc] = index[inputList[0]][1][doc]
        return resultList

    # print(doclist)
    for docid in doclist:
        docid = docid
        locList = []
        statrNum = 0
        for word in inputList:
            if word in nltk.corpus.stopwords.words('english'):
                statrNum += 1
            else:
                break
        for loc in index[inputList[statrNum]][1][docid]:
            floc = loc
            n = len(inputList)
            hasFind = True
            for word in inputList[statrNum + 1:n]:
                floc += 1
                if word not in nltk.corpus.stopwords.words('english'):
                    try:
                        index[word][1][docid].index(floc)
                    except:
                        hasFind = False
                        break
            if hasFind:
                locList.append(loc)
        if len(locList) > 0:
            resultList[docid] = locList
    return resultList


def phrase_search(args):
    args_dict = vars(args)
    tokens = args_dict['query']

    index_path = 'inverted_index.txt'
    file_index = open(index_path, 'r')
    inverted_index = eval(file_index.read())
    file_index.close()

    search_sentence = ''
    for token in tokens:
        search_sentence += token + ' '
    tokens = search_sentence.split()
    print("Query Statement")
    print(tokens)
    print("Spelling Correcting")
    tokens = correctSentence(tokens)
    print(tokens)
    words = set(tokens)
    phraseDocList = searchPhrase(inverted_index, words, tokens)
    if 0 == len(phraseDocList):
        print("Doesn't find \"", tokens, '"')
    else:
        '''
        for key in phraseDocList:
            print('docID: ', key, "   num: ", len(phraseDocList[key]))
            print('    location: ', phraseDocList[key])
        '''
        model_path = 'vsm.txt'
        docID_path = 'docID_list.txt'
        K = args_dict['Kvalue']
        docList = [id for id in phraseDocList]
        file_list = open(docID_path, 'r')
        docID_list = eval(file_list.read())
        file_list.close()
        print(tokens, docList, model_path, len(docID_list), K)
        topK_search(tokens, docList, model_path, len(docID_list), K)


if __name__ == '__main__':
    phrase_search('')

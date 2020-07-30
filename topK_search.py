import math
from heapq import *
from operator import itemgetter

def topK_search(query, docID_list, model_path, doc_num, K):

    # read inverted index from the file
    file_vsm = open(model_path, 'r')
    vsm_model = eval(file_vsm.read())
    file_vsm.close()

    # 去除查询中文档集不存在的词项
    dictionary = [word for word in vsm_model]
    for token in query:
        if token not in dictionary:
            query.remove(token)

    #计算查询向量
    rank = {}
    q_length = 0
    q_vector = {}
    items = set(query)
    #查询向量权重
    for token in items:
        q_vector[token] = (1 + math.log(query.count(token), 10)) * math.log( float(doc_num / len(vsm_model[token])), 10)
    for token in items:
        q_length += math.pow(q_vector[token], 2)
    q_length = math.sqrt(q_length)

    # print(len(docID_list))

    for docID in docID_list:
        docID = str(docID)
        for token in vsm_model:
            if docID not in vsm_model[token]:
                vsm_model[token][docID] = 0

    # 计算文档向量长度
    doc_length = {}
    for docID in docID_list:
        docID = str(docID)
        doc_length[docID] = 0;
        for word in vsm_model:
            if vsm_model[word][docID] != 0:
                doc_length[docID] += math.pow(vsm_model[word][docID], 2)
        doc_length[docID] = math.sqrt(doc_length[docID])

    #文档向量归一化
    for docID in docID_list:
        docID = str(docID)
        for word in vsm_model:
            vsm_model[word][docID] = float(vsm_model[word][docID]) / float(doc_length[docID])

    # 计算余弦相似度
    for docID in docID_list:
        docID = str(docID)
        rank[docID] = 0
        for token in items:
            rank[docID] += float(q_vector[token]) * float(vsm_model[token][docID])
        rank[docID] /= float(q_length)

    #对得分列表rank基于堆TopK排序
    N = len(docID_list)
    K = int(K)

    for docID in docID_list:
        docID = str(docID)
        if rank[docID] == 0:
            N = N - 1
            rank.pop(docID)

    if K > N:
        ranklist = rank.items()
        reslist = [[-v[1], v[0]] for v in ranklist] #变为负值后升序排列
        reslist.sort()
        res  = [reslist[i] for i in range(0, len(reslist))]
        for rankvalue,docID in res:
            print(docID, -rankvalue)
    else:
        for docID in docID_list:
            docID = str(docID)
            rank[docID] = rank[docID]
        heap = []
        ranklist = rank.items()
        ranklist = [[v[1], v[0]] for v in ranklist]
        for i in range(K):
            rankvalue, docID = ranklist[i]
            heappush(heap, [rankvalue,docID])
        for i in range(K, N):
            rankvalue, docID = ranklist[i]
            heappush(heap, [rankvalue, docID])
            heappop(heap)
        for rankvalue, docID in nlargest(K,heap):
            print(docID, rankvalue)

if __name__ == '__main__':
    topK_search('')
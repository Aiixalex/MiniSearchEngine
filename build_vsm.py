import os
import math
import json
import time
from collections import defaultdict

def build_vsm(args):
    time_start = time.time()

    args_dict = vars(args)

    document_folder_path = args_dict['folder']

    index_path = 'inverted_index.txt'
    file_index = open(index_path, 'r')
    inverted_index = eval(file_index.read())
    file_index.close()

    vsm_path = 'vsm.txt'

    vsm_model = defaultdict(dict)

    pathDir = os.listdir(document_folder_path)
    docID_list = [int(eachDir.replace('.html', '')) for eachDir in pathDir]
    docID_list.sort()  # Process files in docID order
    N = len(docID_list)

    position_dict = {}
    for token in inverted_index:
        position_dict = inverted_index[token][1]
        df = inverted_index[token][0]
        idf = math.log(float(N / df), 10)
        for doc_ID in docID_list:
            if doc_ID not in position_dict:
                continue
            else:
                tf = len(position_dict[doc_ID])  # 计数doc_ID文档中token个数
                vsm_model[token][doc_ID] = float( 1 + math.log(tf, 10)) * float(idf)
    del inverted_index
    del docID_list

    file_index = open(vsm_path, 'w')
    js = json.dumps(vsm_model)
    file_index.write(js)
    # file_index.write(str(vsm_model))
    file_index.close()
    print('The vsm model of the document set in folder \'{0}\' has been built and written to \'{1}\'.'
          .format(document_folder_path, vsm_path))

    time_end = time.time()
    print('time cost', time_end - time_start, 's')

if __name__ == '__main__':
    print('2')
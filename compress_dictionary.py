import time


def front_coding(dict_key) :
    return str(len(dict_key)) + dict_key


def postingList_compress(posting_list) :
    result = []
    for i in range(posting_list.__len__()):
        if i is not 0:
            result.append(posting_list[i] - posting_list[i-1])
        else:
            result.append(posting_list[i])
    return result


def compress_dictionary(args):
    time_start = time.time()

    index_path = 'inverted_index.txt'
    file_index = open(index_path, 'r')
    inverted_index = eval(file_index.read())
    file_index.close()

    # sort words in dictionary
    dict_keys = sorted(inverted_index.keys())
    dictionary = {}
    if '' in dict_keys:
        dict_keys.remove('')
    for dict_key in dict_keys:
        dictionary[dict_key] = inverted_index[dict_key]

    #
    dict_pointers = {}
    list_postingList = []
    dict_str = ''
    str_pointer = 0
    for i in range(dict_keys.__len__()):
        dict_key = dict_keys[i]
        doc_freq = dictionary[dict_key][0]
        posting_list = list(dictionary[dict_key][1].keys())

        dict_str += front_coding(dict_key)

        dict_pointers[str_pointer] = []
        dict_pointers[str_pointer].append(doc_freq)
        dict_pointers[str_pointer].append(i)

        list_postingList.append(postingList_compress(sorted(posting_list)))

        str_pointer += len(front_coding(dict_key))

    # for dict_key in dict_keys:
    #     docID_list = list(dictionary[dict_key][1].keys())
    #     for i in range(docID_list.__len__()) :
    #         if i is not 0:
    #             dictionary[dict_key][1][docID_list[i]-docID_list[i-1]] = dictionary[dict_key][1][docID_list[i]]
    #             dictionary.pop()

    str_path = 'DictionaryString.txt'
    file_str = open(str_path, 'w')
    file_str.write(dict_str)
    file_str.close()

    dict_path = 'dict_pointers.txt'
    file_dict = open(dict_path, 'w')
    file_dict.write(str(dict_pointers))
    file_dict.close()

    posting_path = 'posting_list.txt'
    file_posting = open(posting_path, 'w')
    file_posting.write(str(list_postingList))
    file_posting.close()

    print('The Dictionary has been built and compressed.')
    print('The long string consisting all words is saved in file \'{}\''.format(str_path))
    print('The dictionary consisting the pointer of words and posting lists is saved in file \'{}\''.format(dict_path))
    print('The list consisting all posting lists is saved in file \'{}\''.format(posting_path))

    time_end = time.time()
    print('time cost', time_end - time_start, 's')

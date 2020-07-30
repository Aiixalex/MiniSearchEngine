import collections

from spellCorrect import correctSentence
from wildcard_query import wildcard_query

"""
shunting yard algorithm
"""
def shunting_yard(tokens):
    precedence_dict = {'OR': 1, 'AND': 2, 'NOT': 3, '(': 0, ')': 0}
    output_queue = []
    operator_stack = []
    for token in tokens:
        if token == '(':
            operator_stack.append(token)
        elif token == ')':
            operator = operator_stack.pop()
            while operator is not '(':
                output_queue.append(operator)
                operator = operator_stack.pop()

        elif token in precedence_dict.keys():
            if operator_stack:
                top_operator = operator_stack[-1]
                while operator_stack and precedence_dict[top_operator] >= precedence_dict[token]:
                    output_queue.append(operator_stack.pop())
                    if operator_stack:
                        top_operator = operator_stack[-1]

            operator_stack.append(token)
        else:
            output_queue.append(token)

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def boolean_search(args):
    args_dict = vars(args)
    tokens = args_dict['query']

    # read inverted index from the file
    index_path = 'inverted_index.txt'
    file_index = open(index_path, 'r')
    inverted_index = eval(file_index.read())
    file_index.close()

    # read docID list from the file
    docID_path = 'docID_list.txt'
    file_docID_list = open(docID_path, 'r')
    docID_list = eval(file_docID_list.read())
    file_docID_list.close()

    # separate out the brackets
    search_sentence = ''
    for token in tokens:
        search_sentence += token + ' '
    search_sentence = search_sentence.replace('(', ' ( ')
    search_sentence = search_sentence.replace(')', ' ) ')
    tokens = search_sentence.split()

    for i in range(tokens.__len__()):
        if (tokens[i] != 'AND') and (tokens[i] != 'OR') and (tokens[i] != 'NOT'):
            tokens[i] = tokens[i].lower()

    print("Query Statement")
    print(tokens)
    print("Spelling Correcting")
    tokens = correctSentence(tokens)
    print(tokens)

    # tokens in postfix order
    postfix_tokens = shunting_yard(tokens)

    postfix_tokens_queue = collections.deque(postfix_tokens)
    result_stack = []

    while postfix_tokens_queue:
        token = postfix_tokens_queue.popleft()
        if token == 'AND':
            operand_a = result_stack.pop()
            operand_b = result_stack.pop()
            result_stack.append(list(set(operand_a).intersection(set(operand_b))))
        elif token == 'OR':
            operand_a = result_stack.pop()
            operand_b = result_stack.pop()
            result_stack.append(list(set(operand_a).union(set(operand_b))))
        elif token == 'NOT':
            operand = result_stack.pop()
            result_stack.append(list(set(docID_list).difference(set(operand))))
        else:
            if token in inverted_index.keys():
                result_stack.append(list(inverted_index[token][1].keys()))
            else:
                if '*' not in token and '?' not in token:
                    result_stack.append([])
                else:
                    wildcard_tokens = wildcard_query(token, list(inverted_index.keys()))
                    print('Wildcard Query Result:')
                    print(wildcard_tokens)
                    posting_result = []
                    for token in wildcard_tokens:
                        posting = list(inverted_index[token][1].keys())
                        posting_result = list(set(posting_result).union(set(posting)))
                    result_stack.append(posting_result)

    print('Found {} document(s) that matched query:'.format(len(result_stack[-1])))
    print(result_stack.pop())

if __name__ == '__main__':
    print('1')
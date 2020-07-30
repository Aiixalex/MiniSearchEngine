import argparse

from boolean_search import boolean_search
from compress_dictionary import compress_dictionary
from build_inverted_index import build_inverted_index
from build_vsm import build_vsm
from phrase_search import phrase_search
from synonym_search import synonym_search
from topK_search import topK_search

"""
 要求实现 倒排索引以及 向量空间模型
 同时支持 布尔查询、通配查询、拼写矫正、基于快速评分的Top K查询、短语查询、同义词扩展、索引压缩、构建和使用词典索引 功能
"""
def main():
    parser = argparse.ArgumentParser(description='Welcome to use Mini Search Engine.')

    sub_parser = parser.add_subparsers(title='Commands', description='These are common MiniSearchEngine commands '
                                                                     'used in various situations.', help='')

    inverted_index_parser = sub_parser.add_parser('index',
                                                  help='build the Inverted Index of a Document Set')
    inverted_index_parser.add_argument('-f', '--folder', required=True)
    inverted_index_parser.set_defaults(func = build_inverted_index)

    vsm_parser = sub_parser.add_parser('vsm', help='build the VSM of a Document Set')
    vsm_parser.add_argument('-f', '--folder')
    vsm_parser.set_defaults(func=build_vsm)

    boolean_search_parser = sub_parser.add_parser('boolean', help='Boolean Search')
    boolean_search_parser.add_argument('-q', '--query', nargs='*', required=True)
    boolean_search_parser.set_defaults(func = boolean_search)

    phrase_search_parser = sub_parser.add_parser('phrase', help='Phrase Search')
    phrase_search_parser.add_argument('-q', '--query', nargs='*')
    phrase_search_parser.add_argument('-k', '--Kvalue', default=10)
    phrase_search_parser.set_defaults(func=phrase_search)

    synonym_search_parser = sub_parser.add_parser('synonym', help='Synonym Search')
    synonym_search_parser.add_argument('-q', '--query', nargs='*')
    synonym_search_parser.add_argument('-k', '--Kvalue', default=10)
    synonym_search_parser.set_defaults(func=synonym_search)

    dict_parser = sub_parser.add_parser('compress', help='Build and Compress Dictionary')
    dict_parser.set_defaults(func=compress_dictionary)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
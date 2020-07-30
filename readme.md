## MiniSearchEngine Code Description

#### Help Menu

~~~
python main.py -h
~~~

![help](D:\code\MiniSearchEngine\test_results\help.bmp)

#### Building Inverted Index

~~~
python main.py index -f Reuters
~~~

![build_inverted_index](D:\code\MiniSearchEngine\test_results\build_inverted_index.bmp)

#### Building Vector Space Model

~~~
python main.py vsm -f Reuters
~~~

![build_vsm](D:\code\MiniSearchEngine\test_results\build_vsm.bmp)

#### Boolean Search

~~~
python main.py boolean -q government AND policy
~~~

![boolean_search](D:\code\MiniSearchEngine\test_results\boolean_search.bmp)

#### Wildcard Query

~~~
python main.py boolean -q *formatio*
~~~

![wildcard_query](D:\code\MiniSearchEngine\test_results\wildcard_query.bmp)

#### Phrase Query

~~~
python main.py phrase -k 10 -q United Kingdom
~~~

![phrase_query](D:\code\MiniSearchEngine\test_results\phrase_query.bmp)

#### Fuzzy Query

~~~
python main.py boolean -q gurantee
~~~

![fuzzy_query](D:\code\MiniSearchEngine\test_results\fuzzy_query.bmp)

#### Synonym Query

~~~
python main.py synonym -k 10 -q education
~~~

![synonym_query_1](D:\code\MiniSearchEngine\test_results\synonym_query_1.bmp)
![synonym_query_2](D:\code\MiniSearchEngine\test_results\synonym_query_2.bmp)

#### Top K Query

~~~
python main.py phrase -k 10 -q education
~~~

![TopK_query](D:\code\MiniSearchEngine\test_results\TopK_query.bmp)

#### Dictionary Compress

~~~
python main.py compress
~~~

![dictionary_compress](D:\code\MiniSearchEngine\test_results\dictionary_compress.bmp)
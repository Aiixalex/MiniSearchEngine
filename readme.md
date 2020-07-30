## MiniSearchEngine Code Description

#### Help Menu

~~~
python main.py -h
~~~

#### Building Inverted Index

~~~
python main.py index -f Reuters
~~~

#### Building Vector Space Model

~~~
python main.py vsm -f Reuters
~~~

#### Boolean Search

~~~
python main.py boolean -q government AND policy
~~~

#### Wildcard Query

~~~
python main.py boolean -q *formatio*
~~~

#### Phrase Query

~~~
python main.py phrase -k 10 -q United Kingdom
~~~

#### Fuzzy Query

~~~
python main.py boolean -q gurantee
~~~

#### Synonym Query

~~~
python main.py synonym -k 10 -q education
~~~

#### Top K Query

~~~
python main.py phrase -k 10 -q education
~~~

#### Dictionary Compress

~~~
python main.py compress
~~~

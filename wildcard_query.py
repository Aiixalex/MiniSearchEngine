import re


def wildcard2pattern(wildcard) :
    pattern = '^'
    for i in range(wildcard.__len__()) :
        if wildcard[i] == '*' :
            pattern += '[a-z]*'
        elif wildcard[i] == '?' :
            pattern += '[a-z]'
        else :
            pattern += wildcard[i]

    pattern += '$'
    return pattern


def wildcard_query(wildcard, tokenList) :
    wildcard_tokens = []

    pattern = wildcard2pattern(wildcard)
    prog = re.compile(pattern, flags=re.IGNORECASE)

    for token in tokenList :
        if prog.match(token) :
            wildcard_tokens.append(token)

    return wildcard_tokens


if __name__ == '__main__' :
    print(wildcard2pattern('pr?ces*'))

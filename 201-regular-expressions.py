if __name__ == '__main__':
    regex = 'abc'
    regex = 'a+bc' # + znaczy jeden lub więcej razy - taka pętla z wierzchołka do samego siebie abc, aabc, aaabc...
    regex = 'a*bc' # * 0 lub więcej razy - bc, abc, aabc...
    regex = 'a{4}bc' # aaaabc
    regex = 'a{1,4}bc' # literka a od 1 do 4 razy - abc, aabc, aaabc, aaaabc
    regex = 'a?bc' # ? - 0 lub 1 - abc, bc
    regex = '[a-z]' # dowolna litera od a do z. Z liter łacińskich
    regex = '[A-Z]' # dowolna litera od A do Z. Z liter łacińskich
    regex = '[a-z]+[A-Z]*[1-9]?'
    regex = '[a-z]+[A-Z]*[1-9]{0,1}'
    regex = '[abc]' # któryś ze znaków z grupy - a, b, c
    regex = '[^a-z]' # dowolny znak, który nie jest małą literą
    regex = '.' # dowolny znak
    regex = 'a|b' # a lub b - a, b
    regex = '^abc$' # łańcuch znaków od początku napisu do końca zawierający tylko abc.

    import re

    regex = re.compile('^[a-z]+$')
    result = regex.match('hello world')
    print(result.group())

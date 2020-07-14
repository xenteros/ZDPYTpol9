"""
    Napisz wyrażenie, które dopasuje się do:
        1. Twojego imienia
        2. Twojego roku urodzenia
        3. Do wszystich domen zarejestrowanych w Polsce
        4. Do wszystkich napisów kończących się kropką
        5. Do następujących emotikonek: :) :p :( :D ;) ;p ;( ;D
        6. Do prawidłowych nazw klas w pythonie
        7. Do prawidłowych nazw metod w pythonie
"""

if __name__ == '__main__':
    regex1 = 'Adam'
    regex2 = '1980'
    regex3 = '.+[.]pl'
    regex4 = '.*[.]'
    regex5 = '([:;][)(pD])|(xD)'
    regex6 = '([A-Z][a-z]*)+'   #UpperCamelCase
    regex7 = '[a-z]+(_[a-z]+)*' #sneak_case

    import re
    words = re.findall(r'[a-z]+', 'Ala ma kota 123')
    print(words)
def read_csv(file_name, sep, quote_character, escape_character, headers=False):
    pass


if __name__ == '__main__':
    with open('books.csv', 'a', encoding='utf-8') as f:
        columns = ['id', 'title', 'author']
        # f.write(';'.join(columns))
        # f.write('\n')
        books = [
            ['1','Pan Tadeusz', 'Adam Mickiewicz'],
            ['2', 'Balladyna', 'Juliusz Słowacki']
        ]
        for book in books:
            f.write(';'.join(book))
            # f.write(';'.join([str(e) for e in book]))
            f.write('\n')

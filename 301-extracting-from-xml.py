import re

def extract_word(line):
    [word] = re.findall(r'>.+<', line)
    return word[1:-1]

def format_sentence(words):
    sentence = ' '.join(words)
    sentence = re.sub(r' (?=[^\w])', '', sentence)
    print(sentence)
    return sentence


def write_line_to_another_file(sentence):
    with open('wiki_out.txt', 'a', encoding='utf-8') as f:
        f.write(sentence + '\n')


if __name__ == '__main__':
    with open('wiki.xml', 'r', encoding='utf-8') as f:
        words = []
        for line in f:
            line = line.strip()
            if line.startswith('<s'):
                pass  # it's a new sentence
            elif line.startswith('<w'):
                words.append(extract_word(line))
            elif line.startswith('</s'):
                sentence = format_sentence(words)
                write_line_to_another_file(sentence)
                words = []

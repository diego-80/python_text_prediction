'''
This program takes a text file and generates
a sentence based on the writing style of the
corpus using a stochastic selection over the
frequency of words following one another. It
can either take a filename from the command
line or use a default file, set in the main()
function.

The main() function is deliberately simple;
the bulk of the work is done by the
go(filename) function so it is easily
available to other programs, rather than
being necessarily stand-alone.
'''

import sys
import re
import random



def get_word(string):
    match = re.match('([\w\'\-]+)', string)
    if match:
        return match.group()
    else:
        return string[0]

def predict(graph, pre=0, stop=0):
    sentence = [pre]
    index = range(len(graph))
    last = pre
    while True:
        next = random.choices(population=index, weights=graph[last], k=1)[0]
        sentence.append(next)
        if next == stop:
            break
        last = next
    return sentence

def go(filename):
    f = open(filename, 'r')
    text = str(f.read()).lower()
    text = re.sub('[^a-z,;!\s\.\?-]', '', text)
    text = text.split()
    prev = '.'  # implicit . before input text; ensures first word can be start of predicted sentence
    words = ['.']
    index = {'.': 0}
    i = 0
    while i < len(text):
        word = get_word(text[i])
        if len(word) < len(text[i]):
            text.insert(i + 1, text[i][len(word):])
            text[i] = text[i][:len(word)]
        if word not in index:
            index[word] = len(words)
            words.append(word)
        i += 1
    graph = [] #[from][to]
    for i in range(len(index)):
        sub_list = []
        for j in range(len(index)):
            sub_list.append(0)
        graph.append(sub_list)
    i = 0
    while i < len(text):
        word = text[i]
        graph[index[prev]][index[word]] += 1
        prev = word
        i += 1
    sentence = predict(graph, 0, 0)
    print_sentence(nums_to_words(sentence, index))

def nums_to_words(sentence, index):
    keys = list(index.keys())
    vals = list(index.values())
    word_sentence = []
    for val in sentence[1:]:
        word_sentence.append(keys[vals.index(val)])
    return word_sentence

def print_sentence(word_sentence):
    out = ''
    for i in range(len(word_sentence)):
        print(word_sentence[i], end='')
        if i < len(word_sentence)-1 and re.match('([\w])', word_sentence[i+1][0]):
            print(' ', end='')

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'text.txt'
    go(filename)

if __name__ == '__main__':
    main()
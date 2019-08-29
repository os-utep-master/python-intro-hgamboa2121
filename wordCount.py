
import re

string = dict()
file = open("declaration.txt", "r")
for line in file:
    line = line.split(' ')
    line = re.sub('[^A-Za-Z0-9]+', ' ', line)

    for word in line:
        if word in string.keys():
            string[word] += 1
        else:
            string[word] = 1

string.pop('')

wordCountKey = open("myOutput.txt", 'w+')

for setWord in sorted(string.keys()):
    wordCountKey.write("%s %s\n" % (setWord, string[setWord]))
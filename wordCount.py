
import re

string = dict()
file = open("declaration.txt", "r")
for line in file:
    line = line.split(' ')
    line = re.sub('[^A-Za-z0-9]+', ' ', line)
    line = line.lower()

    for word in line:
        if word in string.keys():
            string[word] += 1
        else:
            string[word] = 1

string.pop('')

wordCountKey = open("myOutput.txt", 'w+')

for setWord in sorted(string.keys()):
    wordCountKey.write("%s %s\n" % (setWord, string[setWord]))
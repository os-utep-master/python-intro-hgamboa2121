import re

d = {}
with open("speech.txt") as f:
    for line in f:
        (key, val) = line.split().lowerCase()
        d[int(key)] = val
        f = open("speechTest.txt", "w+")
        f.write("%d\r\n" % (d + 1))

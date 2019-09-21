from array import *
import attachment
term = ['kill','rape','chop','suicide']
file = open('record.txt')
for line in file:
    for i in range(0,4):
        line.strip().split(',')
        f = open('Offensive.txt', 'a')
        if term[i] in line:
            f.write(term[i])
            f.write(" ")
            print(term[i])


f.close()
attachment.attachment

file.close()
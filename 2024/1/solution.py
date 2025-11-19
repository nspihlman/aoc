import requests
import json
import os

def main():
    leftside: list = []
    rightside: list = []
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip()
            line = line.split("   ")
            leftside.append(int(line[0]))
            rightside.append(int(line[1]))
    leftside.sort()
    rightside.sort()
    rightdict = {}
    leftset = set()
    for item in leftside:
        leftset.add(item)
    for item in rightside:
        if item not in rightdict:
            rightdict[item] = 1
        else:
            rightdict[item] += 1
    simscore = 0
    for item in leftset:
        if item not in rightdict:
            continue
        else:
            simscore += item * rightdict[item]
    print(simscore)




if __name__ == '__main__':
    main()

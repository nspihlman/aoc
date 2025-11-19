import math

def add_rule(line: str, rules: dict[int, set[int]]):
    vals = line.rstrip().split('|')
    vals = [int(v) for v in vals]
    if vals[0] not in rules:
        rules[vals[0]] = set()
    rules[vals[0]].add(vals[1])

def good_page(line: list[int], rules: dict[int, set[int]]) -> bool:
    # for each item in the line, look at everything before it. if anyting appears in the rules, bad page
    for i in range(len(line)):
        for j in range(0, i):
            if (line[i] in rules) and (line[j] in rules[line[i]]):
                return False
    return True

def sum_middle_pages(pages: list[list[int]]) -> int:
    sum = 0
    for page in pages:
        middle = math.floor(len(page) / 2)
        sum += page[middle]
    return sum

def correct_bad_pages(pages: list[list[int]], rules: dict[int, set[int]]):
    correct_pages: list[list[int]] = []
    # going to try just swapping
    for page in pages:
        for rep in range(len(page) + 2):
            for i in range(len(page)):
                for j in range(0, i):
                    if (page[i] in rules) and (page[j] in rules[page[i]]):
                        temp = page[i]
                        page[i] = page[j]
                        page[j] = temp
                        break
    

def main():
    rules: dict[int, set[int]] = {}
    # rules contains a mapping of int -> set(int), where set(int) is all the numbers 
    # that must come after the int

    # then for each page, we'll go through if n^2 times. for each number, look at the rest of the set
    with open("/Users/nicholasspihlman/code/aoc/2024/5/rules.txt") as f:
        for line in f:
            add_rule(line, rules)
    
    good_pages: list[list[int]] = []
    bad_pages: list[list[int]] = []
    with open("/Users/nicholasspihlman/code/aoc/2024/5/pages.txt") as f:
        for page in f:
            page = page.rstrip().split(',')
            page = [int(p) for p in page]
            if good_page(page, rules):
                good_pages.append(page)
            else:
                bad_pages.append(page)

    #print(sum_middle_pages(good_pages))
    correct_bad_pages(bad_pages, rules)
    print(sum_middle_pages(bad_pages))

if __name__ == '__main__':
    main()
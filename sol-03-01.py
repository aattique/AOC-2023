import re
import string
from collections import defaultdict

def get_puzzle(path):
    with open(path) as f:
        return f.readlines()


# {'#', '$', '@', '*', '-', '&', '/', '+', '%', '='}


def main():
    puzzle_path = "aoc-03-01.txt"
    file1 = get_puzzle(puzzle_path)
    
    sum = 0
    symloc = []
    #reqlist = []
    myset = []
    number = []
    for a, b in enumerate(file1):
        for c,d in enumerate(b):
            if d.isdigit() == False and d != "." and d != "\n":
                myset.append(d)
                syms = (set(myset))
                symloc.append((d,c,a))
    
    '''for ll in range(len(file1)):
        line = file1[ll]
        digits = re.split("[.]+", line)'''

    reqlist1 = defaultdict(list)
    for k,v in enumerate(file1):
        for match in re.finditer(r"\d+", v):
            for sym, loc1, ll in symloc:
                if (match.start() - 1 <= loc1 < match.end() + 1) and (k - 1 <= ll <= k + 1):
                    num = int(match.group())
                    sum += num
                    if sym == "*":
                        reqlist1[(loc1, ll)].append(num)
    
    sum2 = 0

    for req in reqlist1.values():
        if len(req) == 2:
            prod = req[0] * req[1]
            sum2 += prod

    print(sum2)


                




    '''for n,m in enumerate(v):
                if m.isdigit():
                    loc1 = n
                    if k != (len(file1) -1) and k != 0 and file1[k+1][n] in syms:
                        reqlist.append((m,n,k))
                    elif k != (len(file1) -1) and k != 0 and file1[k+1][n+1] in syms:
                        reqlist.append((m,n,k))
                    elif k != (len(file1) -1) and k != 0 and file1[k+1][n-1] in syms:
                        reqlist.append((m,n,k))    
                    elif k != (len(file1) -1) and k != 0 and file1[k-1][n] in syms:
                        reqlist.append((m,n,k))
                    elif k != (len(file1) -1) and k != 0 and file1[k-1][n+1] in syms:
                        reqlist.append((m,n,k))        
                    elif k != (len(file1) -1) and k != 0 and file1[k-1][n-1] in syms:
                        reqlist.append((m,n,k))'''
    





    
    '''for ll in range(len(file1)):
        line = file1[ll]
        digits = re.split("[.]+", line)
        
        for r in digits:
            
            if r not in syms and r !='' and re.search("['#' | '$' | '@' | '*' | '-' | '&' | '/' | '+' | '%'| '=']", r) == None:
                g = r 
                loc = line.find(g)
            #if line[loc] in syms:
            #    print(re.findall("\d+", r))
                    
            
            if ll !=0 and ll != (len(file1)-1):
                if line[loc] != syms and file1[ll+1] and file1[ll-1]:
                    
                    pat1 = line[loc] in syms
                    pat2 = line[loc] in syms 
                    pat7 = (file1[ll+1])[loc+1] in syms
                    pat8 = (file1[ll-1])[loc-1] in syms
                    pat3 = (file1[ll+1])[loc+1] in syms
                    pat4 = (file1[ll-1])[loc-1] in syms
                    pat5 = (file1[ll+1])[loc+1] in syms
                    pat6 = (file1[ll-1])[loc-1] in syms

                    #if pat1 or pat2 or pat3 or pat4 or pat5 or pat6 or pat7 or pat8:
                        #print(re.findall("\d+", g))'''




    
    
    print(sum)

main()
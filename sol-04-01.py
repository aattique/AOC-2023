import math
from collections import defaultdict

def get_puzzle(path):
    with open(path) as f:
        return f.readlines()





def main():
    puzzle_path = "aoc-04-01.txt"
    file1 = get_puzzle(puzzle_path)
    
    points = 0
    score = 0
    sum1= 0
    pl = []
    cards2 = [1 for i in range(len(file1))]

    for a, b in enumerate(file1):
        cards = b.split(":")
        
        nums = cards[1].split("|")
        
        for m in nums[0].split():
            for n in nums[1].split():
                if m == n:
                    points += 1
              
        for i in range(points):
            cards2[a + i + 1] += cards2[a]
            
    

        pl.append((a, points))
        points = 0
        nums = []
       
    for a in pl:
        if a[1] != 0:
            
            score = math.pow(2, (a[1] - 1))
            sum1 += score
    
    

    print(sum(cards2))

   
            
    
    
    

        

    cards = [1] * len(file1)
    for i, line in enumerate(file1):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        
        for j in range(i + 1, min(i + 1 + n, len(line))):
            cards[j] += cards[i]
    #print(cards)
    
    req = sum(cards)
    #print(req)



main()
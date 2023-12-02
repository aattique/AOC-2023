import re

def get_puzzle(path):
    with open(path) as f:
        return f.readlines()

puzzle_path = "aoc-01-01.txt"
file1 = get_puzzle(puzzle_path)
count = 0
sum = 0
replacements=[("one", "o1e"),("two", "t2o"),("three", "th3ree"),("four", "fo4ur"),("five", "fi5ve"),("six", "si6x"),("seven", "sev7en"),("eight", "eig8ht"),("nine", "ni9ne")]


for line in file1:
    print(line)
    for pat,repl in replacements:
        line = re.sub(pat, repl, line)
    nums = re.findall("[0-9]", line)
    cal = int(nums[0] + nums[len(nums)-1])
    print(cal)
    sum += cal    

print(sum)
import re
import string


def get_puzzle(path):
    with open(path) as f:
        return f.readlines()

puzzle_path = "aoc-02-01.txt"
file1 = get_puzzle(puzzle_path)

sum = 0
sum2 = 0
rb = 0
bb = 0
gb = 0
gameid = 0
power = 0



for line in file1:
    game = line.split(":")
    gameidd = re.findall("\d+", game[0])
    
    for num, col in (re.findall("(\d+) (\w+)", line)):
        
        if col == 'red':
            if int(num) > rb:
                rb = int(num)
        
        if col == 'blue':
            if int(num) > bb:
                bb = int(num)
        
        if col == 'green':
            if int(num) > gb:
                gb = int(num)
        
    if rb <=12 and gb <= 13 and bb <=14:
        gameid = int(gameidd[0])
        print(gameid)
        sum += gameid
    power = rb * gb *bb
    rb,gb,bb = 0,0,0
    sum2 += power  

print(sum)
print(sum2)    


'''for num, col in (re.findall("(\d+) (red)", l)):
            print(num)    

        for num, col in (re.findall(" ([0-9]+) (blue)", l)):
            print(num)
        
        for num, col in (re.findall(" ([0-9]+) (green)", l)):
            print(num)'''
        
        
'''        if reds != []:
            count = (re.findall("\d+", reds[0]))
            print(count)
        if count != 0:
            if int(count[0]) > rb:
                rb = int(count[0])
                
            
        if blues != []:
            count = (re.findall("\d+", blues[0]))
            print(count)
        if count != 0:
            if int(count[0]) > bb:
                bb = int(count[0])
                
            
        if greens != []:
                count = (re.findall("\d+", greens[0]))
                print(count)
        if count != 0:
            if int(count[0]) > gb:
                gb = int(count[0])
                

        count = 0

        #if rb <=12 and gb <= 14 and bb <=13:'''

                
        



        

        

        #reds = (re.findall("\s\d+ red", l))
        #blues = re.findall(" [0-9]+ blue", l)
        #greens = re.findall(" [0-9]+ green", l)

        


'''if m[0].isdigit():
            mydict = {m[1]: int(m[0])}
        
        
        for key in mydict.keys():

            if key == 'red':
                if mydict[key] <= 12:
                    redb = True        
                else:        
                    redb = False
        
            if key == 'green':
                if mydict[key] <= 13:
                    greenb = True        
                else:        
                    greenb = False
        
            if key == 'blue':
                if mydict[key] <= 14:
                    blueb = True        
                else:        
                    blueb = False
                
            if redb and greenb and blueb:
                sum += int(game[0])   '''



























        #game = re.findall("[0-9]+", line[0])
'''if ";" in line:
        line = line.split(";")
        #line = [line[1]] 
       # dict4.update({"game": game})'''
    #print(line)
    


''' i = 0
    for reqn in x:
        print(reqn)
        for num in range(len(reqn)):
            patt = re.compile("\d{2}")
            result = patt.findall(reqn[num])
            if result != []:
                print(result)'''
            
            

    
    ### append to red, greed, and blue lists to make some functions work
    #    dict1.update({"red": x})
     #   dict2.update({"green": y})
      #  dict3.update({"blue": z})
    

#print(dict4)
'''for x in range(len(red)):
    for calc in red[x]:
        calc = re.findall("\d+", calc)
        for cal in calc:
            if int(cal) <= 12:
                indexes.append(x)

indexesr = list(dict.fromkeys(indexes))

for x in indexesr:
    for calc in green[x]:
        print(green[x])
        calc = re.findall("\d+", calc)
        for cal in calc:
            if int(cal) <= 13:
                indexesg.append(x)
indexesgg = list(dict.fromkeys(indexesg))


for x in indexesgg:
    for calc in blue[x]:
        calc = re.findall("\d+", calc)
        for cal in calc:
            if int(cal) <= 14:
                indexesb.append(x)
indexesbb = list(dict.fromkeys(indexesb))
print(indexesbb)

for x in indexesbb:
    sum += x
print(sum)'''




            
    
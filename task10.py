
def count_valleys(n, steps):
    num_valleys = 0        
    level = 0              
    for d in steps:
        if d == 'U':       
            level += 1
        else:           
            if level == 0:
                num_valleys += 1
            level -= 1
    return num_valleys
 
n = int(input().strip())
steps = input().strip()
count_valleys(n, steps)
print(count_valleys(n, steps))

    
/\      /\
  \    /
   \/\/

UDDDUDUUUD
12
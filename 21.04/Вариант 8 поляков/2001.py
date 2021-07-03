import itertools 
  
permutations = set(itertools.permutations('КАБАЛА'))
permutations = map(lambda x: ''.join(x), permutations)  
count=0 
for word in permutations: 
    if word.find('АА')==-1: 
        count+=1 
        #print(word) 
print(count)

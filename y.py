name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lt=dict()

for lines in handle:
    line=lines.rstrip()
    if line.startswith('From'):
        line=line.split()
        if len(line)>4:
         word=line[5]
         word=word[0:2]
         ans=word[0]
         lt[ans]=lt.get(ans,0)+1
tup=list()
sorted(lt.items())
for k,v in lt.items():
    tup.append((v,k))
tup.sort()
for k,v in tup:
     if v>0: print(k,v)
        
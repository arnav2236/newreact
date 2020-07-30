# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# lt=dict()
# for line in handle:
#     line=line.strip()
#     if line.startswith('From'):
#         words=line.split()
#         print(words)
#         try:
# 			alpha=words[5]
#             alpha=alpha.split(':')
#        		lt[alpha[0]]=lt.get(alpha[0],0)+1
#         except:
#             continue
        
# for k,v in lt.items():
#    if v>0:
#         print(k,v)
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lt=dict()
s={'00:','01:','02:','03:','04:','05:','06:','07:','08:','09:','10:','11:','12:','13:','14:','15:','16:','17:'}
 
for i in range(11,24):
    s.append(i+':');
    
print (s)
#    for line in handle:
#     line=line.strip()
#     if line.startswith('From'):
#         words=line.split()
#         for word in words:
            
# for k,v in lt.items():
#    if v>0:
#         print(k,v)

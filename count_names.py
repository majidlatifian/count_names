n=int(input())
counter={}
for i in range(0 , n):
  vurudi=input()
  if vurudi in counter:
    counter[vurudi]+=1
  else:
    counter[vurudi]=1
sorted_dict = dict(sorted(list(counter.items())))
for name, count in sorted_dict.items():
  print('%s %s'%(name , count))
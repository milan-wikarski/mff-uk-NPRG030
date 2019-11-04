longestlist = []
longestofthelongest = []
tempindex = 0
temp = 0
j = 0
listofnums =[]
num = 0while num != -1:
   num = int(input())
   listofnums.append(num)for i in listofnums:
   if i > temp:
       if  tempindex == listofnums.index(i):
           longestlist.append(i)
       temp = i
   else:
       longestlist = []
       longestlist.append(i)
   tempindex = listofnums.index(i) + 1    longestofthelongest.append(longestlist)longestofthelongest.sort(key = len)
for j in longestofthelongest[-1]:
   print(j)

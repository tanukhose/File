# Aapne jo pichle question mein (Question 1) file download kari hai, 
# usko read karke usme number of lines count kar ke print karein. 
# Aapne sirf uss file ki number of lines Count karne ka code likhna hai.

# Hint: Har \n ke baad nayi line shuru hoti hai. Aap yeh use kar ke nayi 
# line ka ko pehchan sakte ho.

o=open("people1.txt","r")
count=0
for i in (o):
    count+=1
    t=o.read()
print(t)
print(count)
o.close()

# o=open("people1.txt","r")
# t=o.read()
# print(t)
# o.close()

# o=open("people1.txt")
# count=0
# for i in (o):
#     count+=1
# print(count)
# o.close()
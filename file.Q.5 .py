# name='''rishabh - meerut
# imtiyaz - delhi
# nilima - cochin
# rati - shimla
# ayishah - delhi
# raghu - shimla
# naseer - kanpur
# karthikeyan - delhi
# salma - jaipur
# pankaj - delhi
# brijesh - delhi
# govind - delhi
# puneet - shimla
# tanuja - Ahmednagar
# siddhi - delhi
# suman - jaipur
# rajeev - shimla
# mohinder - delhi
# rajendra - jaipur
# priyanka - shimla
# neela - delhi
# sashi - jaipur
# sarika - delhi
# deepti - shimla
# harshad - delhi
# trishna - raipur
# pradeep - jaipur
# sekhar - delhi
# nand - delhi
# anoop - delhi
# balwinder - tokyo'''

# o=open("listofdelhi.txt","w")
# o.write(name)
# o.close()


b=open("listofdelhi.txt","r")
f=b.read().splitlines()
for i in f:
    if 'delhi' in i:
        f=open("*delhi.txt",'a')
        f.write(i)
        f.write('\n')
        f.close()
    if 'shimla' in i:
        f=open("*shimla.txt","a")
        f.write(i)
        f.write('\n')
        f.close()
    if 'delhi'not in i and 'shimla' not in i:
        f=open("*other states.txt","a")
        f.write(i)
        f.write('\n')
        f.close() 


    


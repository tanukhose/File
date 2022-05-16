# files-question3

# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein
#  nayi line mein daalo. Aapki list yeh rahi:
# Code Example

# list = ["Kotak ", "HDFC ", "RBL ", "SBI ", "Bank of Baroda"]
# obj=open("Question3.txt","w")
# for i in range(len(list)):
#     a=list[i]
#     obj.write(a)
# obj.close()

# ob=open("Question3.txt","w")
# ob.write("Kotak\nHDFC\nRBL\nSBI\nBank of Baroda")
o=open("Question3.txt","r")
a=o.read()
print(a)
o.close()
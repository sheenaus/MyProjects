import random
import os

cwd=os.getcwd()
afile = open(cwd +"\Random.txt", "w" )
    #for i in range(input('How many random numbers?: ')):
for i in range(100000000000):
    line = random.randint(1, 100000)
    afile.write(str(line)+'\n')
afile.close()
#print("\nReading the file now." )
#afile = open(cwd+"\Random.txt", "r")
#print(afile.read())
#afile.close()

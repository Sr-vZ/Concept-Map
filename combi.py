import pandas as pd
from itertools import combinations

with open("AttributeList.txt", "r") as f:
    attrblist = []
    # for item in f:
    #     number = 0
    #     while number < 5:
    #         attrblist.append(item + str(number))
    #         number += 1
    # print(attrblist)
    attrblist = f.readlines()

print(len(attrblist))


outF = open("myOutFile.txt", "w")
# Get all combinations of attrblist
# and length 4
comb = combinations(attrblist, 4)
# print(list(comb))
# Print the obtained combinations
for i in list(comb):
    outF.write(str(i))
    outF.write("\n")
    print (i)
outF.close()

# outF = open("myOutFile.txt", "w")
# outF.writelines(list(comb))
# outF.close()
# for line in list(comb):
#   # write line to output file
#   outF.write(line)
#   outF.write("\n")
# outF.close()

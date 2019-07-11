

with open('myOutFile1.txt') as f:
  lineList = f.readlines()

# print(lineList[1].strip().split(','))

with open('sampledata.txt') as f:
  temp = f.readlines()

# print(temp[5].split('\t')[1].strip().split(','))
# lineList = lineList[0:100]
# temp = temp[0:100]

finalCount =[]

for lines in lineList:
    attr = lines.strip().split(',')
    attr = map(str.strip, attr)
    # print(attr)
    counter = 0
    for data in temp:
        datalist = data.split('\t')[1].strip().split(',')
        if(all(x in datalist for x in attr)):
            counter = counter + 1
    if counter>0:
        finalCount.append([counter,attr])

# print(str(list(finalCount)[0:5]))
sortedfinalCount = finalCount

# print(sortedfinalCount)
for i in list(finalCount):
    print(str(i))


# outF = open("top40count.txt", "w")
# for i in list(sortedfinalCount):
#     outF.write(str(i))
#     outF.write("\n")
# outF.close()

# outF = open("finalcount.txt", "w")
# for i in list(finalCount):
#     outF.write(str(i))
#     outF.write("\n")
# outF.close()

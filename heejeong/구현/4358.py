import sys
input = sys.stdin.readline

data = {}
while True:
    tree = input().rstrip()
    # print(tree)
    if tree == '':
        break
    if tree in data.keys():
        data[tree] += 1
    else:
        data[tree] = 1
    # print("키: ", tree, "값: ", data[tree] )
sortedData = sorted(data.keys())
sum_value = sum(data.values())
for t in sortedData:
    print('%s %.4f' %(t, data[t]/sum_value*100))
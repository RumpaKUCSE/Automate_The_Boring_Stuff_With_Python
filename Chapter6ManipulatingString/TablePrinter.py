def printTable(data):
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].ljust(15),end = '')
        print()



tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

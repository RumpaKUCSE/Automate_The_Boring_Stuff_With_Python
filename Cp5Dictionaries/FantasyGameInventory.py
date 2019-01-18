def displayInventory(data):
    print('Inventory:')
    totalStuff = 0
    for i, j in data.items():
        print(str(j)+' '+ i)
        totalStuff = totalStuff + j
    print('Total number of items: '+ str(totalStuff))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print(displayInventory(stuff))
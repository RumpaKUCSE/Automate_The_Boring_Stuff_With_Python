def displayInventory(data):
    print('Inventory:')
    totalStuff = 0
    for i, j in data.items():
        print(str(j)+' '+ i)
        totalStuff = totalStuff + j
    print('Total number of items: '+ str(totalStuff))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i]+1
        else:
            inventory[i] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
# print(inv)
displayInventory(inv)
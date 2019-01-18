#section
def hellow():
    print('Hi,')
    print('I am in hellow function')
hellow()

#section
def fun(name):
    print('Hi, ' + name)

fun('Rumpa Paul')
'''
def spam():
    agg = 99
    bacon()
    print(agg)

def bacon():
    hash = 200
    agg = 0
    
spam()


#section
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
'''
#section
def spam():
     global eggs
     eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
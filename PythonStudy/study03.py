message = input("Tell me something:")
print(message)

age = input("How old are you? ")
age = int(age)
print(age)

def multiArgs(*names):
    for name in names:
        print(name)

multiArgs('xudasong','zhangsan','lisi')
multiArgs('123')

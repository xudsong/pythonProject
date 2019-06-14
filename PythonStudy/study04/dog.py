class Dog(object):

    """初始化方法"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """蹲下"""
    def sit(self):
        print(self.name.title() + " is now sitting.")

    """打滚"""
    def roll_over(self):
        print(self.name.title() + " rolled over!")

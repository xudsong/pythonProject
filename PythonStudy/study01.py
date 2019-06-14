moves = ["move1","move2",["move11","move21"]]

# 导入模块
import neast
neast.print_lol(moves)

# def创建函数
def print_lol(the_list):
    for the_list_item in the_list:
        if isinstance(the_list_item, list):
            print_lol(the_list_item)
        else:
            print(the_list_item)

# 函数调用
print_lol(moves)
print("函数调用结束。。。。")

# for循环
for each_item in moves:
    if isinstance(each_item,list):
        for ineach_item in each_item:
            print(ineach_item)
    else:
        print(each_item)

# while循环

"""
多行注释
使用这个注释符
"""
count = 0
while count<len(moves):
    print(moves[count])
    count=count+1

# isinstance检查是否为某个特定类型的数据(如下面的list列表)
result = isinstance(moves, list)
print(result)

# range()内置函数使用
for num in range(5):
    print(num)
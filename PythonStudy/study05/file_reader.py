"""读取文件数据"""

with open('text_files/pi_digits.txt') as file_object:
    # contents = file_object.read()
    """删除字符串末尾的空白"""
    # print(contents.rstrip())

    """逐行读取"""
    # for line in file_object:
    #     print(line.rstrip())

    """读取文件各行内容并存于列表"""
    lines = file_object.readlines()

"""打印列表内容"""
for line in lines:
    print(line.rstrip())
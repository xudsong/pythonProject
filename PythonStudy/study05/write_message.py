"""写入文件内容"""

filename = 'text_files/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
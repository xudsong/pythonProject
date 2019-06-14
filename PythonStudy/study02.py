# 文件与异常处理
import os
import django


"""当前的工作路径"""
curr_path = os.getcwd()
print(curr_path)

"""切换到指定路径"""
os.chdir('../doc')
chd_path = os.getcwd()
print(chd_path)

"""打开数据文件读取数据"""
data = open('sketch.txt')
# 返回文件起始位置
line_num = data.seek(0)
# 获取文件一行数据
data.readline()
# 读取文件每一行数据
for each_line in data:
    print(each_line,end='')
#关闭文件处理
data.close()
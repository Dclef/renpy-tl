import os

# 输入要重命名的目录
path = input('请输入要重命名的目录：')
# 获取目录下的所有文件
files = os.listdir(path)
# 去掉x-前缀并覆盖原文件
for file in files:
    if file.startswith('x-'):
        new_file = file.replace('x-', '')
        os.rename(path + '/' + file, path + '/' + new_file)
        print('重命名成功：', file, '-->', new_file)
# 按任意键结束
input('按任意键结束')
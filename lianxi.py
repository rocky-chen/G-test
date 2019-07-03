# file=open('./1.txt','a',encoding='utf-8')
# file.write('难念的经')
# file.close()

# file1=open('./1.txt','r',encoding='utf-8')
# content=file1.read()
# print(content)
# file1.close()
# import os

# list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

# with open ('poem.txt','r') as f:
#     lines = f.readlines()

# with open('poem_new.txt','w') as new:
#     for line in lines:
#         if line in list_test:
#             new.write('____________。\n')
#         else:
#             new.write(line)

# os.replace('poem_new.txt', 'poem.txt')
import os

with open ('test.txt','r') as f:
    lines = f.readlines()

with open('test_new.txt','w') as new:  # 新建一个文档
    for line in lines:
        if line not in ['0\n','1\n']:
            new.write(line)     

# 可以先运行一次代码，然后，再将下面代码的注释取消，再运行一次。
os.replace('test_new.txt', 'test.txt')  # 语法：os.replace(file1,file2)，将file1重命名为file2，将其替代。

# 请你根据上面的方法，将之前的代码改为用模块 os 实现（可选文档poem2）。
# 在改代码之前，可以先将上面的代码注释，然后取消下面代码的注释。

list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

with open ('poem2.txt','r') as f:
     lines = f.readlines()

with open('poem2.txt','w') as new:
     for line in lines:
         if line in list_test:
             new.write('____________。\n')
         else:
             new.write(line)
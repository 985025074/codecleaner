import re
import os
#  learn *args and *kwargs in python.
def write_to_new_file(code_path, new_code):
    # 分离文件路径和文件名
    base_name, ext = os.path.splitext(code_path)
    # 在文件名中间添加 "_new"
    new_file_name = base_name + '_new' + ext
    # 写入新文件
    with open(new_file_name, 'w') as f:
        f.write(new_code)
def overwrite_file(code_path, new_code):
    with open(code_path, 'w') as f:
        f.write(new_code)
def replace_all(pattern, replacement, code,code_path,create_new_file=False):
    pass
def replace_all(pattern, replacement, code,code_path,create_new_file=False):
    print("code:\n", code)
    print("-----------------\n")
    new_code = re.sub(pattern, replacement, code)
    print("new_code:\n", new_code)
    print("-----------------\n")
    result = input("Substitute? [Y/n]")
    if result == "Y" or result == "y":
       if create_new_file:
           write_to_new_file(code_path, new_code)
       else:
           overwrite_file(code_path, new_code)
    else:
        print("No substitution made.")
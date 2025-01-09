import re
import os
from colorama import init, Fore, Style
# 初始化 colorama
init()
def replace_line_by_line(pattern, replacement, code, context_lines=2):
    """
    Process code line by line, apply regex substitution, and ask the user for confirmation on each line.
    Print the modified line along with a specified number of surrounding lines.
    """
    lines = code.splitlines()  # 将代码按行分割
    modified_lines = []  # 存储修改后的行
    flag = False  # 标记是否有发生变化

    for line_num, line in enumerate(lines):
        new_line = re.sub(pattern, replacement, line)  # 对当前行应用替换

        if new_line != line:  # 仅在发生变化时提示用户
        # 打印上下文信息
            start = max(0, line_num - context_lines)  # 确定起始行
            end = min(len(lines), line_num + context_lines + 1)  # 确定结束行
            print(f"\nContext around line {line_num + 1}:")
            for i in range(start, end):
                prefix = Fore.RED + ">> " if i == line_num else "   "  # 当前行加标记
                print(f"{prefix}Line {i + 1}: {lines[i]}" + Style.RESET_ALL)        
            print("-----------------\n")
            print("Modified line:")
            print(new_line)
            print("-----------------\n")
            result = input(f"Substitute line {line_num + 1}? [Y/n]: ")
            if result.lower() == "y":
                flag = True  # 标记发生了变化
                if new_line == "":  # 若替换后为空行，则不添加到列表中
                    continue
                modified_lines.append(new_line)  # 使用替换后的行
            else:
                modified_lines.append(line)  # 保留原始行
        else:
            modified_lines.append(line)  # 无变化时直接添加

    if not flag:  # 无变化时提示用户
        return None
    return "\n".join(modified_lines)  # 将修改后的行重新组合为字符串






def replace_all(pattern, replacement, code) -> str | None:
    """
    Apply regex substitution to the entire code, and directly highlight removed lines
    in the `Original code` section.
    """
    print("Original code:")
    new_code = re.sub(pattern, replacement, code)
    
    # 将代码按行处理
    code_lines = code.splitlines()
    new_code_lines = new_code.splitlines()

    # 打印 `Original code` 高亮被删除的行
    for line in code_lines:
        if line not in new_code_lines:
            print(Fore.RED + line + Style.RESET_ALL)  # 红色高亮显示被移除的行
        else:
            print(line)  # 正常显示未被移除的行
    
    print("-----------------\n")
    print("Modified code:")
    print(new_code)
    print("-----------------\n")
    
    # 用户确认替换
    result = input("Substitute? [Y/n]: ")
    if result.lower() == "y":
        return new_code
    else:
        return None

def replace_logic(pattern, replacement, code,code_path,create_new_file=False,line_by_line=False):
    new_code = None
    # first: logic of line by line replacement or all replacement:
    if line_by_line:
        new_code = replace_line_by_line(pattern, replacement, code)
    else:
        new_code = replace_all(pattern, replacement, code)
    
    # second step: write to new file or overwrite the original file:

    if new_code is None:
        print("No replacement made.")
    else:
        if create_new_file:
            print("New file created.")
            write_to_new_file(code_path, new_code)
        else:
            print("Original file overwritten.")
            overwrite_file(code_path, new_code)
    return

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
        

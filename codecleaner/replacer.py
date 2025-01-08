import re
import os


def replacer(code_path, pattern, replacement,create_new_file=False,line_by_line=False):
    try:
        with open(code_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f" {code_path} is not found。")
        return 
    # TODO: more error checks
    # TODO :replace logic here

    

    
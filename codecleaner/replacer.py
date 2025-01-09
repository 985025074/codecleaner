import re
import os
# relative import for normal files
from .replace_method import replace_logic
#注释
def replacer(code_path, pattern, replacement,create_new_file=False,line_by_line=False):
    """
    Replace code_path with the new code.
    ** code_path **: the path of the code file to be replaced
    ** pattern **: the pattern to be replaced
    ** replacement **: the replacement string
    ** create_new_file **: whether to create a new file or replace the original file
    """
    try:
        with open(code_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f" {code_path} is not found。")
        return 
    
    # TODO: more error checks
    # TODO :replace logic here
    replace_logic(pattern, replacement, code,code_path,create_new_file,line_by_line)

    

    
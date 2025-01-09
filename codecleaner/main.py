#!/usr/bin/python3
import os
# global run,so we use absolute import here
from codecleaner.args_handler import parse_args,tactics,built_in_option 
from codecleaner.replacer import replacer

def choose_the_first_option(args:dict)->tuple[str,str]|None:
    for key,value in args: 
        if key not in built_in_option and value!= None:
            return (key,value)
    return None
def parse_args_wrapper()->tuple[list,dict]:
    # may be there is a better way to do the following work... 
    # but i forgot it for i have do alot with otehr languages
    args_space = parse_args()
    args_dict = vars(args_space)
    args_list = list(args_dict.items()) 
    return args_list,args_dict
def main():
    # parse args
    args_list,args_dict = parse_args_wrapper()
    # here we get the what we need to do
    # TODO : support multi options? Now we just support one option (one tactic)
    first_option = choose_the_first_option(args_list)
    if first_option == None:
        print("No tactic or file selected, please select a tactic")
        return
    # every option is composed of a dict like {}
    fisrt_file_path = first_option[1]
    first_file_ext = first_option[0]
    final_tactics = tactics()[first_file_ext]
    # print(final_tactics)
    # clean logic here  
    replacer(fisrt_file_path, final_tactics["pattern"], final_tactics["target"]
             ,create_new_file=args_dict["n"],
             line_by_line=args_dict["l"])
if __name__ == "__main__":
    main()



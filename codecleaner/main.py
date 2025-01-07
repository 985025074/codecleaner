#!/usr/bin/python3
import os
from codecleaner.args_handler import parse_args,tactics 
from codecleaner.replacer import replacer
def main():
    args = parse_args()
    args = vars(args)
    first_option = list(args.keys())[0]
    fisrt_file_path = args[first_option]
    final_tactics = tactics()[first_option]
    print(final_tactics)
    replacer(fisrt_file_path, final_tactics["pattern"], final_tactics["target"])
main()



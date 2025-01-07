import re

def replacer(code_path, pattern, replacement):
    try:
        with open(code_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f" {code_path} is not found。")
        return 
    # TODO: more error checks
    print("code:\n", code)
    print("-----------------\n")
    new_code = re.sub(pattern, replacement, code)
    print("new_code:\n", new_code)
    print("-----------------\n")
    result = input("Substitute? [Y/n]")
    if result == "Y" or result == "y":
        with open(code_path, 'w') as f:
            f.write(new_code)
    else:
        print("No substitution made.")
    

    
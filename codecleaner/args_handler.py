import argparse
import json
import os 
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.json')
# mention: when you add inner argument, add it to built_in_option list
built_in_option = ["n","l"]

with open(config_path, 'r') as f:
    config = json.load(f)
def parse_args():
    parser = argparse.ArgumentParser(description=config['description']) 
    # no parameter needed for creating new file
    parser.add_argument("-n", action="store_true", help=config["newfile_help"])
    parser.add_argument("-l", action="store_true", help=config["line_help"])
    for key,value in config["tactics"].items():
        parser.add_argument(f"-{key}",f"--{key}",nargs="?",type=str, help=value["description"])
    return parser.parse_args()
def tactics():
    return config["tactics"]
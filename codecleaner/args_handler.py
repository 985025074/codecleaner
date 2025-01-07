import argparse
import json
with open('config.json', 'r') as f:
    config = json.load(f)
def parse_args():
    parser = argparse.ArgumentParser(description=config['description']) 
    for key,value in config["tactics"].items():
        parser.add_argument(f"--{key}",nargs="?",type=str, help=value["description"])
    return parser.parse_args()
def tactics():
    return config["tactics"]
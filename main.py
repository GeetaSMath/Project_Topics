# read json file using nested dictionary
import json
with open("data.json") as access_json:
    read_content = json.load(access_json)
    print(read_content)

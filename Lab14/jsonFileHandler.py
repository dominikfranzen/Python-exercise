import json

def readJsonFile(filename):
    data = ""
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    except IOError:
        print("Could not read file")
    return data



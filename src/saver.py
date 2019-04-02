import json

def save_json_file(data):
    RESULTS_PATH = "../results.json"
    with open(RESULTS_PATH, 'w') as outfile:
        json.dump(data, outfile)
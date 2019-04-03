import json
import os

def save_json_file(data):
	RESULT_DIRECTORY = "./../result"
	RESULTS_PATH = RESULT_DIRECTORY + "/results.json"

	if not os.path.exists(RESULT_DIRECTORY):
		os.makedirs(RESULT_DIRECTORY)
		
	with open(RESULTS_PATH, 'w') as outfile:
		json.dump(data, outfile)
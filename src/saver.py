import json
import os

def save_json_file(data):
	'''Save metrics in json file.'''
	
	RESULT_DIRECTORY = "./../results"
	RESULTS_PATH = RESULT_DIRECTORY + "/result.json"

	if not os.path.exists(RESULT_DIRECTORY):
		os.makedirs(RESULT_DIRECTORY)
		
	with open(RESULTS_PATH, 'w') as outfile:
		json.dump(data, outfile)
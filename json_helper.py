import pandas as pd
import os
import json


def read_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def read_all_json_files(JSON_ROOT):
    maindf = pd.DataFrame()
    for path, subdirs, files in os.walk(JSON_ROOT):
        for name in files:
            if name.endswith(".json"):
                json_content = read_json(os.path.join(path, name))
                df = pd.DataFrame(json_content['results'])
                df['source'] = os.path.join(path,name)
                maindf = maindf.append(df, ignore_index=True)
    return maindf



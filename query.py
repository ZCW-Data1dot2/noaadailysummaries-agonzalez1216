import requests
import json
import time

i = 0
offset = 1
limit = 1000
data_set_id = 'GHCND'
start_date = '2018-12-01'
end_date = '2018-12-31'
location_id = 'FIPS:10003'
headers = {'Token': 'iPUFLyvvyzixkBcMRarLLeoLASMlWkEE'
           }
payload = {'limit': limit,
           'offset': offset,
           'datasetid': data_set_id,
           'startdate': start_date,
           'enddate': end_date,
           'locationid': location_id}
data_set_name = 'data'
r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/{data_set_name}', headers=headers, params=payload)
r_dict = r.json()
total_results = r_dict['metadata']['resultset']['count']
r_str = json.dumps(r_dict, indent=4)
while offset <= total_results:
    time.sleep(.75)
    with open(f'daily_summaries_FIPS10003_jan_2018_{i}.json', 'w') as outfile:
        outfile.write(r_str)
    i += 1
    offset = offset + limit
    payload['offset'] = offset
    r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/{data_set_name}', headers=headers, params=payload)
    r_dict = r.json()
    r_str = json.dumps(r_dict, indent=4)



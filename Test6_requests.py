# Didn't really test this much

# =========================
# Sorting out URLs
# =========================
import json


def read_config_file(configPath):
    print("Config Path: %s" % str(configPath))
    with open(configPath) as data_file:
        data = json.load(data_file)

        return data

my_data = read_config_file('FilePaths.json')

print("AndroZoo URL: {}".format(my_data['androzoo_url']))
print("Local Path: {}".format(my_data['local_path']))
print("Other URL: {}".format(my_data['url']))


#-------------------------------
import requests
import csv
import os

temp_file_name = 'temp_csv.csv'
url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
download = requests.get(url)

with open(temp_file_name, 'w') as temp_file:
    temp_file.writelines(download.content)

with open(temp_file_name, 'rU') as temp_file:
    csv_reader = csv.reader(temp_file, dialect=csv.excel_tab)
    for line in csv_reader:
        print(line)

# delete the temp file after process
os.remove(temp_file_name)
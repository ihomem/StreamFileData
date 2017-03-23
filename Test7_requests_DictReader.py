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



#---------------------
import csv
import requests

response = requests.get('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
reader = csv.DictReader(response.iter_lines())
for record in reader:
    print(record)
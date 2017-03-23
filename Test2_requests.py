# worked initially ... but had a bug to do with iterators / generators
# Still haven't fully understood what's going wrong
# PRobably suffers the saem problem of having to download the entire file first

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


#---------------------------
# WORKS
#-----------
import csv
import requests

CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
#CSV_URL = my_data['androzoo_url']

def loop_through_file(file):
    for row in file:
        yield row

#def get_stuff():
with requests.Session() as s:
    download = s.get(CSV_URL, stream=True)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    #my_list = list(cr)
    #for row in cr: #my_list:
     #   print(row)
        #yield row
    print(loop_through_file(cr))
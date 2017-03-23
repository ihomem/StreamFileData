# Seems to work but is extremely slow because it needs to DOWNLOAD the entire file first
# If the file is large it will take a long time
# Not an appropriate solution ... for now

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


#-----------------------
# Also works
#----------------------
import csv
import requests

#CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
CSV_URL = my_data['androzoo_url']

with requests.Session() as s:
    download = s.get(CSV_URL)

    line_iterator = (x.decode('utf-8') for x in download.iter_lines(decode_unicode=True))
    print('Here')
    cr = csv.reader(line_iterator, delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

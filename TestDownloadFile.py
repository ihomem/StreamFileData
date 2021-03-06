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

import csv
import requests
from contextlib import closing
from itertools import islice
#import codecs

#CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

#url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
#url = "http://download-and-process-csv-efficiently/python.csv"
url = my_data['androzoo_url']

with closing(requests.get(url, stream=True)) as r:

    #reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
    #reader = csv.reader(codecs.iterdecode(r.iter_lines(decode_unicode=True), 'utf-8'), delimiter=',', quotechar='"')
    #reader = csv.reader(codecs.iterdecode(r.iter_lines(decode_unicode=True), 'utf-8')) # works only with samplecsvs url
    reader = csv.reader(r.iter_lines(decode_unicode=True))  # Works only with AndroZoo URL
    # for row in reader:
    #     print(row)

    for row in islice(reader, 10):  # files are iterable
        print(row)













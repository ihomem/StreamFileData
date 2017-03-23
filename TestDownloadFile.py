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

# import csv
# import requests
# from contextlib import closing
# import codecs
#
# #CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
#
# url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# #url = "http://download-and-process-csv-efficiently/python.csv"
# #url = my_data['androzoo_url']
#
# with closing(requests.get(url, stream=True)) as r:
#
#     #reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
#     #reader = csv.reader(codecs.iterdecode(r.iter_lines(decode_unicode=True), 'utf-8'), delimiter=',', quotechar='"')
#     reader = csv.reader(codecs.iterdecode(r.iter_lines(decode_unicode=True), 'utf-8'))
#     for row in reader:
#         print(row)

#---------------------------#
# import csv
# import urllib.request
# import codecs
#
# url = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
# ftpstream = urllib.request.urlopen(url)
# csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
# for line in csvfile:
#     print(line)  # do something with line

#---------------------------
# WORKS
#-----------
# import csv
# import requests
#
# CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# #CSV_URL = my_data['androzoo_url']
#
# def loop_through_file(file):
#     for row in file:
#         yield row
#
# #def get_stuff():
# with requests.Session() as s:
#     download = s.get(CSV_URL, stream=True)
#
#     decoded_content = download.content.decode('utf-8')
#
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     #my_list = list(cr)
#     #for row in cr: #my_list:
#      #   print(row)
#         #yield row
#     print(loop_through_file(cr))

#-----------------------
# Also works
#----------------------
# import csv
# import requests
#
# #CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# CSV_URL = my_data['androzoo_url']
#
# with requests.Session() as s:
#     download = s.get(CSV_URL)
#
#     line_iterator = (x.decode('utf-8') for x in download.iter_lines(decode_unicode=True))
#     print('Here')
#     cr = csv.reader(line_iterator, delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)


#---------------------
# import csv
# import requests
#
# response = requests.get('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
# reader = csv.DictReader(response.iter_lines())
# for record in reader:
#     print(record)

#-------------------------------
# import requests
# import csv
# import os
#
# temp_file_name = 'temp_csv.csv'
# url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# download = requests.get(url)
#
# with open(temp_file_name, 'w') as temp_file:
#     temp_file.writelines(download.content)
#
# with open(temp_file_name, 'rU') as temp_file:
#     csv_reader = csv.reader(temp_file, dialect=csv.excel_tab)
#     for line in csv_reader:
#         print(line)
#
# # delete the temp file after process
# os.remove(temp_file_name)


#--------------------
#Also works, but requires some tweaking and is slow over the network
#---------------------
# import pandas as pd
#
# # chunksize = 10 ** 6
# chunksize = 10
# filename = my_data['local_path']
# #filename = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# #filename = my_data['androzoo_url']
# #df_chunk = pd.read_csv(filename, chunksize=chunksize)
# #for line in df_chunk:
# #    print(line)
#
# df_chunk = pd.read_csv(filename, nrows=10)
# #setting screen width for pandas
# desired_width = 320
# pd.set_option('display.width', desired_width)
#
# print(df_chunk)
# # print(df_chunk, end='')


#---------------
# WORKS Best ... probably
#----------------
import urllib.request
from itertools import islice

#url = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
url = my_data['androzoo_url']
data = urllib.request.urlopen(url) # it's a file like object and works just like a file
# for line in data: # files are iterable
#     print(line)

# For reading the first 10 items
# for idx,line in enumerate(data): # files are iterable
#     if idx < 10:
#         print(line)
#     else:
#         break

for line in islice(data, 10): # files are iterable
    print(line)

print("reached here")

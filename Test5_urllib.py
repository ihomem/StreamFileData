# This seems to work ... not sure whether it is optimal
# Need to check whether urllib is streaming the data?? What does that even mean?
# IT seems to be streaming ... but not entirely sure
# GOOD SOLUTION

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



#---------------
# WORKS Best ... probably!
#----------------
import urllib.request
from itertools import islice

#url = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
#url = my_data['url']
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


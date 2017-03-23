# This seems to work, but is slow over the network because it
# needs to load the entire file first before outputing anything

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


#--------------------
#Also works, but requires some tweaking and is slow over the network
#---------------------
import pandas as pd

# chunksize = 10 ** 6
chunksize = 10
filename = my_data['local_path']
#filename = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
#filename = my_data['androzoo_url']
#df_chunk = pd.read_csv(filename, chunksize=chunksize)
#for line in df_chunk:
#    print(line)

df_chunk = pd.read_csv(filename, nrows=10)
#setting screen width for pandas
desired_width = 320
pd.set_option('display.width', desired_width)

print(df_chunk)
# print(df_chunk, end='')

from multiprocessing.spawn import import_main_path
import requests
import pprint
import json
import csv

from requests.models import default_hooks
try:
     import xmlrpclib
except ImportError:
     import xmlrpc.client as xmlrpclib

client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
# get a list of package names
packages = client.list_packages()

for i in packages:
     q = requests.get(f'https://pypi.python.org/pypi/{i}/json')
     try:          
          jsonData = q.json()
          # print(jsonData)
          names = jsonData['info']['name'] 
          des = jsonData['info']['description']
          url = jsonData['info']['package_url']
          keyw = jsonData['info']['keywords']

          with open("Data.csv","a", newline='') as file:
               csv_file = csv.writer(file)
               csv_file.writerow([names,des,url,keyw])
     except:
          print("Error")

print("Done")

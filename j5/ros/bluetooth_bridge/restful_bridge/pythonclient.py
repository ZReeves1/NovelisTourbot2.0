#Spencer Waguespack
#python client example
#this prints the data from the url to the console
import requests

#url to get data from
url = 'http://localhost:8080'

#start a new sesion
s = requests.Session()

#continously check for new data at url
while True:
    r = s.get(url)

    print(r.text)




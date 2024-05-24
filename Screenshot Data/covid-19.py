import requests   #It will send request to website and get official data from there.
from win10toast import ToastNotifier   # it will help us to show the notification in the notification area in the windows 10.
import json  # it is an api that retens the data.
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nrecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=20)
        time.sleep(60)

update()
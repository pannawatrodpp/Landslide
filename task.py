import requests

def Train():
    # API
    url = "http://ews1.dwr.go.th/website/webservice/rain_daily.php?uid=landslide2022cm&upass=cicecmu2020&dmode=2&dtype=2&ondate=dd/mm/yyyy"
    req = requests.get(url).json()
    for i in req['station']:
        print(i['id'])
    # ANN

Train()
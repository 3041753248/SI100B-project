#preparations
import requests
import json
import pandas as pd
with open('../data/state_name.json') as q:
    q = json.load(q)
w = list(q.keys())
#cases_by_Fanzx
for i in range(0, 52):
    wangzhi = "https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/cases/" + w[i] + ".json"
    qingqiu = requests.get(wangzhi)
    wenben = qingqiu.text
    jiema = json.loads(wenben)
    date = list(jiema.keys())
    cases = jiema.values()
    table = pd.DataFrame(cases,date)
    table.index.name = 'date'
    name = str(q.get(w[i])) + '_cases.csv'
    table.to_csv(name)
#deaths_by_Liuzh
for i in range(0,52):
    URL='https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/deaths/'+w[i]+'.json'
    URL_get=requests.get(URL)
    URL_js=URL_get.text
    URL_dic=json.loads(URL_js)
    date=URL_dic.keys()
    deaths=URL_dic.values()
    date_list=list(date)
    res=pd.DataFrame(deaths,date_list)
    res.index.name='date'
    res.rename(columns={'raw_positives': 'deaths'})
    filename_prefix=q.get(w[i])
    filename=filename_prefix+'_deaths.csv'
    res.to_csv(filename)
#vaccines_by_Dengzq
for i in range(0, 52):
    a1 = requests.get("https://jhucoronavirus.azureedge.net/api/v1/timeseries/us/vaccines/" + w[i] + ".json")
    a2 = json.loads(a1.text)
    a3 = pd.DataFrame(a2)
    name = str(q.get(w[i])) + '_vaccines' + '.csv'
    a3.to_csv(name, index=False)
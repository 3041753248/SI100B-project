#prepareations:
from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
from selenium import webdriver

import json
#get the state names:
with open('../data/state_name.json') as q:
    q = json.load(q)
w = list(q.keys())
#get the timeline
date = pd.read_csv("../data/Alaska_cases.csv")
date = list(date['date'])
l = len(date)
#s records the cumulative cases for each state:
s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#repeat through the timeline
for i in range(0, l):
    e = date[i]
    #r records the cumulative cases of each state on certain day:
    r = []
    #get the cumulative cases on certain day of each state:
    for j in range(0, 52):
        a1 = pd.read_csv("../data/" + q.get(w[j]) + "_cases.csv")
        b = list(a1['raw_positives'])
        b = int(a1[a1['date'] == e]['raw_positives'])
        s[j] = s[j] + b
        r.append([q.get(w[j]), s[j]])
    #generate a demo for each day:
    low, high = min(s), max(s)

    (
        Map()
            .add("", r, maptype="美国", is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=high, min_=low),
            title_opts=opts.TitleOpts(title="美国各州COVID-19累计确诊病例数(" + str(date[i]) + ")"))
            .render('../data/html/' + date[i] + '.html')
    )
    browser = webdriver.Edge()
    browser.get('D:/课/信导/project/data/html/' + date[i] + '.html')
    browser.get_screenshot_as_file('../data/png/' + date[i] + '.png')
    browser.quit()
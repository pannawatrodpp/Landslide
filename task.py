import requests
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db import models


# ANN
import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'landslide.settings')
django.setup()

# Database
from app.models import *

# For check exsit
# riskDb = RiskDb()
def Train():
    # API
    
    url = "http://ews1.dwr.go.th/website/webservice/rain_daily.php?uid=landslide2022cm&upass=cicecmu2020&dmode=2&dtype=2&ondate=dd/mm/yyyy"
    req = requests.get(url).json()
    for i in req['station']:
        if(i['id'] == "STN0001"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0036"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0051"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0141"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0249"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0255"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0523"):
            try:
                rainDb = RainDb.objects.get(scope="01",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "01"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        
        # 02
        if(i['id'] == "STN0203"):
            try:
                rainDb = RainDb.objects.get(scope="02",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "02"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0311"):
            try:
                rainDb = RainDb.objects.get(scope="02",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "02"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0421"):
            try:
                rainDb = RainDb.objects.get(scope="02",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "02"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        
        # 03
        if(i['id'] == "STN0023"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0045"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0115"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN00115"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0182"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0254"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0422"):
            try:
                rainDb = RainDb.objects.get(scope="03",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "03"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        
        # 04
        if(i['id'] == "STN0045"):
            try:
                rainDb = RainDb.objects.get(scope="04",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "04"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0075"):
            try:
                rainDb = RainDb.objects.get(scope="04",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "04"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0254"):
            try:
                rainDb = RainDb.objects.get(scope="04",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "04"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        # 05
        if(i['id'] == "STN0014"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0024"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0075"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0205"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0252"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0415"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0417"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0418"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0419"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
        elif(i['id'] == "STN0520"):
            try:
                rainDb = RainDb.objects.get(scope="05",station=i['id'])
                rainDb.rain = i['rain07h']
                rainDb.save()
            except:
                rainDb = RainDb()
                rainDb.scope = "05"
                rainDb.rain = i['rain07h']
                rainDb.station = i['id']
                rainDb.save()
    print("-------- Rain from API Complete ---------")
    # req.close()

    # Calculate Rain Total
    sum1 = 0 
    sum2 = 0 
    sum3 = 0 
    sum4 = 0 
    sum5 = 0 
    for i in RainDb.objects.all():
        if(i.scope == "01"):
            sum1 += i.rain
        elif(i.scope == "02"): 
            sum2 += i.rain
        elif(i.scope == "03"):
            sum3 += i.rain
        elif(i.scope == "04"):
            sum4 += i.rain
        else:
            sum5 += i.rain
    
    # DB 01
    try:
        rainTotalDb = RainTotalDb.objects.get(scope="01")
        rainTotalDb.rainTotal = int(sum1/7)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    except:
        rainTotalDb = RainTotalDb()
        rainTotalDb.scope = "01"
        rainTotalDb.rainTotal = int(sum1/7)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    # DB 02
    try:
        rainTotalDb = RainTotalDb.objects.get(scope="02")
        rainTotalDb.rainTotal = int(sum2/3)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    except:
        rainTotalDb = RainTotalDb()
        rainTotalDb.scope = "02"
        rainTotalDb.rainTotal = int(sum2/3)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    # DB 03
    try:
        rainTotalDb = RainTotalDb.objects.get(scope="03")
        rainTotalDb.rainTotal = int(sum3/6)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    except:
        rainTotalDb = RainTotalDb()
        rainTotalDb.scope = "03"
        rainTotalDb.rainTotal = int(sum3/6)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    # DB 04
    try:
        rainTotalDb = RainTotalDb.objects.get(scope="04")
        rainTotalDb.rainTotal = int(sum4/3)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    except:
        rainTotalDb = RainTotalDb()
        rainTotalDb.scope = "04"
        rainTotalDb.rainTotal = int(sum4/3)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    # DB 05
    try:
        rainTotalDb = RainTotalDb.objects.get(scope="05")
        rainTotalDb.rainTotal = int(sum5/10)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    except:
        rainTotalDb = RainTotalDb()
        rainTotalDb.scope = "05"
        rainTotalDb.rainTotal = int(sum5/10)
        rainTotalDb.rain5Total = 0
        rainTotalDb.save()
    
    print("------ Rain total complete -----")

    
    # ANN 01
    LSmodel = load_model('./static/model/model.h5')
    filePath = './static/model/01.csv'
    rain = RainDb.objects.all()
    dataset = pd.read_csv(filePath)
    newRain = []
    # IDW
    for i in range(len(dataset)):
        #STN0001,STN0036,STN0051,STN0141,STN0249,STN0255,STN0523
        newRain.append(
            (RainDb.objects.get(station="STN0001",scope="01").rain/dataset.iloc[i][8] +
            RainDb.objects.get(station="STN0036",scope="01").rain/dataset.iloc[i][9] +
            RainDb.objects.get(station="STN0051",scope="01").rain/dataset.iloc[i][10] +
            RainDb.objects.get(station="STN0141",scope="01").rain/dataset.iloc[i][11] +
            RainDb.objects.get(station="STN0249",scope="01").rain/dataset.iloc[i][12] +
            RainDb.objects.get(station="STN0255",scope="01").rain/dataset.iloc[i][13] +
            RainDb.objects.get(station="STN0523",scope="01").rain/dataset.iloc[i][14]
            )/(1/dataset.iloc[i][8] +
            1/dataset.iloc[i][9] +
            1/dataset.iloc[i][10] +
            1/dataset.iloc[i][11] +
            1/dataset.iloc[i][12] +
            1/dataset.iloc[i][13] +
            1/dataset.iloc[i][14])
            )
    dataset['IDW-5d'] = DataFrame(newRain)
    dataset.to_csv(filePath, index=False, mode= 'w')
    dataset.isnull().sum()
    X = dataset.iloc[:,1:5].values
    sl = dataset.iloc[:,3].values
    le = LabelEncoder()
    X[:, 1] = le.fit_transform(X[:, 1])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    sc = StandardScaler()
    X_test  = sc.fit_transform(X)
    meanSt1 = 26.9769               
    sdSt1 = 20.7869
    rainSt1 = X[:,7]
    stardScaleSt1 = (rainSt1 - meanSt1)/sdSt1
    X_test[:,7] = stardScaleSt1
    meanSt2 = 12.8612               
    sdSt2 = 5.185
    rainSt2 = X[:,6]
    stardScaleSt2 = (rainSt2 - meanSt2)/sdSt2
    X_test[:,6] = stardScaleSt2
    y_pred = LSmodel.predict(X_test)
    normalized = (sl-min(sl))/(max(sl)-min(sl))
    for i in range(len(y_pred)):
        if sl[i] >= 5:
            y_pred[i] = normalized[i]*y_pred[i]
            # print(y_pred[i])
        else:
            y_pred[i] = 0
    df = DataFrame(y_pred)
    df_csv = pd.read_csv(filePath)
    df_csv['ls_prob'] = df
    df_csv.to_csv(filePath, index=False, mode= 'w')
    # Push to Db
    for i in range(len(df_csv)):
        try:
            riskDb = RiskDb.objects.get(scope="01",latitude=df_csv.iloc[i][6],longitude=df_csv.iloc[i][7])
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.risk = df_csv.iloc[i][15]
            riskDb.save()
        except:
            riskDb = RiskDb()
            riskDb.scope = "01"
            riskDb.slope = df_csv.iloc[i][3]
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.latitude = df_csv.iloc[i][6]
            riskDb.longitude = df_csv.iloc[i][7]
            riskDb.risk = df_csv.iloc[i][15]
            riskDb.save()

    print("------- 01 COMPLETE -------")

    
    # ANN 02
    LSmodel = load_model('./static/model/model.h5')
    filePath = './static/model/02.csv'
    dataset = pd.read_csv(filePath)
    newRain = []
    # IDW
    for i in range(len(dataset)):
        #STN0203,STN0311,STN0421
        newRain.append(
            (RainDb.objects.get(station="STN0203",scope="02").rain/dataset.iloc[i][8] +
            RainDb.objects.get(station="STN0311",scope="02").rain/dataset.iloc[i][9] +
            RainDb.objects.get(station="STN0421",scope="02").rain/dataset.iloc[i][10]
            )/(1/dataset.iloc[i][8] +
            1/dataset.iloc[i][9] +
            1/dataset.iloc[i][10])
            )
    dataset['IDW-5d'] = DataFrame(newRain)
    dataset.to_csv(filePath, index=False, mode= 'w')
    dataset.isnull().sum()
    X = dataset.iloc[:,1:5].values
    sl = dataset.iloc[:,3].values
    le = LabelEncoder()
    X[:, 1] = le.fit_transform(X[:, 1])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    sc = StandardScaler()
    X_test  = sc.fit_transform(X)
    meanSt1 = 26.9769               
    sdSt1 = 20.7869
    rainSt1 = X[:,7]
    stardScaleSt1 = (rainSt1 - meanSt1)/sdSt1
    X_test[:,7] = stardScaleSt1
    meanSt2 = 12.8612               
    sdSt2 = 5.185
    rainSt2 = X[:,6]
    stardScaleSt2 = (rainSt2 - meanSt2)/sdSt2
    X_test[:,6] = stardScaleSt2
    y_pred = LSmodel.predict(X_test)
    normalized = (sl-min(sl))/(max(sl)-min(sl))
    for i in range(len(y_pred)):
        if sl[i] >= 5:
            y_pred[i] = normalized[i]*y_pred[i]
            # print(y_pred[i])
        else:
            y_pred[i] = 0
    df = DataFrame(y_pred)
    df_csv = pd.read_csv(filePath)
    df_csv['ls_prob'] = df
    df_csv.to_csv(filePath, index=False, mode= 'w')
    # Push to Db
    for i in range(len(df_csv)):
        try:
            riskDb = RiskDb.objects.get(scope="02",latitude=df_csv.iloc[i][6],longitude=df_csv.iloc[i][7])
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.risk = df_csv.iloc[i][11]
            riskDb.save()
        except:
            riskDb = RiskDb()
            riskDb.scope = "02"
            riskDb.slope = df_csv.iloc[i][3]
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.latitude = df_csv.iloc[i][6]
            riskDb.longitude = df_csv.iloc[i][7]
            riskDb.risk = df_csv.iloc[i][11]
            riskDb.save()
    print("------- 02 COMPLETE -------")
    

    # ANN 03
    LSmodel = load_model('./static/model/model.h5')
    filePath = './static/model/03.csv'
    dataset = pd.read_csv(filePath)
    newRain = []
    # IDW
    for i in range(len(dataset)):
        #STN0023,STN0045,STN0115,STN0182,STN0254,STN0422 5
        newRain.append(
            (RainDb.objects.get(station="STN0023",scope="03").rain/dataset.iloc[i][8] +
            RainDb.objects.get(station="STN0045",scope="03").rain/dataset.iloc[i][9] +
            RainDb.objects.get(station="STN0115",scope="03").rain/dataset.iloc[i][10] +
            RainDb.objects.get(station="STN0182",scope="03").rain/dataset.iloc[i][11] +
            RainDb.objects.get(station="STN0254",scope="03").rain/dataset.iloc[i][12] +
            RainDb.objects.get(station="STN0422",scope="03").rain/dataset.iloc[i][13]
            )/(1/dataset.iloc[i][8] +
            1/dataset.iloc[i][9] +
            1/dataset.iloc[i][10] +
            1/dataset.iloc[i][11] +
            1/dataset.iloc[i][12] +
            1/dataset.iloc[i][13])
            )
    dataset['IDW-5d'] = DataFrame(newRain)
    dataset.to_csv(filePath, index=False, mode= 'w')
    dataset.isnull().sum()
    X = dataset.iloc[:,1:5].values
    sl = dataset.iloc[:,3].values
    le = LabelEncoder()
    X[:, 1] = le.fit_transform(X[:, 1])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    sc = StandardScaler()
    X_test  = sc.fit_transform(X)
    meanSt1 = 26.9769               
    sdSt1 = 20.7869
    rainSt1 = X[:,7]
    stardScaleSt1 = (rainSt1 - meanSt1)/sdSt1
    X_test[:,7] = stardScaleSt1
    meanSt2 = 12.8612               
    sdSt2 = 5.185
    rainSt2 = X[:,6]
    stardScaleSt2 = (rainSt2 - meanSt2)/sdSt2
    X_test[:,6] = stardScaleSt2
    y_pred = LSmodel.predict(X_test)
    normalized = (sl-min(sl))/(max(sl)-min(sl))
    for i in range(len(y_pred)):
        if sl[i] >= 5:
            y_pred[i] = normalized[i]*y_pred[i]
            # print(y_pred[i])
        else:
            y_pred[i] = 0
    df = DataFrame(y_pred)
    df_csv = pd.read_csv(filePath)
    df_csv['ls_prob'] = df
    df_csv.to_csv(filePath, index=False, mode= 'w')
    # Push to Db
    for i in range(len(df_csv)):
        try:
            riskDb = RiskDb.objects.get(scope="03",latitude=df_csv.iloc[i][6],longitude=df_csv.iloc[i][7])
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.risk = df_csv.iloc[i][14]
            riskDb.save()
        except:
            riskDb = RiskDb()
            riskDb.scope = "03"
            riskDb.slope = df_csv.iloc[i][3]
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.latitude = df_csv.iloc[i][6]
            riskDb.longitude = df_csv.iloc[i][7]
            riskDb.risk = df_csv.iloc[i][14]
            riskDb.save()
    print("------- 03 COMPLETE -------")

    
    # ANN 04
    LSmodel = load_model('./static/model/model.h5')
    filePath = './static/model/04.csv'
    dataset = pd.read_csv(filePath)
    newRain = []
    # IDW
    for i in range(len(dataset)):
        #STN0045,STN0075,STN0254
        newRain.append(
            (RainDb.objects.get(station="STN0045",scope="04").rain/dataset.iloc[i][8] +
            RainDb.objects.get(station="STN0075",scope="04").rain/dataset.iloc[i][9] +
            RainDb.objects.get(station="STN0254",scope="04").rain/dataset.iloc[i][10]
            )/(1/dataset.iloc[i][8] +
            1/dataset.iloc[i][9] +
            1/dataset.iloc[i][10])
            )
    dataset['IDW-5d'] = DataFrame(newRain)
    dataset.to_csv(filePath, index=False, mode= 'w')
    dataset.isnull().sum()
    X = dataset.iloc[:,1:5].values
    sl = dataset.iloc[:,3].values
    le = LabelEncoder()
    X[:, 1] = le.fit_transform(X[:, 1])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    sc = StandardScaler()
    X_test  = sc.fit_transform(X)
    meanSt1 = 26.9769               
    sdSt1 = 20.7869
    rainSt1 = X[:,7]
    stardScaleSt1 = (rainSt1 - meanSt1)/sdSt1
    X_test[:,7] = stardScaleSt1
    meanSt2 = 12.8612               
    sdSt2 = 5.185
    rainSt2 = X[:,6]
    stardScaleSt2 = (rainSt2 - meanSt2)/sdSt2
    X_test[:,6] = stardScaleSt2
    y_pred = LSmodel.predict(X_test)
    normalized = (sl-min(sl))/(max(sl)-min(sl))
    for i in range(len(y_pred)):
        if sl[i] >= 5:
            y_pred[i] = normalized[i]*y_pred[i]
            # print(y_pred[i])
        else:
            y_pred[i] = 0
    df = DataFrame(y_pred)
    df_csv = pd.read_csv(filePath)
    df_csv['ls_prob'] = df
    df_csv.to_csv(filePath, index=False, mode= 'w')
    # Push to Db
    for i in range(len(df_csv)):
        try:
            riskDb = RiskDb.objects.get(scope="04",latitude=df_csv.iloc[i][6],longitude=df_csv.iloc[i][7])
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.risk = df_csv.iloc[i][11]
            riskDb.save()
        except:
            riskDb = RiskDb()
            riskDb.scope = "04"
            riskDb.slope = df_csv.iloc[i][3]
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.latitude = df_csv.iloc[i][6]
            riskDb.longitude = df_csv.iloc[i][7]
            riskDb.risk = df_csv.iloc[i][11]
            riskDb.save()
    print("------- 04 COMPLETE -------")


    # ANN 05
    LSmodel = load_model('./static/model/model.h5')
    filePath = './static/model/05.csv'
    dataset = pd.read_csv(filePath)
    newRain = []
    # IDW
    for i in range(len(dataset)):
        #STN0014,STN0024,STN0075,STN0205,STN0252,STN0415,STN0417,STN0418,STN0419,STN0520
        newRain.append(
            (RainDb.objects.get(station="STN0014",scope="05").rain/dataset.iloc[i][8] +
            RainDb.objects.get(station="STN0024",scope="05").rain/dataset.iloc[i][9] +
            RainDb.objects.get(station="STN0075",scope="05").rain/dataset.iloc[i][10] +
            RainDb.objects.get(station="STN0205",scope="05").rain/dataset.iloc[i][11] +
            RainDb.objects.get(station="STN0252",scope="05").rain/dataset.iloc[i][12] +
            RainDb.objects.get(station="STN0415",scope="05").rain/dataset.iloc[i][13] +
            RainDb.objects.get(station="STN0417",scope="05").rain/dataset.iloc[i][14] +
            RainDb.objects.get(station="STN0418",scope="05").rain/dataset.iloc[i][15] +
            RainDb.objects.get(station="STN0419",scope="05").rain/dataset.iloc[i][16] +
            RainDb.objects.get(station="STN0520",scope="05").rain/dataset.iloc[i][17]
            )/(1/dataset.iloc[i][8] +
            1/dataset.iloc[i][9] +
            1/dataset.iloc[i][10] +
            1/dataset.iloc[i][11] +
            1/dataset.iloc[i][12] +
            1/dataset.iloc[i][13] +
            1/dataset.iloc[i][14] +
            1/dataset.iloc[i][15] +
            1/dataset.iloc[i][16] +
            1/dataset.iloc[i][17])
            )
    dataset['IDW-5d'] = DataFrame(newRain)
    dataset.to_csv(filePath, index=False, mode= 'w')
    dataset.isnull().sum()
    X = dataset.iloc[:,1:5].values
    sl = dataset.iloc[:,3].values
    le = LabelEncoder()
    X[:, 1] = le.fit_transform(X[:, 1])
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))
    sc = StandardScaler()
    X_test  = sc.fit_transform(X)
    meanSt1 = 26.9769               
    sdSt1 = 20.7869
    rainSt1 = X[:,7]
    stardScaleSt1 = (rainSt1 - meanSt1)/sdSt1
    X_test[:,7] = stardScaleSt1
    meanSt2 = 12.8612               
    sdSt2 = 5.185
    rainSt2 = X[:,6]
    stardScaleSt2 = (rainSt2 - meanSt2)/sdSt2
    X_test[:,6] = stardScaleSt2
    y_pred = LSmodel.predict(X_test)
    normalized = (sl-min(sl))/(max(sl)-min(sl))
    for i in range(len(y_pred)):
        if sl[i] >= 5:
            y_pred[i] = normalized[i]*y_pred[i]
            # print(y_pred[i])
        else:
            y_pred[i] = 0
    df = DataFrame(y_pred)
    df_csv = pd.read_csv(filePath)
    df_csv['ls_prob'] = df
    df_csv.to_csv(filePath, index=False, mode= 'w')
    # Push to Db
    for i in range(len(df_csv)):
        try:
            riskDb = RiskDb.objects.get(scope="05",latitude=df_csv.iloc[i][6],longitude=df_csv.iloc[i][7])
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.risk = df_csv.iloc[i][18]
            riskDb.save()
        except:
            riskDb = RiskDb()
            riskDb.scope = "05"
            riskDb.slope = df_csv.iloc[i][3]
            riskDb.rain= df_csv.iloc[i][4]
            riskDb.latitude = df_csv.iloc[i][6]
            riskDb.longitude = df_csv.iloc[i][7]
            riskDb.risk = df_csv.iloc[i][18]
            riskDb.save()
    print("------- 05 COMPLETE -------")
    
    testrisk = RiskDb.objects.get(id=1)
    testrisk.rain = 100
    testrisk.save()

    # History Risk
    for i in RiskDb.objects.all():
        if(i.risk >= 0.5):
            historyDb = HistoryDb()
            historyDb.date = datetime.datetime.today().strftime("%Y-%m-%d")
            historyDb.risk = i.risk
            historyDb.rain = i.rain
            historyDb.latitude = i.latitude
            historyDb.longitude = i.longitude
            historyDb.save()
    print("------- All Complete --------")
    
    

Train()
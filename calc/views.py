from django.shortcuts import render
# from django.http import HttpResponse 
from .models import Result
# Create your views here.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from sklearn.externals import joblib
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
import csv
import datetime
from math import sqrt
from sklearn.svm import SVR
import sklearn.svm as svm
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from datetime import timedelta


column_names = [
    'Fran Datum Tid (UTC)', 'till', 'day', 'temperature', 'Kvalitet', 'Tidsutsnitt:', 'Unnamed: 5'
]
column_names_used = [
    'Fran Datum Tid (UTC)', 'till', 'day'
]
def make_numeric_values(arr, title):
    new_arr = []
    for date in arr[title]:
        new_date = make_date(date)
        new_arr.append(new_date)
    arr[title] = new_arr

def fix_array(arr):
    for name in column_names_used:
        make_numeric_values(arr, name)

def make_date(date):
    new_date = date.split(' ')
    new_date = new_date[0]
    new_date = new_date.split('-')
    new_number = ''
    first = True
    for number in new_date:
        if first:
            first = False
        else:
            new_number = new_number + number
    return new_number

def convert_date_to_string(plus_days):
    date = datetime.datetime.today() + timedelta(days=plus_days)
    date = date.strftime("%Y-%m-%d %H:%M:%S") 
    date = date.split(' ')
    date = date[0]
    date = date.split('-')
    date = date[1]+date[2]
    return date

# THIS IS WHERE THE MODEL GETS TRAINED
# if you want to use this in your own project this is the method you want to study

def train():
    dataset_url1 = 'calc/smhi-opendata_2_71420_corrected-archive_2020-05-01_18-00-00.csv'
    dataset_url2 = 'calc/smhi-opendata_2_71420_latest-months_2020-05-03_15-00-00.csv'

    data1 = pd.read_csv(dataset_url1, sep=';', skiprows=3607, names=column_names)
    data2 = pd.read_csv(dataset_url2, sep=';', skiprows=15, names=column_names)

    data1 = data2.append(data1)
    data1 = data1.drop('Tidsutsnitt:', axis=1)
    X = data1.drop(["temperature"], axis=1)
    X = X.drop(['Kvalitet'], axis = 1)
    X = X.drop(['Unnamed: 5'], axis = 1)
    fix_array(X)

    y = data1['temperature']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=123)

    tree_model = DecisionTreeRegressor()

    tree_model.fit(X_train, y_train)
    joblib.dump(tree_model, 'weather_predictor.pkl')
    print("---------------------------" * 48)
    print("\n---------------------Done training--------------------------\n")
    print("-" * 48)

def predict_weather(year, month, day):
    tree_model = joblib.load('weather_predictor.pkl')

    year = year
    month = month
    theday = day

    day = str(month) + str(theday)
    
    date = [
        [day, 
        (str(int(day) + 1)), 
        (day)]
    ]
    temp = tree_model.predict(date)[0]
    return str(temp)

def home(request):
    return render(request, 'home.html', {'name': 'shubham'})




def add(request):
    name = request.POST['birthday']
    year = name[0:4]
    month = name[5:7]
    date = name[8:10]
    train()
    params = predict_weather(year, month, date)
    return render (request, 'result.html', {'ans': params})
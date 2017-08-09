# coding: utf-8

import warnings
# Ignore the warnings: https://github.com/jupyter/notebook/issues/2239
warnings.filterwarnings(action='ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
import pywt
import pickle

def predict_last_day(cs, df, clf):
    #print cs
    
    df_cs = df[df['cowshed'] == cs]
    df_cs.sort_values(by='date')
    df_cs.index = range(len(df_cs))
    
    # compute THI
    df_thi = 0.81 * df_cs['temp_high'] + (0.99 * df_cs['temp_high'] - 14.3) * df_cs['RH'] / 100.0
    df_thi = pd.DataFrame(df_thi, columns=['THI'])
    df_etl = pd.concat([df_cs, df_thi], axis=1)
    
    #print df_etl
    ws = 4
    
    index_target = len(df_etl) - 1
    index_train_s = index_target - ws
    index_train_e = index_target - 1
    data_train = df_etl.iloc[index_train_s:index_train_e+1, :]
    
    X = [df_etl['avg_actual'].iloc[index_train_e]]
    
    cA, cD = pywt.dwt(data_train['avg_milk'].values, 'db1')
    X = np.append(X, list(cA) + list(cD))
    X = np.append(X, [df_etl.iloc[index_target]['THI']])
    X = np.append(X, df_etl.iloc[index_train_e]['calving_days'])
    X = np.append(X, df_etl.iloc[index_train_e]['calving_indices'])
    #print X

    prediction = clf.predict(np.array([X]))[0]
    print cs + ':', + prediction


if __name__ == '__main__':
    # Load the model
    clf = pickle.load(open("model.pickle.dat", "rb"))

    filename = 'input.csv'
    df = pd.read_csv(filename)
    #print df.head()

    cowsheds = set(df['cowshed'].values)
    print '牛舍：',
    for x in cowsheds:
        print x,
    print ''

    for cs in cowsheds:
        predict_last_day(cs, df, clf)


import pandas as pd
import numpy as np
import nltk
import preprocessor as p

cols = [
    'UserId',
    'UserName',
    'CreatedAt',
    'RetweetCount',
    'IsRetweet',
    'FavoriteCount',
    'Text',
    'Id',
    'Source',
    'Hashtags',
    'Urls',
    'Posted',
    'UserMentions'
]
real_data = pd.read_csv('Data/Tweets_Remainder.csv', names=cols, encoding='utf-8')
for i, tweet in enumerate(real_data['Text']):
    real_data.iloc(i).Text = p.clean(str(tweet).encode('ascii', errors='ignore').decode())

print(real_data)
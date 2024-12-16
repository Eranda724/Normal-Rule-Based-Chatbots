# -*- coding: utf-8 -*-
"""ChatBot1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xg8PIPl6-RjFcNjU8Ft1hgxnmGhD6YkH
"""

import numpy as np
import pandas as pd
df = pd.read_csv("Mental_Health_FAQ.csv")

df.head()

df.info()

df.isnull().sum()

#null value remove
#df.dropna(inplace = True)
df = df.drop("Question_ID", axis=1)

df.isnull().sum()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vec = TfidfVectorizer()
vec.fit(np.concatenate((df["Questions"],df["Answers"])))

np.concatenate((df["Questions"],df["Answers"]))

feature_cols = vec.get_feature_names_out()
len(feature_cols)

df_vec = vec.transform(df["Questions"])

print("Hello How can I help you")

while True:
    input_q = input()
    input_qvec = vec.transform([input_q])
    simila = cosine_similarity(input_qvec , df_vec)
    close_answr = np.argmax(simila , axis =1)
    print("Chatbot: " , df["Answers"].iloc[close_answr].values[0])
















# Python script to build a model from kaggle data
# Steps would be
# 1. Initialize environment
# 2. Rertieve the data from S3
# 3. Split the data into train/test
# 4. Train the model
# 5. Test the accuracy of the model
# 6. Save the model

import pandas as pd
import numpy as np

# Load the data
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"

df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only 4 feature
df_ = df[include]

# Cleans the data
categoricals = []
for col, col_type in df_.dtypes.iteritems():
    if col_type == 'O':
        categoricals.append(col)
    else:
        df_[col].fillna(0, inplace=True)

# Encode categorical values with One Hot Encoding
df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)


# Train the model
from sklearn.linear_model import LogisticRegression
dependent_variable = 'Survived'

x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
lr = LogisticRegression()
lr.fit(x, y)

# save the model
from sklearn.externals import joblib
joblib.dump(lr, 'model.pkl')
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')


# Import Pandas
import pandas as pd

file_name = 'India_in_Tests.csv'
fields = ['Result','Toss','Bat']

# Read the CSV file
df = pd.read_csv(file_name,skipinitialspace=True,usecols=fields)
df.to_csv('India_in_Tests_Filter.csv',index=False)

# Convert features and labels into digits
df_replace = df.replace(['lost','draw','won','1st','2nd'],[-1,0,1,-1,1])
dataset_length = len(df_replace)

# 65% of training data
ratio = 0.65
train_data_df = df_replace[:round(dataset_length*ratio)] # first 65% of data
test_data_df = df_replace[-(1-round(dataset_length*ratio)):] # rest for testing

# Create Respected CSV
train_data_df.to_csv('train.csv',index=False)
test_data_df.to_csv('test.csv',index=False)

#read the csv file in pandas
import pandas as pd
df = pd.read_csv(r'D:\MLOps\Data-Versioning-Using-DVC\data\Friends_Sample_Dataset.csv')
print(df.head()) 


# add new row to the csv file
df.loc[len(df)] = ['Hashim',30,'ICT']

# save it 
df.to_csv(r'D:\MLOps\Data-Versioning-Using-DVC\data\Friends_Sample_Dataset.csv',index=False)
print(df.head())
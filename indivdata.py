import pandas as pd

df = pd.read_csv("/Users/shayaan/Downloads/single.txt",
                 skipfooter=75,sep='\t',engine="python")
df.columns = ["value"]
df['value'] = df['value'].astype(str)
ICD_code = ["I10","I11","I12","I13","I14","I15"]
race_code = ["6","7"]

#Filter ICD
df = df.loc[df['value'].str[145:148].isin(ICD_code)]
#Filter Filter race
df = df.loc[df['value'].str[487].isin(race_code)]

df1 = pd.DataFrame()
#Get ICD
df1["ICD"] = df['value'].str[145:149]
df1['ICD'] = df1["ICD"].apply(lambda x: x[:3] + '.' + x[3:] if len(x) > 3 and x[3] != ' ' else x)
#Get Race
df1["Race"] = df['value'].str[487]
df1['Race'] = df1['Race'].apply(lambda x: 'White' if x == '6' else 'Black')
#Get Gender
df1["Gender"] = df['value'].str[68]
df1['Gender'] = df1['Gender'].map({'M': 'Male', 'F': 'Female'})
#Get age
df1["Age"] = df['value'].str[69]
df1.loc[df1["Age"] == "1", "Age"] = df['value'].str[70:73]
df1.loc[df1["Age"] != "1", "Age"] = 0
df1.loc[df['value'].str[70] == "0", "Age"] = df['value'].str[71:73]
#Get year
df1["Year"] = "2020"

df1 = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df1.to_csv("new_data.csv", index = False, sep = "\t")
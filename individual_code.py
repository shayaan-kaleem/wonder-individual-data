import pandas as pd

df = pd.read_csv("/Users/shayaan/Downloads/2021.txt",
                 sep='\t',engine="python", header = None)
df.columns = ["value"]
df['value'] = df['value'].astype(str)
ICD_code = ["I20","I21","I22","I23","I24","I25","I46"]
hispanic_status = [str(number) for number in range(100, 200)]
race_code_2021 = ["01","02"]
race_code = ["6","7"]

#Filter ICD
df = df.loc[df['value'].str[145:148].isin(ICD_code)]
#Filter hispanic status
df = df.loc[df['value'].str[483:486].isin(hispanic_status)]
#Filter Filter race
df = df.loc[df['value'].str[488:490].isin(race_code_2021)]
#Filter residence status
df = df[df['value'].str[19] == '1']

df1 = pd.DataFrame()
#Get ICD
df1["ICD"] = df['value'].str[145:149]
df1['ICD'] = df1["ICD"].apply(lambda x: x[:3] + '.' + x[3:] if len(x) > 3 and x[3] != ' ' else x)
#Get Race
df1["Race"] = df['value'].str[488:490]
df1['Race'] = df1['Race'].apply(lambda x: 'White' if x == '01' else 'Black')
#Get Gender
df1["Gender"] = df['value'].str[68]
df1['Gender'] = df1['Gender'].map({'M': 'Male', 'F': 'Female'})
# Get age
df1["Age"] = df['value'].str[69]
df1["find_NA"] = df['value'].str[70:73]
df1.loc[df1["Age"] == "1", "Age Code"] = df['value'].str[70:73]
df1.loc[df1["Age"] != "1", "Age Code"] = "0"
df1 = df1.drop(df1[df1["Age"] == "9"].index)
df1 = df1.drop(df1[df1["find_NA"] == "999"].index)
df1['Age Code'] = df1['Age Code'].str.lstrip('0')
df1 = df1.astype(str)
df1 = df1.drop(['Age',"find_NA"], axis=1)
df1 = df1.rename(columns={"Age Code": "Age"})

#Get year
df1["Year"] = "2021"
print(df1.head())

df1 = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df1.to_csv("ind_data_IHD.csv", index = False, sep = "\t")

for year in range(2020, 2002, -1):
    filename = f"/Users/shayaan/Downloads/{year}.txt"

    df = pd.read_csv(filename, sep='\t', engine="python",header = None)
    df.columns = ["value"]
    df['value'] = df['value'].astype(str)

    # Filter ICD
    df = df.loc[df['value'].str[145:148].isin(ICD_code)]
    # Filter race
    df = df.loc[df['value'].str[487].isin(race_code)]

    df1 = pd.DataFrame()
    # Get ICD
    df1["ICD"] = df['value'].str[145:149]
    df1['ICD'] = df1["ICD"].apply(lambda x: x[:3] + '.' + x[3:] if len(x) > 3 and x[3] != ' ' else x)
    # Get Race
    df1["Race"] = df['value'].str[487]
    df1['Race'] = df1['Race'].apply(lambda x: 'White' if x == '6' else 'Black')
    # Get Gender
    df1["Gender"] = df['value'].str[68]
    df1['Gender'] = df1['Gender'].map({'M': 'Male', 'F': 'Female'})
    #Get age
    df1["Age"] = df['value'].str[69]
    df1["find_NA"] = df['value'].str[70:73]
    df1.loc[df1["Age"] == "1", "Age Code"] = df['value'].str[70:73]
    df1.loc[df1["Age"] != "1", "Age Code"] = "0"
    df1 = df1.drop(df1[df1["Age"] == "9"].index)
    df1 = df1.drop(df1[df1["find_NA"] == "999"].index)
    df1['Age Code'] = df1['Age Code'].str.lstrip('0')
    df1 = df1.astype(str)
    df1 = df1.drop(['Age',"find_NA"], axis=1)
    df1 = df1.rename(columns={"Age Code": "Age"})
    # Get year
    df1["Year"] = str(year)
    df1 = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df1.to_csv("ind_data_IHD.csv", mode="a", header=False, index=False, sep="\t")

for year in range(2002, 1998, -1):
    filename = f"/Users/shayaan/Downloads/{year}.txt"

    df = pd.read_csv(filename, sep='\t', engine="c",header = None)
    df.columns = ["value"]
    df['value'] = df['value'].astype(str)

    # Filter ICD
    df = df.loc[df['value'].str[141:144].isin(ICD_code)]
    # Filter race
    df = df.loc[df['value'].str[81].isin(race_code)]

    df1 = pd.DataFrame()
    # Get ICD
    df1["ICD"] = df['value'].str[141:145]
    df1['ICD'] = df1["ICD"].apply(lambda x: x[:3] + '.' + x[3:] if len(x) > 3 and x[3] != ' ' else x)
    # Get Race
    df1["Race"] = df['value'].str[81]
    df1['Race'] = df1['Race'].apply(lambda x: 'White' if x == '6' else 'Black')
    # Get Gender
    df1["Gender"] = df['value'].str[58]
    df1['Gender'] = df1['Gender'].map({'1': 'Male', '2': 'Female'})
    # Get age
    df1["Age"] = df['value'].str[63]
    df1 = df1[df1['Age'] != 9]
    df1.loc[(df1["Age"] != "0") & (df1["Age"] != "1"), "Age"] = 0
    df1.loc[df1["Age"] == "0", "Age"] = df['value'].str[64:66]
    df1.loc[df1["Age"] == "1", "Age"] = df['value'].str[64:66].astype(int) + 100
    df1["Age"] = df1["Age"].astype(str)
    # Get year
    df1["Year"] = str(year)

    df1 = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df1.to_csv("ind_data_IHD.csv", mode="a", header=False, index=False, sep="\t")

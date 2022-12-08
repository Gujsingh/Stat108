import pandas as pd
x = pd.read_csv('housingData/housing.csv')  
x = x[(x.StateName == "CA")]
x['average2021'] = x[['2021-01-31','2021-02-28','2021-03-31','2021-04-30','2021-05-31','2021-06-30','2021-07-31','2021-08-31','2021-09-30','2021-10-31','2021-11-30','2021-12-31']].mean(axis = 1)
df = pd.read_csv("schoolData/abreason2021.txt", sep="\t",encoding='latin-1')
df1 = pd.read_csv("schoolData/chrabs2021.txt", sep="\t",encoding='latin-1')
df2 = pd.read_csv("schoolData/cohort2021.txt", sep="\t",encoding='latin-1')
df3 = pd.read_csv("schoolData/sr2021.txt", sep="\t",encoding='latin-1')
df4 = pd.read_csv("schoolData/susp2021.txt", sep="\t",encoding='latin-1')
df5 = pd.read_csv("schoolData/test/test.txt", sep="^",encoding='latin-1')
df6 = pd.read_csv("schoolData/test/testEntities.txt", sep="^",encoding='latin-1')
for i in ['County Code', 'District Code','School Code', 'School Name']:
    df = df[df[i].notna()]
    df1 = df1[df1[i].notna()]
    df2 = df2[df2[i].notna()]
    df3 = df3[df3[i].notna()]
    df4 = df4[df4[i].notna()]
    if i != 'School Name':
        df5 = df5[df5[i].notna()]
    df6 = df6[df6[i].notna()]
print(df.columns)
print(df1.columns)
print(df2.columns)
print(df3.columns)
print(df4.columns)
df = df[['County Code', 'District Code','School Code', 'School Name',"Average Days Absent"]][df["Average Days Absent"]!="*"]
df['Average Days Absent'] = df['Average Days Absent'].astype(float)
df = df.groupby(['County Code', 'District Code','School Code', 'School Name'])["Average Days Absent"].mean()
print(df)
df1 = df1[['County Code', 'District Code','School Code', 'School Name',"ChronicAbsenteeismRate"]][df1["ChronicAbsenteeismRate"]!="*"]
df1['ChronicAbsenteeismRate'] = df1['ChronicAbsenteeismRate'].astype(float)
df1 = df1.groupby(['County Code', 'District Code','School Code', 'School Name'])["ChronicAbsenteeismRate"].mean()
print(df1)
df2 = df2[['County Code', 'District Code','School Code', 'School Name',"Dropout (Rate)"]][df2["Dropout (Rate)"]!="*"]
df2['Dropout (Rate)'] = df2['Dropout (Rate)'].astype(float)
df2 = df2.groupby(['County Code', 'District Code','School Code', 'School Name'])["Dropout (Rate)"].mean()
print(df2)
df3 = df3[['County Code', 'District Code','School Code', 'School Name',"Non-Stability Rate (percent)"]][df3["Non-Stability Rate (percent)"]!="*"]
df3['Non-Stability Rate (percent)'] = df3['Non-Stability Rate (percent)'].astype(float)
df3 = df3.groupby(['County Code', 'District Code','School Code', 'School Name'])["Non-Stability Rate (percent)"].mean()
print(df3)
df4 = df4[['County Code', 'District Code','School Code', 'School Name',"Suspension Rate (Total)"]][df4["Suspension Rate (Total)"]!="*"]
df4['Suspension Rate (Total)'] = df4['Suspension Rate (Total)'].astype(float)
df4 = df4.groupby(['County Code', 'District Code','School Code', 'School Name'])["Suspension Rate (Total)"].mean()
print(df4)
df = df.to_frame()
df1 =df1.to_frame()
df2 =df2.to_frame()
df3=df3.to_frame()
df4=df4.to_frame()
print(df.shape,df1.shape)
merged_df = df.merge(df1, how = 'inner', on = ['County Code', 'District Code','School Code', 'School Name'])
print(merged_df.shape)
merged_df = merged_df.merge(df2, how = 'inner', on = ['County Code', 'District Code','School Code', 'School Name'])
print(merged_df.shape)
merged_df = merged_df.merge(df3, how = 'inner', on = ['County Code', 'District Code','School Code', 'School Name'])
print(merged_df.shape)
merged_df = merged_df.merge(df4, how = 'inner', on = ['County Code', 'District Code','School Code', 'School Name'])
print(merged_df.shape)


df5 = df5[['County Code', 'District Code','School Code',"Mean Scale Score"]][df5["Mean Scale Score"]!="*"]
df6 = df6[['County Code', 'District Code','School Code',"School Name", "Zip Code"]]
df7 = df5.merge(df6, how = 'inner', on = ['County Code', 'District Code','School Code'])
df7['Mean Scale Score'] = df7['Mean Scale Score'].astype(float)
merged_df = merged_df.merge(df7, how = 'inner', on = ['County Code', 'District Code','School Code', 'School Name'])
merged_df = merged_df[merged_df["Mean Scale Score"].notna()]

x = x[["average2021", "RegionName"]]
x["Zip Code"] = x["RegionName"]
x = x[["average2021", "Zip Code"]]
print(x.columns,merged_df.columns)
merged_df = merged_df.merge(x , how = 'inner', on ="Zip Code")
merged_df = merged_df.groupby(['County Code', 'District Code','School Code', 'School Name','Zip Code'])["Average Days Absent","ChronicAbsenteeismRate", "Dropout (Rate)", "Non-Stability Rate (percent)", "Suspension Rate (Total)", "Mean Scale Score", "average2021"].mean()
merged_df.to_csv('data.csv')
# dataframe creation
import pandas as pd
data = {'ID':[1, 2, 3, 4, 5], 
        'Name': ['Krisha', 'Riya', 'Vaidehi', 'Misha', 'Dhyani'], 
        'Age': [17, 18, 18, 18, 17], 
        'Department':['IT', 'Computer', 'Computer', 'IT', 'IT']}
df = pd.DataFrame(data)
print("Data Frame:\n",df,"\n")

# series creation
series = pd.Series([1, 2, 3, 4, 5])
print("Series:\n",series,"\n")

# reading data: 1.to convert csv file to excel file, 2.reads csv files
file = df.to_csv('data1.csv')
read = pd.read_csv('data1.csv')
print("Reading data:\n",read,"\n")

# dataframe inspection
print("head function:\n",df.head(3),"\n")

print("tail function:\n",df.tail(2),"\n")

print("info function:\n",df.info(),"\n")

print("describe function:\n",df.describe(),"\n")

print("shape function:\n",df.shape,"\n")

# data selection
print("Selecting a single column:\n",df['Name'],"\n")

print("Selecting multiple columns:\n",df[['Name', 'Age']],"\n")

print("Selecting rows by index:\n",df.iloc[0],"\n") 

print("Selecting rows by label:\n",df.loc[3],"\n") 

# data manipulation
df['Height'] = [170, 160, 163, 158, 150]
print("Adding a new column:\n",df,"\n")

teenage = df[df['Age'] > 13]
print("Filtering data:\n",teenage,"\n")

sorted_df = df.sort_values(by='Age')
print("Sorting Data:\n",sorted_df,"\n")

df = df.drop(columns=['Height'],axis=1)
print("Deleting/Deleting a column:\n",df,"\n")

df_renamed = df.rename(columns={'Name': 'Student Name'})
print("Renaming a column name:\n",df_renamed,"\n")

df_filled = df.fillna(0)
print("Fill missing values:\n",df_filled,"\n")

df_dropped = df.dropna()
print("Drop rows with missing values:\n",df_dropped,"\n")

# aggregation and grouping
grouped = df.groupby('Name').mean(numeric_only=True)
print("Groupby function on numeric columns:\n", grouped, "\n")

total_age = df['Age'].sum()
print("sum function(sum of age):\n",total_age,"\n")

min_age = df['Age'].min()
print("minimum age:\n",min_age,"\n")

max_age = df['Age'].max()
print("maximum age:\n",max_age,"\n")

count = df['Age'].count()
print("count function:\n",count,"\n")

# pivot table
pivot = df.pivot_table(values='Age', index='Name', aggfunc='mean')
print("pivot table:\n",pivot,"\n")

# conctenate
df2 = pd.DataFrame({'Name': ['Aira'], 'Age': [23], 'Department':['Computer']})
concatenate = pd.concat([df, df2])
print("concatenation:\n",concatenate,"\n")

# merging
df1 = pd.DataFrame({'Name': ['Isha', 'Sana'], 'Score': [85, 90]})
merge = pd.merge(df, df1, on='Name')
print("merge function:\n",merge,"\n")

# Data Visualization (with Matplotlib)
import matplotlib.pyplot as plt
df['Age'].plot(kind='bar')
plt.xticks(ticks=range(len(df['Name'])), labels=df['Name'])
plt.title('Student Data')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()

# transposing data
transpose = df.T
print("Transposed DataFrame:\n",transpose,"\n")

# add a new column based on calculation
df['Age in 5 Years'] = df['Age'] + 5
print("DataFrame with Calculated Column:\n", df, "\n")

# string operations
df['Name Upper'] = df['Name'].str.upper()
print("DataFrame with Uppercase Names:\n", df, "\n")

df['Contains R'] = df['Name'].str.contains('r', case=False)
print("DataFrame with Substring Check:\n", df, "\n")

# data transformation
df['Age Category'] = df['Age'].apply(lambda x: 'Teen' if x < 20 else 'Adult')
print("DataFrame with Age Category:\n", df, "\n")

# filtring and selecting data
filtered_df = df[(df['Age'] > 17) & (df['Name'].str.contains('R'))]
print("Filtered DataFrame:\n", filtered_df, "\n")

query_df = df.query('Age == 18')
print("Queried DataFrame:\n", query_df, "\n")

# data aggregation
df['Cumulative Age'] = df['Age'].cumsum()
print("DataFrame with Cumulative Sum:\n", df, "\n")

unique_ages = df['Age'].unique()
print("Unique Ages:\n", unique_ages, "\n")

import pandas as pd

# Read the input file into a DataFrame
df = pd.read_csv("forParsing_task.xls", delimiter="\t", header=None)

# Filter rows that contain "|" and do not contain "--------"
df = df[df[0].str.contains('\|') & 
~df[0].str.contains('--------')][0].str.split('|', expand=True)

# Drop columns that have all empty values
df = df.drop(df.columns[df.apply(lambda x: x.str.strip().eq('').all())], axis=1)

# Set the first row as column headers
df.columns = df.iloc[0]

# Drop the first row (previously used as column headers)
df = df[1:]

# Remove leading/trailing spaces from column names
df = df.rename(columns=lambda x: x.strip())

# Filter out rows where "Stat" appears in the "Stat" column
df = df[~df['Stat'].str.contains('Stat')]

# Clean the "LC amnt" column by handling negative values, removing commas, 
# and converting to float
df['LC amnt'] = df['LC amnt'].apply(
    lambda x: '-' + x.strip()[:-1] if x.endswith('-') else x.strip()
    ).str.replace(',', '').astype(float)

# Save the cleaned DataFrame to a CSV file
df.to_csv('cleaned_example.csv', index=False)

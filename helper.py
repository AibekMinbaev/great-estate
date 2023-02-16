import pandas as pd 

# Read the JSON file into a DataFrame
df = pd.read_json('backup.json')

# Export the DataFrame to an Excel file
df.to_excel('backup.xlsx', index=False) 

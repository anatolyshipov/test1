import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('user_behavior_dataset 2.csv')

# Filter the DataFrame to include only rows where Gender is 'Male' and Age is greater than 30
filtered_df = df.query('Gender == "Male" and Age > 30')

# Print the filtered DataFrame to verify the results
print(filtered_df)

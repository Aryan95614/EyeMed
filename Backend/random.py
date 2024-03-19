import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Create a dictionary with the data for the new row
new_row = {'Name': 'David', 'Age': 40}

# Append the dictionary to the DataFrame
df = df.append(new_row, ignore_index=True)

# Reset the index
df = df.reset_index(drop=True)

print(df)

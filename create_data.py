import pandas as pd

df = pd.read_csv('preprocessed_data_clean.csv')
# Convert to JS variable
with open('data.js', 'w') as f:
    f.write("const aqiData = " + df.to_json(orient='records') + ";")
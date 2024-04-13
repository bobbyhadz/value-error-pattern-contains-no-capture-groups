# ValueError: pattern contains no capture groups

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice9', 'Bobby8', 'Carl7', 'Dan6', 'Ethan5'],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

new_df = df['name'].str.extract(r'([a-zA-Z]+)(\d)')

print(new_df)
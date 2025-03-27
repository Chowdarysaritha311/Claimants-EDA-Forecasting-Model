import pandas as pd

df = pd.read_csv("data/claimants.csv")
df.fillna(df.median(), inplace=True)
df['CLMSEX'] = df['CLMSEX'].map({'Male': 0, 'Female': 1})
df['SEATBELT'] = df['SEATBELT'].map({'Yes': 0, 'No': 1})
df['CLMINSUR'] = df['CLMINSUR'].map({'Yes': 0, 'No': 1})
df.to_csv("data/cleaned_claimants.csv", index=False)

import pandas as pd

df = pd.read_csv("Data/Test.csv")
df["text_length"] = (df["text"]).apply(lambda x: len(x.replace(" ", "")))
df.to_csv("Data/Processed_Test.csv", index=False)
print(df.head())
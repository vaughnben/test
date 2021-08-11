import pandas as pd
dictionary = {"Name": ["Bill", "John"], "Grade": ["A", "C+"]}

df = pd.DataFrame(dictionary).to_csv("test.csv")
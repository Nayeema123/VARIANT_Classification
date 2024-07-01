import pandas as pd

# Read annotated CSV file
annotated = pd.read_csv('annotated.csv', sep=';')

# Print first 5 rows of the annotated dataframe
print(annotated.head())

# Read class CSV file
class_df = pd.read_csv('class.csv', sep=';')

# Print first 5 rows of the class dataframe
print(class_df.head())

out_df = annotated.merge(class_df, how='left')

out_df.to_csv('result.csv', index=False)

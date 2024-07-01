import pandas as pd

# Read annotated CSV file
annotated_df = pd.read_csv('annotated.csv', sep=';')

# Print first 5 rows of the annotated dataframe
print(annotated_df.head())

# Read haplo CSV file
haplo_df = pd.read_csv('haplo.csv', sep=';')

# Print first 5 rows of the class dataframe
print(haplo_df.head())

# Iterate over each haplo region and check if each annotation falls within that region
for _, row in haplo_df.iterrows():
    mask = (annotated_df['chr'] == row['chr']) & (annotated_df['start'].between(row['start'], row['end']))
    annotated_df.loc[mask, 'haplo_score'] = row['score']

# Print the updated annotations DataFrame
out_df = annotated_df
print(out_df)

"""In this code, we iterate over each row of the haplo_df using the iterrows() method. For each haplo region, we create a boolean mask that checks if each annotation falls within that region using the between() method. We then use this mask to select the relevant rows of the annotated_df and add a new column called 'haplo_score' with the score for that haplo region.
Finally, we print the updated annotated_df with the haplo scores. Note that if an annotation does not fall within any haplo region, the corresponding 'haplo_score' value will be NaN.
"""

out_df['haplo_score'].fillna('-', inplace=True)
print(out_df)

out_df.to_csv('result.csv', index=False)

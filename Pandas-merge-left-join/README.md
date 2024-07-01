# Pandas-merge-left-join

There are two CSV files.
File 1 = annotated.csv

![image](https://github.com/Nayeema123/Variant_Classification/assets/108891639/a02ab9e4-3f14-4d10-8e2e-5fb34d3259ff)

File 2 = class.csv

![image](https://github.com/Nayeema123/Variant_Classification/assets/108891639/0df44858-09dc-4a33-9a54-4229193442c1)

annotated.csv has three columns: chr, start, alt and class.csv has four column: chr, start, alt, class.

Whenever chr, start and alt in annotated.csv matches chr, start and alt in class.csv file, then take the class column value and append it to annotated.csv file.

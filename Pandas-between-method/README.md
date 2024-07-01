There are two CSV files.

File 1 = annotated.csv

![image](https://github.com/Nayeema123/Variant_Classification/assets/108891639/fd433de4-91a9-44fd-9027-5fe926d29ec0)

File 2 = haplo.csv

![image](https://github.com/Nayeema123/Variant_Classification/assets/108891639/673f1407-6b14-4d27-8e73-1644ba6d468e)

annotated.csv has three columns: chr, start, alt and haplo.csv has four column: chr, start, end, score.

haplo.csv file contains regions (start and end columns). In the annotated.csv file has mutations also (start or end column). If a mutation falls within any of the regions in the haplo.csv file, then give it that score of that region.

For example, in annotation.csv file has this mutation:

chr1-----234-----G

and in haplo.csv file has those regions:

chr1-----200-----210-----3

chr1-----230-----240-----10

In this case, the mutation falls within the 2nd row of haplo.csv, so append a new colum for the mutation with score 10.

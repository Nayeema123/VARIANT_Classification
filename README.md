# VARIANT_Classification
Develop a classification model that accurately predicts the pathogenicity of genetic mutations based on various genomic features.
# Genomic Data Classification with Random Forest

This project involves classifying genomic data using a Random Forest classifier. The process includes data preprocessing, feature selection, model training, and evaluation. 
Additionally, the project demonstrates how to save and load the trained model for future use and how to make predictions on new data.

# OBJECTIVE
The goal is to develop a predictive model that can accurately classify VUS mutations based on their functional and structural consequences on the affected genes.
By leveraging all available mutation-specific information, the classifier will guide the classification process and help clinicians make more informed decisions regarding patient care.
The dataset contains around 3000 germline cancer mutations curated from ClinVar database with clear classifications as either pathogenic or benign.
Additionally, haplo scores was also curated from Clingen database to identify its impact on mutations.

## Project Structure

- **annotated.csv**: The dataset used for training and testing after annotating using VEP tool.
- **clinvar.csv**: Data curated from clinvar with clear classifications.
- **class.txt**: Mutations from clinvar, and the respective class ( class1 is pathogenic/likely pathogenic, class2 is benign/Likely benign).
- **haplo.txt**: haploinsufficiency scores for each gene.
- **test.csv**: The new pateint data for predictions.
- **random_forest_model.pkl**: The saved Random Forest model.
- **variant_classification.ipynb**: Jupyter Notebook containing the complete code for the project.

## Steps Involved

1. ------- Data Collection ----------
    - Curated about 3000 germline cancer mutations curated from ClinVar database with clear classifications as either pathogenic or benign.
    - Used VEP to annotate the variants and predict its functional consequences.
    - Additionally, haplo scores was also curated from Clingen database to identify its impact on mutations.
    - Added class to the annotated file by matching the chromosome,start position and alternate allele.
    - Similarly added haploinsufficiency scores whenever a mutation in the annotated file falls within any of the regions inside the haplo file.


2. --------Data loading and preprocessing ---------
    - Loaded the dataset and removed indels and Vus to ensure data quality.
    - Encode categorical variables using `LabelEncoder`.
    - Scale numerical variables using `MinMaxScaler`.

2. ---------- Model Selection --------------:
    - Chose 4 classification algorithms, trained and evaluated each model to choose the best one.
    - Algorithms used:
        - `RandomForestClassifier`
        - `KNeighborsClassifier`
        - `SVC`
        - `GradientBoostingClassifier`

3. -------- Feature Selection -------------
    - Random Forest classifier showed the best accuracy among the others and selected the top features based on their importance.
    - Haploinsufficiency scores showed no impact on mutations .
   
4. ----------- Model Saving and Loading -------------
    - Save the trained model to a file using `joblib`.
    - Load the model from the file for future use.

5. ------------ Predictions on patient data ----------------
    - Preprocess the test data to match the training data format.
    - Make predictions using the loaded model.
    - Map predictions to the original class labels.

# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model used in this project is the Random Forest Classifier from scikit-learn.

## Intended Use

The model's intended use is to predict if an individual's salary is <= $50K or > $50K based on demographic and employment characteristics from the U.S. Census income dataset. The intended use of this model is educational and should not be used for real world business decisions.

Data source: https://archive.ics.uci.edu/dataset/20/census+income 

## Training Data

The model was trained using the U.S. Census Income dataset, source included below. The dataset contains demographic and employment information. The target variable, salary, indicates whether an individual's salary is <= $50K or > $50K. The dataset was split into a training and a test dataset with a fixed random seed (random_state=42). The training dataset includes 80% of the entire dataset, and the test dataset includes 20% of the entire dataset. The dataset was preprocessed using One-Hot encoding on categorical features and label binarization.

## Evaluation Data

The model was evaluated on the 20% test set (train_test_split). One-Hot encoding and label binarization were also applied to the test set using the encoder and label binarizer fitted on the training set. Performance metrics were calculated on overall model performance in addition to data slices for categorical features.

## Metrics

The metrics used to evaluate model performance were precision, recall, and F1 score.

Model performance values

Precision: 0.7419
Recall: 0.6384
F1 score: 0.6863

Additionally, model performance was evaluated on categorical feature slices and those metrics were saved to the file slice_output.txt. Metrics are included for features such as workclass, native-country, education, marital-status, sex, race, relationship, and occupation. 

## Ethical Considerations

The data attributes include demographic features such as race, sex, marital status, and native country, which could introduce biases resulting in variable model performance across certain demographics. As such, the model should only be used for educational purposes.

## Caveats and Recommendations

The model has several limitations to consider. The dataset used is from 1994 and represents only U.S. data. It was trained using only a single train-test split and Random Forest Classifier without hyperparameter tuning. Future model improvement could include collecting more recent data and including other country data, hyperparameter tuning and cross-validation. Additional improvements could involve evaluating data for fairness and bias across different demographic groups. As such, this model is recommended only for research and educational purposes. 
# Doing the necessary imports
from sklearn.model_selection import train_test_split
from Model_Train import tuner_model
from Data_Pfreprocessing import data_preprocessing
import files_methods

"""
This is the Entry point for Training the Machine Learning Model.
"""


def trainingModel(data):
    try:
        # Getting the data from the source

        """doing the data preprocessing"""

        # repalcing 'na' values with np.nan as discussed in the EDA part

        data = data_preprocessing.replaceInvalidValuesWithNull(data)

        # get encoded values for categorical data

        data = data_preprocessing.encodeCategoricalValues(data)

        # check if missing values are present in the dataset
        is_null_present, cols_with_missing_values = data_preprocessing.is_null_present(data)

        # if missing values are there, replace them appropriately.

        if is_null_present:
            data = data_preprocessing.handleMissingValues(data)  # missing value imputation by mean

        # Get columns with standard deviation zero

        # create separate features and labels
        X, Y = data_preprocessing.separate_label_feature(data, label_column_name='class')

        cols_to_drop = data_preprocessing.get_columns_with_zero_std_deviation(X)

        # drop the columns obtained above
        X = data_preprocessing.remove_columns(X, cols_to_drop)

        X = data_preprocessing.scale_numerical_columns(X)

        X = data_preprocessing.pcaTransformation(X)

        # handle imbalance in label column

        X, Y = data_preprocessing.handleImbalance(X, Y)

        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=1 / 3, random_state=36)

        # getting the best model for each of the clusters

        best_model_name, best_model = tuner_model.get_best_model(x_train, y_train, x_test, y_test)
        print('Successful End of Training')
        # saving the best model to the directory.

        # save_model=file_op.save_model(best_model,best_model_name+str(i))
        save_model = files_methods.save_model(best_model, best_model_name)
        print('Successful End of Training' + str(save_model))

    except Exception as e:

        raise Exception('Unsuccessful End of Training', e)

import numpy as np
import pandas as pd
import os
import gc
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE
import matplotlib


def remove_columns(data, columns):
    """
            Method Name: remove_columns
            Description: This method removes the given columns from a pandas dataframe.
            Output: A pandas DataFrame after removing the specified columns.
            On Failure: Raise Exception
    """

    try:

        useful_data = data.drop(labels=columns, axis=1)  # drop the labels specified in the columns

        return useful_data
    except Exception as e:

        raise Exception('Column removal Unsuccessful. Exited the remove_columns method of the Preprocessor class', e)


def separate_label_feature(data, label_column_name):
    """
                    Method Name: separate_label_feature
                    Description: This method separates the features and a Label Coulmns.
                    Output: Returns two separate Dataframes, one containing features and the other containing Labels .
                    On Failure: Raise Exception

    """
    try:
        X = data.drop(labels=label_column_name,
                      axis=1)  # drop the columns specified and separate the feature columns
        Y = data[label_column_name]  # Filter the Label columns

        return X, Y

    except Exception as e:
        raise Exception(
            'Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class', e)


def dropUnnecessaryColumns(data, columnNameList):
    """
                    Method Name: is_null_present
                    Description: This method drops the unwanted columns as discussed in EDA section.

                            """
    data = data.drop(columnNameList, axis=1)
    return data


def replaceInvalidValuesWithNull(data):
    """
   Method Name: is_null_present
   Description: This method replaces invalid values i.e. '?' with null, as discussed in EDA.

    """

    data.replace('na', np.NaN, inplace=True)

    return data


def is_null_present(data):
    """
    Method Name: is_null_present
    Description: This method checks whether there are null values present in the pandas Dataframe or not.
    Output: Returns True if null values are present in the DataFrame, False if they are not present and
            returns the list of columns for which null values are present.
    On Failure: Raise Exception
    """
    null_present = False
    cols_with_missing_values = []
    cols = data.columns
    try:
        null_counts = data.isna().sum()  # check for the count of null values per column

        for i in range(len(null_counts)):
            if null_counts[i] > 0:
                null_present = True
                cols_with_missing_values.append(cols[i])

        if null_present:  # write the logs to see which columns have null values
            dataframe_with_null = pd.DataFrame()
            dataframe_with_null['columns'] = data.columns
            dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
            dataframe_with_null.to_csv('preprocessing_data/null_values.csv')  # storing the null column information
            # to file

        return null_present, cols_with_missing_values
    except Exception as e:
        raise Exception('Finding missing values failed. Exited the is_null_present method of the Preprocessor class', e)


def encodeCategoricalValues(data):
    """
       Method Name: encodeCategoricalValues
       Description: This method encodes all the categorical values in the training set.
       Output: A Dataframe which has all the categorical values encoded.
       On Failure: Raise Exception

    """
    data['class'] = data['class'].map({'neg': 0, 'pos': 1})

    return data


def encodeCategoricalValuesPrediction(data):
    """
       Method Name: encodeCategoricalValuesPrediction
       Description: This method encodes all the categorical values in the prediction set.
       Output: A Dataframe which has all the categorical values encoded.
       On Failure: Raise Exception

    """

    for column in data.columns:
        data = pd.get_dummies(data, columns=[column])

    return data


def handleMissingValues(data):
    """

        Method Name: handleMissingValues
        Description: This method find the missing values and replace with the mean values particular columns.
        Output: A Dataframe which has all the  values encoded.
    """
    data = data[data.columns[data.isnull().mean() < 0.6]]

    data = data.apply(pd.to_numeric)

    for col in data.columns:
        data[col] = data[col].replace(np.NaN, data[col].mean())

    return data


def scale_numerical_columns(self, data):
    """
    Method Name: scale_numerical_columns
    Description: This method scales the numerical values using the Standard scaler.
    Output: A dataframe with scaled values
    On Failure: Raise Exception

    """
    try:

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.data)
        scaled_num_df = pd.DataFrame(data=scaled_data, columns=data.columns, index=data.index)

        return scaled_num_df
    except Exception as e:

        raise Exception('scaling for numerical columns Failed. Exited the scale_numerical_columns method of the Preprocessor class', e)


def pcaTransformation(X_scaled_data, data):
    pca = PCA(n_components=100)
    new_data = pca.fit_transform(X_scaled_data)

    principal_x = pd.DataFrame(new_data, index=data.index)

    return principal_x


def get_columns_with_zero_std_deviation(data):
    """
    Method Name: get_columns_with_zero_std_deviation
    Description: This method finds out the columns which have a standard deviation of zero.
    Output: List of the columns with standard deviation of zero
    On Failure: Raise Exception
    """

    columns = data.columns
    data_n = data.describe()
    col_to_drop = []
    try:
        for x in columns:

            if data_n[x]['std'] == 0:  # check if standard deviation is zero
                col_to_drop.append(x)  # prepare the list of columns with standard deviation zero
        return col_to_drop

    except Exception as e:
        raise Exception('Column search for Standard Deviation of Zero Failed. '
                        'Exited the get_columns_with_zero_std_deviation method of the Preprocessor class', e)


def handleImbalance(X, Y):
    sample = SMOTE()

    X_bal, y_bal = sample.fit_resample(X, Y)

    return X_bal, y_bal

import pandas
import files_methods
from Data_Pfreprocessing import data_preprocessing


def predictionFromModel(data, file_object=None):
    try:

        data = data_preprocessing.replaceInvalidValuesWithNull(data)

        is_null_present, cols_with_missing_values = data_preprocessing.is_null_present(data)
        if is_null_present:
            # data=preprocessor.impute_missing_values(data,cols_with_missing_values)
            data = data_preprocessing.handleMissingValues(data)  # missing value imputation by mean

        # we get these columns while training and we dropped them there, so we will drop it from here
        cols_to_drop = ['cd_000', 'ch_000']

        # drop the columns obtained above
        X = data_preprocessing.remove_columns(data, cols_to_drop)

        X = data_preprocessing.scale_numerical_columns(X)

        X = data_preprocessing.pcaTransformation(X)

        # data=data.to_numpy()
        file_loader = files_methods.File_Operation(file_object)

        result = []  # initialize blank list for storing predictions

        model_name = file_loader.find_correct_model_file()
        model = file_loader.load_model(model_name)
        for val in (model.predict(X)):
            result.append(val)
        result = pandas.DataFrame(result, columns=['Predictions'])
        result['Predictions'] = result['Predictions'].map({0: 'neg', 1: 'pos'})
        path = "Prediction_Output_File/Predictions.csv"
        result.to_csv("Prediction_Output_File/Predictions.csv", header=True)  # appends result to prediction file
    except Exception as ex:
        raise ex
    return path

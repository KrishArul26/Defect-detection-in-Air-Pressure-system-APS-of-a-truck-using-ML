import sqlite3
from datetime import datetime
from os import listdir
import os
import re
import json
import shutil
import pandas as pd

"""
This files shall be used for handling all the validation done on the Raw Prediction Data!!.
           
"""

Batch_Directory = 'path'
schema_path = 'schema_prediction.json'


def valuesFromSchema():
    """
    Method Name: valuesFromSchema
    Description: This method extracts all the relevant information from the pre-defined "Schema" file.
    Output: LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, Number of Columns
    On Failure: Raise ValueError,KeyError,Exception

    """

    try:
        with open(schema_path, 'r') as f:
            dic = json.load(f)
            f.close()
        pattern = dic['SampleFileName']
        LengthOfDateStampInFile = dic['LengthOfDateStampInFile']
        LengthOfTimeStampInFile = dic['LengthOfTimeStampInFile']
        column_names = dic['ColName']
        NumberofColumns = dic['Number of Columns']

        file = open("Training_Logs/valuesfromSchemaValidationLog.txt", 'a+')
        message = "LengthOfDateStampInFile:: %s" % LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile + "\t " + "NumberofColumns:: %s" % NumberofColumns + "\n"
        file.close()

    except ValueError:
        file = open("Prediction_Logs/values from    SchemaValidationLog.txt", 'a+')
        file.close()
        raise ValueError

    except KeyError:
        file = open("Prediction_Logs/values from SchemaValidationLog.txt", 'a+')
        file.close()
        raise KeyError

    except Exception as e:
        file = open("Prediction_Logs/values from SchemaValidationLog.txt", 'a+')
        file.close()
        raise e

    return LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, NumberofColumns


def manualRegexCreation():
    """
      Method Name: manualRegexCreation
      Description: This method contains a manually defined regex based on the "FileName" given in "Schema" file.
                  This Regex is used to validate the filename of the prediction data.
      Output: Regex pattern
      On Failure: None

    """
    regex = "['ApsFailure']+['\_'']+[\d_]+[\d]+\.csv"
    return regex


def validateColumnLength(NumberofColumns):
    """
    Method Name: validateColumnLength
    Description: This function validates the number of columns in the csv files.
                 It is should be same as given in the schema file.
                 If not same file is not suitable for processing and thus is moved to Bad Raw Data folder.
                 If the column number matches, file is kept in Good Raw Data for processing.
                The csv file is missing the first column name, this function changes the missing name to "Wafer".
    Output: None
    On Failure: Exception

    """

    try:

        f = open("Prediction_Logs/columnValidationLog.txt", 'a+')
        for file in listdir('Prediction_Raw_Files_Validated/Good_Raw/'):
            csv = pd.read_csv("Prediction_Raw_Files_Validated/Good_Raw/" + file)
            if csv.shape[1] == NumberofColumns:
                # csv.rename(columns={"Unnamed: 0": "Wafer"}, inplace=True)
                csv.to_csv("Prediction_Raw_Files_Validated/Good_Raw/" + file, index=None, header=True)
            else:
                shutil.move("Prediction_Raw_Files_Validated/Good_Raw/" + file, "Prediction_Raw_Files_Validated/Bad_Raw")

    except OSError:
        f = open("Prediction_Logs/columnValidationLog.txt", 'a+')
        f.close()
        raise OSError

    except Exception as e:
        f = open("Prediction_Logs/columnValidationLog.txt", 'a+')
        f.close()
        raise e

    f.close()


def deletePredictionFile(self):
    if os.path.exists('Prediction_Output_File/Predictions.csv'):
        os.remove('Prediction_Output_File/Predictions.csv')


def validateMissingValuesInWholeColumn():
    """
      Method Name: validateMissingValuesInWholeColumn
      Description: This function validates if any column in the csv file has all values missing.
                   If all the values are missing, the file is not suitable for processing.
                   SUch files are moved to bad raw data.
      Output: None
      On Failure: Exception
    """

    try:
        f = open("Prediction_Logs/missingValuesInColumn.txt", 'a+')

        for file in listdir('Prediction_Raw_Files_Validated/Good_Raw/'):
            csv = pd.read_csv("Prediction_Raw_Files_Validated/Good_Raw/" + file)
            count = 0
            for columns in csv:
                if (len(csv[columns]) - csv[columns].count()) == len(csv[columns]):
                    count += 1
                    shutil.move("Prediction_Raw_Files_Validated/Good_Raw/" + file,
                                "Prediction_Raw_Files_Validated/Bad_Raw")
                    break
            if count == 0:
                csv.rename(columns={"Unnamed: 0": "Wafer"}, inplace=True)
                csv.to_csv("Prediction_Raw_Files_Validated/Good_Raw/" + file, index=None, header=True)

    except OSError:
        f = open("Prediction_Logs/missingValuesInColumn.txt", 'a+')
        f.close()
        raise OSError

    except Exception as e:
        f = open("Prediction_Logs/missingValuesInColumn.txt", 'a+')
        f.close()
        raise e
    f.close()

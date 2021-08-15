import pickle
import os
import shutil


"""
This files shall be used to save the model after training
and load the saved model for prediction.
"""

model_directory = 'models/'


def save_model(model, filename):
    """
        Method Name: save_model
        Description: Save the model file to directory
        Outcome: File gets saved
        On Failure: Raise Exception
"""

    try:
        path = os.path.join(model_directory, filename)  # create separate directory for each cluster
        if os.path.isdir(path):  # remove previously existing models for each clusters
            shutil.rmtree(model_directory)
            os.makedirs(path)
        else:
            os.makedirs(path)  #
        with open(path + '/' + filename + '.sav',
                  'wb') as f:
            pickle.dump(model, f)  # save the model to file

        return 'success' + str(filename)

    except Exception as e:

        raise Exception('could not be saved. Exited the save_model method of the Model_Finder class', e)


def load_model(filename):
    """
                Method Name: load_model
                Description: load the model file to memory
                Output: The Model file loaded in memory
                On Failure: Raise Exception
    """
    try:
        with open(model_directory + filename + '/' + filename + '.sav',
                  'rb') as f:
            print('loaded. Exited the load_model method of the Model_Finder class')
            return pickle.load(f)

    except Exception as e:

        raise Exception(' could not be saved. Exited the load_model method of the Model_Finder class', e)

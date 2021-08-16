from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def get_best_params_for_svm(train_x, train_y):
    """
    Method Name: get_best_params_for_naive_bayes
    Description: get the parameters for the SVM Algorithm which give the best accuracy.
                 Use Hyper Parameter Tuning.
    Output: The model with the best parameters
    On Failure: Raise Exception
    """
    try:
        sv_classifier = SVC()

        # initializing with different combination of parameters
        param_grid = {"kernel": ['rbf', 'sigmoid'],
                      "C": [0.1, 0.5, 1.0],
                      "random_state": [0, 100, 200, 300]}

        # Creating an object of the Grid Search class
        grid = GridSearchCV(estimator=sv_classifier, param_grid=param_grid, cv=5, verbose=3)
        # finding the best parameters
        grid.fit(train_x, train_y)

        # extracting the best parameters
        kernel = grid.best_params_['kernel']
        C = grid.best_params_['C']
        random_state = self.grid.best_params_['random_state']

        # creating a new model with the best parameters
        sv_classifier = SVC(kernel=kernel, C=C, random_state=random_state)
        # training the mew model
        sv_classifier.fit(train_x, train_y)

        return sv_classifier

    except Exception as e:

        raise Exception('SVM training  failed. Exited the get_best_params_for_svm method of the Model_Finder class', e)


def get_best_params_for_KNN(self, train_x, train_y):
    """
    Method Name: get_best_params_for_KNN
    Description: get the parameters for KNN Algorithm which give the best accuracy.
                 Use Hyper Parameter Tuning.
    Output: The model with the best parameters
    On Failure: Raise Exception

    """

    try:
        knn = KNeighborsClassifier()
        # initializing with different combination of parameters
        param_grid_knn = {
            'algorithm': ['ball_tree', 'kd_tree'],
            'leaf_size': [10, 17, 24, 28, 30, 35],
            'n_neighbors': [4, 5, 8, 10, 11],
            'p': [1, 2]
        }

        # Creating an object of the Grid Search class
        grid = GridSearchCV(knn, param_grid_knn, verbose=3,
                            cv=4)
        # finding the best parameters
        grid.fit(train_x, train_y)

        # extracting the best parameters
        algorithm = grid.best_params_['algorithm']
        leaf_size = grid.best_params_['leaf_size']
        n_neighbors = grid.best_params_['n_neighbors']
        p = grid.best_params_['p']

        # creating a new model with the best parameters
        knn = KNeighborsClassifier(algorithm=algorithm, leaf_size=leaf_size,
                                   n_neighbors=n_neighbors, p=p, n_jobs=-1)
        # training the mew model
        knn.fit(train_x, train_y)

        return knn
    except Exception as e:

        raise Exception('knn Parameter tuning  failed. Exited the knn method of the Model_Finder class', e)


def get_best_model(train_x, train_y, test_x, test_y):
    """
    Method Name: get_best_model
    Description: Find out the Model which has the best AUC score.
    Output: The best model name and the model object
    On Failure: Raise Exception
    """

    # create best model for get_best_params_for_KNN
    try:
        knn = get_best_params_for_KNN(train_x, train_y)
        prediction_knn = knn.predict(test_x)  # Predictions using the XGBoost Model

        if len(test_y.unique()) == 1:
            # if there is only one label in y, then roc_auc_score returns error.
            # We will use accuracy in that case
            knn_score = accuracy_score(test_y, prediction_knn)
            print('Accuracy for Knn:' + str(knn_score))
        else:
            knn_score = roc_auc_score(test_y, prediction_knn)  # AUC for KNN

            print('AUC for KNN:' + str(knn_score))

        # create best model for svm
        svm = get_best_params_for_svm(train_x, train_y)
        prediction_svm = svm.predict(test_x)  # prediction using the SVM Algorithm

        if len(test_y.unique()) == 1:
            # if there is only one label in y, then roc_auc_score returns error.
            # We will use accuracy in that case
            svm_score = accuracy_score(test_y, prediction_svm)
            print('Accuracy for SVM:' + str(svm_score))

        else:
            svm_score = roc_auc_score(test_y, prediction_svm)  # AUC SVM
            print('AUC for SVM:' + str(svm_score))


        # comparing the two models
        if svm_score < knn_score:
            return 'KNN', knn
        else:
            return 'SVM', svm

    except Exception as e:

        raise Exception('Model Selection Failed. Exited the get_best_model method of the Model_Finder class', e)

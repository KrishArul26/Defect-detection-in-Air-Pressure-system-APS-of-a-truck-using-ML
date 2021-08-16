<h2 align="center"> Defect-detection-in-Air-Pressure-system-APS-of-a-truck-using-ML</h2>

<h2 align="left">Introduction</h2>

<p style= 'text-align: justify;'> The dataset consists of data collected from heavy Scania trucks in everyday usage. The system in focus is the Air Pressure system (APS) which generates  pressurised air that is utilized in various functions in a truck, such as braking and gear changes. The dataset’s positive class consists of component failures for a 
specific component of the APS system. The negative class consists of trucks with failures for components not related to the APS. So, I created a model where It can able 
to detect whether the APS is going to fail or Not. Further, The attribute names of the data have been anonymized for proprietary reasons.
Challenge metric:
 
<h1 align="center"> <span style="color:green">Missing Values, PCA, SMOTE, KNN, SVM, Hyperparametrs Tuning, Pickle, F1-Score and AUC - Values.</span></h1>
 
                 * Cost-metric of miss-classification
 
                 * Predicted class | True class |#
 
                 | pos | neg |
 
 
                 pos | - | Cost_1 |
 
 
                 neg | Cost_2 | - |

 
 
 
Cost_1 = 10 and cost_2 = 500
 
The total cost of a prediction model the sum of 'Cost_1' multiplied by the number of Instances with type 1 failure and 'Cost_2' with the number of instances with type 2 failure, resulting in a 'Total_cost'.
 
 
In this case Cost_1 refers to the cost that an unnessecary check needs to be done by an mechanic at an workshop, while Cost_2 refer to the cost of missing a faulty truck, which may cause a breakdown.
 
Total_cost = Cost_1No_Instances + Cost_2No_Instances.
 
•	The training set contains 60000 examples in total in which 59000 belong to the negative class and 1000 positive class. The test set contains 16000 examples.
 
•	Number of Attributes: 171
 
•	Attribute Information: The attribute names of the data have been anonymized for proprietary reasons. It consists of both single numerical counters and histograms consisting of bins with different conditions. Typically the histograms have open-ended conditions at each end. For example if we measuring the ambient temperature 'T' then the histogram could be defined with 4 bins where:
 
            •	bin 1 collect values for temperature T < -20
                                                          
            •	bin 2 collect values for temperature T >= -20 and T < 0
                                                                     
            •	bin 3 collect values for temperature T >= 0 and T < 20
                                                                    
            •	bin 4 collect values for temperature T > 20</p>
  
<p align="left">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/129486706-6ef0fa0b-721c-427f-81f5-a57494c30dcc.jpeg">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/129486713-9612c049-b39a-4264-812c-df2cba00e2db.jpeg">
  
</p> 
 

<h2 align="left">Files Descriptions</h2>
 
 <p style= 'text-align: justify;'> 
  
              1.	Data Preprocessing Folder: This folder only contains preprocessing file which is needed for remove_columns, 
  
                 separate label feature, replace invalid values with Null, finding the null values present in the dataset, 
  
                 encodes all the categorical values in the training set to numeric values, the method finds the missing  
  
                 values, method scales the numerical values, dealing with Dimensanility reduction  techniques using  PCA, 
   
                 the method finds out the columns which have a standard deviation of zero, 
  
                 The methods handle the Imbalance the dependent variables using SMOTE.
  
              2.	EDA: This folder only contains the Jupyter Notebook and the sample data files. 
  
              3.	Model_Train Folder: This folder only contains model_training.py and tuner.py files.
  
                               a.	tuner.py: This file contains all necessary coding for initializing the SVM, KNN parameters in order to 
               
                                   get the best prediction with good accuracy using GridsearchCV. Finally, It will return the best model. 
            
                               b.	model_training.py: It has all coding for trained the model and saves the model in the working directory. 
  
              4.	Models: Only contain the KNN model which we used to train the model.
  
              5.	Files_models.py: This file contains coding for the save the trained model and loads the model.
  
              6.	predictionFrom_Model.py: This file is only for predicting the unseen data
  
              7.	Main.py: For predicting the Unseen data whether the truck’s APS  is going to fail or not
  
</p>
 
<h2 align="left">Data Preprocessing</h2>
 
 
 
<p style= 'text-align: justify;'> 

               1.	Remove Unnecessary Columns

               2.	Separate Label Feature

               3.	Replace Invalid Values With Null

               4.	Finding The Null Values Present In The Dataset

               5.	Encodes All The Categorical Values In The Training Set To Numeric Values

               6.	Missing Values Replace With Mean

               7.	Scales The Numerical Values Using Standardscaler

               8.	Dimensionality Reduction Using  PCA

               9.	Remove Columns Which A Standard Deviation Of Zero

               10.	Balance The Dependent Variables Using SMOTE 
</p>

 
<h2 align="left"> Model Selection </h2>
 
<p style= 'text-align: justify;'>  We are using two algorithms, "SVM" and "KNN". The data is trained on both the 
algorithms with the hyper parameters for each algorithoms which is derived from GridSearch. We calculate the AUC scores for both 
models and select the model with the best score.</p>
 
<h2 align="left">  Prediction </h2>
 
<p style= 'text-align: justify;'> 
 
                1.	Data Export from Db - The data in the stored database is exported as a CSV file to be used for prediction. 

                2.	Data Preprocessing 

                                      a) Replace the invalid values with numpy “nan” so we can use imputer on such values. 


                                      b) Check for null values in the columns. If present, impute the null values using the mean.


                3.	Prediction - The respective model is loaded and is used to predict the data. 

                4.	Once the prediction is made, the predictions along with the original names before label encoder are saved in 

                   a CSV file at a given location  and the location is returned to the working directory.
 </p>

 
<h2 align="left"> Result of KNN Model</h2>
 
<h3 align="left">Confusion Matrix </h3>
 
 <p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/129513771-786624f8-40fb-4b1c-ae97-db97856e4255.png">
  
</p> 
 
 
 <h3 align="left">Precision - Recall Curve For KNN  </h3>
 
 <p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/129513861-848fe6b9-83e2-41d0-9275-9b7ecd5d9939.png">
  
</p> 
 
<h3 align="left"> ROC Curve For KNN  </h3>
 
<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/129513922-b4005f16-d98d-4d00-b258-bdcc6fcd70fd.png">
  
</p> 
 


















# Predictive Models and Analytics related to User Profile

This repo serves as a demo for churn prediction model and gender prediction model trained on users' in-app activity data for a news feed mobile app. For illustration purpose, all data presented in this repo are synthesized data only. For deployment, API is called to query data from Redshift database and make real-time prediction for a particular user.  


## Churn Prediction Model and Churn Cohort Analysis
* See `demo-churn-prediction.ipynb`

 | 					              | Description                                          | 
 | ------------------------------ | :----------------------------------------------------|
 | Problem              		  | Predict churn score in the next 30 days of app users based on their recent 90-day in-app behaviour | 
 | Dataset               		  | 150k app users, a total of 24 features such as number of active days, events clicks, average session time, push notification received, block activities, browsing activity| 
 | Model       					  | XGBoost                                              |
 | Performance                    | AUC 0.83, Accuracy 0.84 on 20% test set       |


* Visualization fo Churn Cohort Analysis
![plot](https://github.com/sukilau/demo-userprofile-predictive-models/blob/master/plot/heatmap_by_month.png)


## Gender Prediction Model

* See `demo-gender-prediction.ipynb`
 | 					              | Description                                          | 
 | ------------------------------ | :----------------------------------------------------|
 | Problem              		  | Predict users' gender based on their recent 120-day browsing history in various news channels | 
 | Dataset               		  | 5k app users, a total of 163 feataures representing the number of news feed read by a user in selected channels| 
 | Model       					  | XGBoost                                              |
 | Performance                    | AUC 0.83, Accuracy 0.77 on 20% test set       |


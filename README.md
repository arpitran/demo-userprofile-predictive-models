# Demo - Predictive Models and Analytics related to User Profile

This repo serves as demo for the churn prediction model and the gender prediction model built based on users' in-app activity data of a news feed mobile app. For illustration purpose, all data presented in this repo are synthesized data only.

---
## Churn Cohort Analysis and Churn Prediction Model
* See `demo-churn-prediction.ipynb`

 | 					              | Description                                          | 
 | ------------------------------ |-----------------------------------------------------:|
 | Problem              		  | Predict churn score in the next 30 days of app users based on their recent 90-day in-app behaviour | 
 | Dataset               		  | 150k app users, a total of 24 features such as total number of active days, number of events clicks, average session time, number of push notification received, block activities, browsing activity   | 
 | Model       					  | XGBoost                                              |
 | Performance                    | 0.84 accuracy and 0.83 AUC on the 20% test set       |


![plot](https://github.com/sukilau/demo-userprofile-predictive-models/blob/master/plot/heatmap_by_month.png)



## Gender Prediction Model

* See `demo-gender-prediction.ipynb`



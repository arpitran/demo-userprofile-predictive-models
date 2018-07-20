import numpy as np
import pandas as pd
from sklearn.metrics import *

def evaluate(y_pred, y_true):
    acc = accuracy_score(y_pred, y_true)
    auc = roc_auc_score(y_pred, y_true)
    precision = precision_score(y_pred, y_true)
    recall = recall_score(y_pred, y_true)
    f1score = f1_score(y_pred, y_true)   
    print ("Accuracy : {:.4f}".format(acc))
    print("AUC score : {:.4f}".format(auc))
    print("Precision : {:.4f}".format(precision))
    print("Recall : {:.4f}".format(recall))
    print("F1 score : {:.4f}".format(f1score))
    print("\nClassification report : \n", classification_report(y_pred, y_true))
    print("\nConfusion matrix : \n", confusion_matrix(y_pred, y_true))
    return acc, auc, precision, recall, f1score

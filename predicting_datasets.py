# -*- coding: utf-8 -*-
"""predicting_datasets

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15UexWGwfHKuXu-dOvIvhKa-G366Pd91A
"""

from google.colab import drive
drive.mount("/content/drive/")

import pandas as pd
import numpy as np
import tensorflow as tf
import logging
import os

#These are save locations
og_dataset_location = "/content/drive/My Drive/Colab Notebooks/Personal/predicting_missing_values/datasets/unsorted/"
dataset_for_training = "/content/drive/My Drive/Colab Notebooks/Personal/predicting_missing_values/datasets/sorted/"
dataset_after_prediction = "/content/drive/My Drive/Colab Notebooks/Personal/predicting_missing_values/datasets/predictedData/"

class data:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

new = data("sam")
print(new)

class dataset_sorting:
    def __int__(self, file_name):
        self.file_name = file_name
        self.location = "/content/drive/My Drive/Colab Notebooks/Personal/predicting_missing_values/datasets/unsorted/kidney_disease.csv"
        self.original_dataframe = self.load_dataset()
        self.new_dataset = None
        self.empty_Value_rows = None
        self.fixed_data = "/content/drive/My Drive/Colab Notebooks/Personal/predicting_missing_values/datasets/sorted/"
        self.dataframe_as_list = None
        #self.deep_learning_model
    
    def __str__(self):
        return f"The data{file}"

    def load_dataset(self) -> pd.DataFrame or None:
        try:
            file = pd.read_csv(self.location)
            print("Loading dataset")
            return file
        except FileNotFoundError:
            print(f"The file in {self.location} does not exist.")
            return None
        except:
            print("load_dataset: Error not accounted for.")
            return None

    def seperate_data(self):
        if(self.original_Dataframe.isnull().values.ravel().sum()) > 0:
            print(f"The amount of NaN/Null's in the data is {(self.original_Dataframe.isnull().values.ravel().sum())}")
            dataframe = self.original.dropna()
            if (dataframe.isnull().values.ravell().sum()) == 0:
                self.new_dataset = dataframe
        else:
            print(f"There are no nulls in the data.")
            self.sorted = True
            self.new_dataset = self.original_Dataframe
        dataset_list = self.original_dataframe.values.tolist()
        rows = []
        for index in dataset_list:
            for element in index:
                if element is None:
                    rows.append(index)
        print(rows)        
        

    def save_to_csv(self):
        self.new_Dataframe.to_csv(self.new_dataset)
    
    def to_list(self):
        self.dataframe_as_list = ps.DataFrame.values.tolist(self.new_dataset)

    def deep_learning_model(self):
        logger = tf.get_logger()
        logger.setLevel(logging.ERROR)

file_list = os.listdir("/content/drive/My Drive/Colab Notebooks/Personal/predicting_missing_values/datasets/unsorted/")
object_instance_list = []
print(file_list)

for x in file_list:
    data = Dataset_Sorting(x)
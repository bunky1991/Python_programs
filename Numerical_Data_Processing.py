import os
import sys
import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import matplotlib.pyplot as plt


class Data_Processing:
    def __init__(self, location: str, file_name: str) -> None:
        """ 
        :param file_name: name of the file
        :param location: Location where file is stored
        :param dataframe: file opened into dataframe
        :param check_data: checks if the data type is numerical
        :param column_names: list of names of columns in the dataframe 
        :param data_type: Data type of the data
        :param save_preTrained_location: location to save sorted dataframe
        :param sorted: If data has been sorted 
        :param extracted_features: creates new features form the existing data
        :param extracted_targets: creates targets
        :param features_and_targets: call function to fill previous 2 parameters
        :param dataset_usable: This returns True or false whether the data can be used.
        :param save_to_csv: Saved sorted dataframe to a new csv file
        :return: None
        """
        self.location = location
        self.dataframe = self.Load_DataSet()
        self.file_name = file_name.replace(".csv", "") if ".csv" in file_name else file_name
        self.check_data()
        self.column_names = self.columns()
        self.data_type = self.check_type()
        """if self.dataset_usable:
            print("Dataset is useable, please proceed")
        elif self.dataset_usable == None:
            print("A error occured during checking functions for data useability.")
        else:
            print("Dataset return false, please check dataset is a formatted correctly")"""
        self.save_preTrained_location = "/content/drive/My Drive/Colab Notebooks/Dissertation/Tensorflow_DataSets/Sorted_Data/"
        self.sorted = False
        self.extracted_features = None
        self.extracted_targets = None
        self.features_and_targets()
        #self.dataset_usable = self.dataset_use_ability
        #if sorted:
           #self.save_to_csv()
 
    def __str__(self) -> str:
        """
        Prints a description of the class object
        :return: string of Details of object 
        """
        if self.data_type == "Numerical":
            return f"Data information:\nLocation: {self.location}\ndata type: {self.data_type}\nfile name: {self.file_name}\nNumber of columns: {len(self.column_names)}\nAmount of rows: {self.dataframe.shape[0]}\n"
        else:
            return f"Data information:\nLocation: {self.location}\ndata type: The columns that are numerical are {self.data_type}\nfile name: {self.file_name}\nNumber of columns: {len(self.column_names)}\nAmount of rows: {self.dataframe.shape[0]}\n"
        
    def dataset_use_ability() -> bool or None:
        issue_list = []
        try:
            issue_list.append("dataframe" if self.dataframe == None else None)
            issue_list.append("check_type" if self.data_type == None else None) 
            issue_list.append("check_data" if self.column_names == None else None)
            isses_list.append("column_names" if self.check_data == None else None)
            if self.check_type or self.check_data or self.column_names == None:
                print(f"Dataset is not usable in this state: Issue with {x for x in issue_list if x != None}")
                return False
            else:
                print("No issues have been found")
                return True
        except:
            print("Unknown error: dataset_use_ability")
            return None

    def Load_DataSet(self) -> pd.DataFrame or None:
        """
        Opens the csv file with pandas and is returned a dataframe
        :return: returns data loaded using pandas
        """
        try:
            file = pd.read_csv(self.location)
            return file
        except FileNotFoundError:
            print(f"The file in {self.loaction} does not exist.")
            return None
        except:
            print("Load_DataSet: Error not accounted for.")
            return None
 
    def check_type(self, is_numeric=None) -> str or [str] or None:
        """
        :param is_numeric: True or False if column is numerical in dataframe
        :return: Will return a string if all data is numerical, otherwise will return a list with all the column names that can be used
        """
        try:
            if is_numeric is None:
                is_numeric = []
            for i in range(len(self.column_names)):
                if is_numeric_dtype(self.dataframe[self.column_names[i]]):
                    is_numeric.append(True)
                else:
                    self.convert_string_columns(self.column_names[i])
                    if is_numeric_dtype(self.dataframe[self.column_names[i]]):
                        is_numeric.append(True)
                    else:
                        self.dataframe = self.dataframe.drop(columns=self.column_names[i]) 
            if all(is_numeric):
                return "Numerical"
            else:
                numerical_list = []
                for is_True in range(len(self.column_names)):
                    if is_numeric[is_True]:
                        numerical_list.append(self.column_names[is_True])       
                return numerical_list
        except TypeError:
            print(f"Check_Type: Type Error: 1:\nShould return  {len(self.column_names)} but returned {len(is_numeric)}.")
            return None
        except ValueError:
            print(f"Check_Type: Value Error: 2:\nIssue is with {print(self)}")
            return None
        except:
            print("Check_Type: Unknown Error: 3: Issue not accounted for.")
            return None
        
    def save_to_csv(self) -> None:
        """
        Saves the sorted data frame as a new csv
        :return: Doesn't return anything for this
        """
        self.dataframe.to_csv(self.save_preTrained_location + self.file_name + ".csv" )
 
    def show_head(self) -> None:
        if self.data_type == "Numerical":
            print(', '.join(self.column_names))
        elif self.data_type != "Numerical":
            print(', '.join(self.data_type))
 
    def columns(self, column_names=None) -> [str] or None:
        """
        gets list of column names
        :param column_names: list of column names
        :return: returns a list containing strings
        """
        try:
            if column_names is None:
                column_names = []
            file = pd.read_csv(self.location)
            for column in file.columns:
                column_names.append(column)
            return column_names
        except ValueError:
            print("Value Error 1: function name: columns:")
            return None
        except:
            print("Unknon Error 2: function name: columns:")
            return None
    
    def convert_string_columns(self, column_to_change: str) -> None:
        unique_values = self.dataframe[column_to_change].unique()
        for index, word in enumerate(unique_values):
            self.dataframe[column_to_change] = self.dataframe[column_to_change].replace([word],index)
        print(f"Converted string's to integer's in {self.file_name}. Column name {column_to_change}")
        print(f"{column_to_change} was {unique_values}")
        print(f"{column_to_change} now {self.dataframe[column_to_change].unique()}")


    def check_data(self) -> pd.DataFrame or None:
        """
        Used to check the data has no NaN/Null's, then will remove them and and will return a new dataframe.
        :return: either the original dataframe or new dataframe containing no null's or returns None
        """
        try:
            if (self.dataframe.isnull().values.ravel().sum()) > 0:
                print(f"The amount of NaN/Null's in the data is {(self.dataframe.isnull().values.ravel().sum())}")
                dataframe2 = self.dataframe.dropna()
                if (dataframe2.isnull().values.ravel().sum()) == 0:
                    print(f"There are no more NaN/Null's in {self.file_name} in location {self.location}.")
                    return dataframe2
                else:
                    print("There are NaN/Null's that cant be removed this way.\nPlease do it manually.")
                    userinput = input("Would you like to continue: Y or N").upper()
                    if userinput == "Y":
                        self.sorted = True
                        return dataframe2
                    elif userinput == "N":
                        self.sorted = False
                        return None
                    else:
                        print("The option you chose was not in the choice. Default action: stopping")
                        self.sorted = False
                        return None
            else:
                print(f"There are no nulls in the data.")
                self.sorted = True
                return self.dataframe
        except FileNotFoundError:
            print(":File not found:")
            self.sorted = False
            return None
        except TypeError:
            print("Please check the data, there is a type error. ")
            self.sorted = False
            return None
        except:
            print("Check_data: Unknown Error 1:")
            self.sorted = False
            return None
    
    def features_and_targets(self) -> None:
        """
        This function is finding out from the user which 
        :param extracted_features: will have a type of pandas.core.frame.DataFrame
        :param extracted_targets: will have a type pandas.core.series.Series
        :return: None
        """
        try:
            print("Choose a column: ", end=" ")
            for name in self.column_names:
                print(f"{name}", end=", ")
            columns_NOT_use = []
            while True:
                amount_of_features = int(input("How many faetures are being used: "))
                for i in range(amount_of_features):
                    while True:
                        user_input = str(input("Enter column to not use ->> "))
                        if user_input in self.column_names:
                            columns_NOT_use.append(user_input)
                            break
                        else:
                            print("Please try again, the column you entered is nto in the list!")
            self.extracted_features = self.dataframe.loc[:, self.dataframe.columns[x for x in amount_NOT_use]]
            print("Choose a column: ", end=" ")
            for name in self.column_names:
                print(f"{name}", end=", ")
            columns_NOT_use = []
            while True:
                column_target = str(input("Enter target column ->> "))
                if column_target in self.column_names:
                    self.extracted_targets = self.dataframe.iloc[:, column_target]
        except TyprError:
            print("features_and_targets: Type error: 1")
        except ValueError:
            print("features_and_targets: Value error: 2")
        except:
            print("features_and_targets: Unknown error")
 
    def plot_data(self) -> None:
        """
        Plots data with scatter and plot
        :return: Nothing
        """
        while True:
            graph_names = ["scatter", "Box"]
            print("Please choose a plot: ")
            for index, name in enumerate(graph_names):
                print(f"{index}: {name}")
            user_choice = input("Which plotting would like to use: ")
            if user_choice in graph_names:
                if user_choice == "scatter":
                    while True:
                        print("Column names:")
                        self.show_head()
                        X_value = str(input("Which column for X: "))
                        Y_value = str(input("Which column for Y: "))
                        try:
                            if X_value in self.column_names and Y_value in self.column_names:
                                plt.scatter(self.dataframe[X_value], self.dataframe[Y_value])
                                plt.xlabel = X_value
                                plt.ylabel = Y_value
                                plt.show()
                                break
                            else:
                                if X_value in self.column_names:
                                    print(f"{Y_value} is not in the column names. Please try again.")
                                else:
                                    print(f"{X_value} is not in the column names. Please try again.")
                        except TypeError:
                            print("Error 1: Type error")
                        except:
                            print("Error 2: Unknown error")
                elif user_choice == "Box":
                    while True:
                        columns_to_show = []
                        self.show_head()
                        amount_of_columns = int(input("How many columns would you like to use? "))
                        if amount_of_columns <= len(self.column_names):
                            for i in range(amount_of_columns):
                                user_column_selection = input("Enter column name: ")
                                if user_column_selection in self.column_names:
                                    columns_to_show.append(user_column_selection)
                                    i = len(user_column_selection)
                                else:
                                  print("that is not a column in this data")
                            boxplot = self.dataframe.boxplot(column=columns_to_show)
                            plt.show()
                            break            
                        else:
                            print("""you have eneterd a number that is larger 
                                      than the amount of columns you have availbe""")
                user_choice = input("Try again: Y or N")
                if user_choice == "Y":
                    continue
                else:
                    break
            else:
                print("The graph you have chosen is not supported.\nPlease try again")

 

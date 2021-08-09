import os
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
        :param column_names: list of names of columns in the dataframe 
        :param data_type: Data type of the data
        :param save_preTrained_location: location to save sorted dataframe
        :param sorted: If data has been sorted 
        :return: None
        """
        self.file_name =  file_name.replace(".csv", "") if ".csv" in file_name else file_name
        self.location = location
        self.dataframe = self.Load_DataSet()
        self.check_data()
        self.column_names = self.columns()
        self.data_type = self.check_type()
        self.save_preTrained_location = "dir location"
        self.sorted = False
        self.extracted_features = None
        self.extracted_targets = None
        self.features_and_targets()
        if sorted:
            self.save_to_csv()
  
  def __str__(self) -> str:
        """
        Prints a description of the class object
        :return: string of Details of object 
        """
        if self.data_type == "Numerical":
            return f"Data information:\nLocation: {self.location}\ndata type: {self.data_type}\nfile name: {self.file_name}\nNumber of columns: {len(self.column_names)}\nAmount of rows: {self.dataframe.shape[0]}\n"
        else:
            return f"Data information:\nLocation: {self.location}\ndata type: The columns that are numerical are {self.data_type}\nfile name: {self.file_name}\nNumber of columns: {len(self.column_names)}\nAmount of rows: {self.dataframe.shape[0]}\n"
 
  def Load_DataSet(self) -> pd.DataFrame:
        """
        Just opens the csv file with pandas
        :return: returns data loaded with pandas
        """
        file = pd.read_csv(self.location)
        return file
 
    def check_type(self, is_numeric=None) -> str or [str]:
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
            print("Check_Type: Unknown Error: 3: Issues not accounted for.")
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
 
    def check_data(self) -> pd.DataFrame or None:
        """
        Used to check the data has no NaN/Null's
        :return: New dataframe containing no null's or returns None
        """
        #if a row has a null then the row will be removed, same proccess to all dataset's to make it fair
        try:
            #for i in self.dataframe.index:
                #if (self.dataframe.loc[i].isnull().sum() != 0):
                    #print('Missing value at ', i)
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
                        return dataframe2
                    elif userinput == "N":
                        return None
                    else:
                        print("The option you chose was not in the choice. Default action: stopping")
                        return None
            else:
                print(f"There are no nulls in the data.")
                self.sorted = True
                return self.dataframe
        except FileNotFoundError:
            print(":File not found:")
            return None
        except TypeError:
            print("Please check the data, there is a type error. ")
            return None
        except:
            print("Check_data: Unknown Error 1:")
            return None
    
    def features_and_targets(self) -> None:
        """
        extracted_features will have a type of pandas.core.frame.DataFrame
        extracted_targets will have a type pandas.core.series.Series
        :return: None
        """
        try:
            self.extracted_features = self.dataframe.loc[:, self.dataframe.columns != 'target']
            self.extracted_targets = self.dataframe.iloc[:, -1]
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

 

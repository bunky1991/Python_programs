import pandas as pd
import csv

def open_csv() -> None:
    """
    :return: None
    """
    doesFileExist = input("Does the file already exist: ").lower()
    if doesFileExist == "no":
        fileName = input("Enter new file name: ")
        path = input("Enter file path in the following format: C:\\Desktop\\Folder\\CSVFiles\\")
        try:
            with open(path + fileName + ".csv", "w") as file:
                writer = csv.writer(file)
                addNext = True
                wordList = []
                while addNext:
                    for i in range(5):
                        word = input("Enter a word to add to list: ")
                        wordList.append(word)
                    next = input("Do you want to add another 5")
                    if next == "Yes" or next == "yes":
                        pass
                    elif next == "No" or next == "no":
                        addNext = False
                writer.writerow(wordList)

            with open(path + fileName, "w") as file:
                print(file)

        except FileExistsError:
            print("File already exists")
        except FileNotFoundError:
            print(f"Couldnt find the file at {path}")
        except:
            print("Unknown error occured.")

    if doesFileExist == "yes":
        fileName = input("Enter new file name: ")
        path = input("Enter file path in the following format: C:\\Desktop\\Folder\\CSVFiles\\")
        try:
            with open(path + fileName + ".csv", "a") as file:
                writer = csv.writer(file)
                addNext = True
                wordList = []
                while addNext:
                    for i in range(5):
                        word = input("Enter a word to add to list: ")
                        wordList.append(word)
                    next = input("Do you want to add another 5")
                    if next == "Yes" or next == "yes":
                        pass
                    elif next == "No" or next == "no":
                        addNext = False
                writer.writerow(wordList)

            with open(path + fileName, "w") as file:
                print(file)

        except FileExistsError:
            print("File already exists")
        except FileNotFoundError:
            print(f"Couldnt find the file at {path}")
        except:
            print("Unknown error occured.")




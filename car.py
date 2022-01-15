import pandas as pd

data = pd.read_csv('Projects\carprice\Cardata.csv')

def headerlist():
    listOfHeader = list()
    for i in data:
        listOfHeader.append(i)
    return listOfHeader

currentIndex = "Car_Id"
data.set_index(currentIndex, inplace=True)
info = data.loc[1]







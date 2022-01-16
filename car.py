import pandas as pd

<<<<<<< HEAD
data = pd.read_csv('Cardata.csv')
=======
data = pd.read_csv('Projects\carFinding\Cardata.csv')
>>>>>>> 4ccd1328f00effc7831fef0d066247826d7124dd

def headerlist():
    listOfHeader = list()
    for i in data:
        listOfHeader.append(i)
    return listOfHeader
 
currentIndex = "Car_Id"
data.set_index(currentIndex, inplace=True)
info = data.loc[1]







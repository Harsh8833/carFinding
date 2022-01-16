import pandas as pd

data = pd.read_csv('Projects\carFinding\Cardata.csv')


def headerlist():
    listOfHeader = list()
    for i in data:
        listOfHeader.append(i)
    return listOfHeader


sampleDict = {'WheelBase': '105-120',
              'CylinderNumber': 'four-six',
              'CityMPL': '17-24',
              'FuelType': 'Petrol',
              'PeakRPM': '4000-4750(low)',
              'CylinderNumber': 'four-six',
              'CityMPL': '17-24',
              'FuelType': 'Petrol',
              'HighwayMPL': '14-18'}


def filterdata(filterDict):
    
    
    for key in filterDict:
        currentIndex = key
        data.set_index(currentIndex, inplace=True)
        info = data.loc[filterDict[key]]
        print(info)
        print('++++++++++++++++++++++++++++++++++++')
        


    #print(filterDict)

filterdata(sampleDict)

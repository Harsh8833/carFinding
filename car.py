import pandas as pd

data = pd.read_csv('Projects\carFinding\Cardata.csv')


def headerlist():
    listOfHeader = list()
    for i in data:
        listOfHeader.append(i)
    return listOfHeader


sampleDict = {'Symboling': 'Risk'}
sampleDict1 = {'WheelBase': '105-120',
               'CylinderNumber': 'four-six',
               'CityMPL': '17-24',
               'FuelType': 'Petrol',
               'PeakRPM': '4000-4750(low)'}

filterConditions = {'Symboling': {'Safe': [-2, -1],
                                  'Medium': [0, 1],
                                  'Risk': [2, 3]},
                    'FuelType': {'Petrol': 'petrol',
                                 'Diesel': 'diesel'},
                    'DoorNumber': ['Two', 'Four'],
                    'CarBody': ['Convertible', 'Sedan', 'Hatch Back', 'SUV'],
                    'DriveWheel': ['RWD', 'FWD', '4WD'],
                    'WheelBase': ['88-95', '95-105', '105-120'],
                    'CurbWeight': ['below 2200', 'above 2200'],
                    'CylinderNumber': ['two-three', 'four-six', 'eight-twelve'],
                    'Horsepower': ['less than 200', '200 to 250', '250 and above'],
                    'PeakRPM': ['4000-4750(low)', '4751-5000(medium)', '5000-6000(high)'],
                    'CityMPL': ['12-16', '17-24', '25-35', '36 and above'],
                    'HighwayMPL': ['14-18', '19-26', '27-35', '36 and above']}


def filterdata(filterDict):
    for key in filterDict:
        currentIndex = key
        data.set_index(currentIndex, inplace=True)
        info = data.loc[filterConditions[key][filterDict[key]]]
        print(info)

    # print(filterDict)


filterdata(sampleDict)

import pandas as pd




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
                    'DoorNumber': {'Two': 'two',
                                   'Four': 'four'},
                    'CarBody': {'Convertible': 'convertible',
                                'Sedan': 'sedan',
                                'Hatch Back': 'hatchback',
                                'SUV': 'suv'},
                    'DriveWheel': {'RWD': 'rwd',
                                   'FWD': 'fwd',
                                   '4WD': '4wd'},
                    'WheelBase': {'88-95': [range(88, 95, 0.1)],
                                '95-105':'',
                                '105-120':''},
                    'CurbWeight': ['below 2200':, 'above 2200'],
                    'CylinderNumber': ['two-three', 'four-six', 'eight-twelve'],
                    'Horsepower': ['less than 200', '200 to 250', '250 and above'],
                    'PeakRPM': ['4000-4750(low)', '4751-5000(medium)', '5000-6000(high)'],
                    'CityMPL': ['12-16', '17-24', '25-35', '36 and above'],
                    'HighwayMPL': ['14-18', '19-26', '27-35', '36 and above']}


def filterdata(filterDict):
    data = pd.read_csv('Projects\carFinding\Cardata.csv')
    for key in filterDict:
        currentIndex = key
        data.set_index(currentIndex, inplace=True)
        resultData = data.loc[filterConditions[key][filterDict[key]]]
        print(resultData)

    # print(filterDict)


filterdata(sampleDict)

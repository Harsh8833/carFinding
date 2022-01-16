import pandas as pd


sampleDict = {'FuelType': 'Petrol',
              'Symboling': 'Safe',
              'DoorNumber': 'Four',
              'CarBody': 'Sedan',
              'DriveWheel': 'FWD'}

sampleDict1 = {'WheelBase': '105-120',
               'CylinderNumber': 'four-six',
               'CityMPL': '17-24',
               'FuelType': 'Petrol',
               'PeakRPM': '4000-4750(low)'}

filterConditions = {'Symboling': {'Safe': 'Symboling < 0',
                                  'Medium': 'Symboling == 0 & Symboling == 1',
                                  'Risk': 'Symboling > 1'},
                    'FuelType': {'Petrol': "FuelType == 'petrol'",
                                 'Diesel': "FuelType == 'diesel'"},
                    'DoorNumber': {'Two': "DoorNumber == 'two'",
                                   'Four': "DoorNumber == 'four'"},
                    'CarBody': {'Convertible': "CarBody == 'convertible'",
                                'Sedan': "CarBody == 'sedan'",
                                'Hatch Back': "CarBody == 'hatchback'",
                                'SUV': "CarBody == 'suv'"},
                    'DriveWheel': {'RWD': "DriveWheel == 'rwd'",
                                   'FWD': "DriveWheel == 'fwd'",
                                   '4WD': "DriveWheel == '4wd'"},
                    'WheelBase': {'85-95': 'WheelBase < 95',
                                  '95-105': 'WheelBase > 95 & WheelBase < 105',
                                  '105-120': 'WheelBase > 105'},
                    'CurbWeight': {'below 2200': 'CurbWeight < 2200',
                                   'above 2200': 'CurbWeight >= 2200'},
           
                    'Horsepower': ['less than 200', '200 to 250', '250 and above'],
                    'PeakRPM': ['4000-4750(low)', '4751-5000(medium)', '5000-6000(high)'],
                    'CityMPL': ['12-16', '17-24', '25-35', '36 and above'],
                    'HighwayMPL': ['14-18', '19-26', '27-35', '36 and above']}


def filterdata(filterDict):
    data = pd.read_csv('Projects\carFinding\Cardata.csv')
    # for key in filterDict:
    #     currentIndex = key
    #     data.set_index(currentIndex, inplace=True)
    #     resultData = data.loc[filterConditions[key][filterDict[key]]]
    #     data = resultData
    filters = ""
    keys = list(filterDict.keys())
    print(keys)
    for key in keys:
        if key == keys[-1]:
            filters += filterConditions[key][filterDict[key]]
        else:
            filters += filterConditions[key][filterDict[key]]+" & "
    print(filters)
    res = data[data.eval(filters)]
    print(res)


filterdata(sampleDict)

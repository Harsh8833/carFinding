import pandas as pd

filterConditions = {'Symboling': {'Safe': 'Symboling < 0',
                                  'Medium': 'Symboling == 0 | Symboling == 1',
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
                    'CylinderNumber': {'two-three': "CylinderNumber == 'two' | CylinderNumber == 'three'",
                                       'four-six': "CylinderNumber == 'four' | CylinderNumber == 'five' | CylinderNumber == 'six'",
                                       'eight-twelve': "CylinderNumber == 'eight' | CylinderNumber == 'nine' | CylinderNumber == 'ten' | CylinderNumber == 'eleven' | CylinderNumber == 'twelve'"},
                    'Horsepower': {'less than 200': "Horsepower < 200",
                                   '200 to 250': "Horsepower > 200 & Horsepower < 250",
                                   '250 and above': "Horsepower > 250"},
                    'PeakRPM': {'4000-4750(low)': 'PeakRPM < 4750',
                                '4751-5000(medium)': 'PeakRPM > 4750 & PeakRPM < 5000',
                                '5000-6000(high)': 'PeakRPM > 5000'},
                    'CityMPL': {'12-16': 'CityMPL < 16',
                                '17-24': 'CityMPL < 24 & CityMPL > 16',
                                '25-35': 'CityMPL < 36 & CityMPL > 24',
                                '36 and above': 'CityMPL > 36'},
                    'HighwayMPL': {'14-18':'HighwayMPL < 18',
                                   '19-26':'HighwayMPL < 26 & HighwayMPL > 19',
                                   '27-35':'HighwayMPL < 35 & HighwayMPL > 26',
                                   '36 and above':'HighwayMPL > 36'}}


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
    outputData = data[data.eval(filters)]
    return outputData




# Import the required libraries
from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import car
import ctypes

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("800x600")

# ctypes.windll.shcore.SetProcessDpiAwareness(1)

####################################
#  Frames

headingFrame = Frame(win)
headingFrame.pack(fill=X)

selectionFrame = Frame(win)
selectionFrame.pack(fill=X)

buttonFrame = Frame(win)
buttonFrame.pack(fill=X)

####################################


# Define the style for combobox widget
style = ttk.Style()
style.theme_use('xpnative')
style.configure("TCombobox", fieldbackground="white", background="white")

# Add a label widget
label = ttk.Label(headingFrame,
                  text="Car Predictor",
                  font=('orbitron', 45, BOLD))
label.pack(pady=30)

selectionCB = list()
headerList = ['Symboling', 'FuelType', 'DoorNumber', 'CarBody', 'DriveWheel', 'WheelBase','CurbWeight', 'CylinderNumber', 'Horsepower', 'PeakRPM', 'CityMPL', 'HighwayMPL']


# Add a Combobox widget
currentSelected = list()
for i in range(5):
    currentSelectedEach = StringVar()
    cb = ttk.Combobox(selectionFrame,
                      width=25,
                      values=headerList,
                      textvariable=currentSelectedEach)
    cb.bind('<<ComboboxSelected>>', lambda event, x=i: selectionOnCB(event, x))
    cb.grid(row=i, column=0, padx=20, pady=10)
    selectionCB.append(cb)




def selectionOnCB(event, row):
    radioDict = {'Symboling': ['Safe', 'Medium', 'Risk'],
     'FuelType': ['Petrol', 'Diesel'],
     'DoorNumber':['Two', 'Four'],
     'CarBody':['Convertible', 'Sedan', 'Hatch Back', 'SUV'],
     'DriveWheel':['RWD', 'FWD', '4WD'],
     'WheelBase':['88-95', '95-105', '105-120'],
     'CurbWeight': ['below 2200', 'above 2200'],
     'CylinderNumber':['two-three', 'four-six', 'eight-twelve'],
     'Horsepower':['less than 200', '200 to 250', '250 and above'],
     'PeakRPM':['4000-4750(low)', '4751-5000(medium)', '5000-6000(high)'],
     'CityMPL':['12-16', '17-24', '25-35', '36 and above'],
     'HighwayMPL':['14-18', '19-26', '27-35', '36 and above']}

    selectedOption = radioDict[selectionCB[row].get()]

    def buildRadioButtons(selectedList):
        selected = StringVar()
        for each in range(len(selectedList)):
            r = ttk.Radiobutton(
                selectionFrame,
                text=selectedList[each],
                value=each,
                variable=selected)
            r.grid(row=row, column=each+1, padx=5, pady=5)

    buildRadioButtons(selectedOption)

findCars = ttk.Button(buttonFrame,
text="Find Cars")
findCars.pack()



win.mainloop()

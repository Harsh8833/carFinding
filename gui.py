# Import the required libraries
from cgitb import text
from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from pandastable import Table
import car


# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("900x600")

# ctypes.windll.shcore.SetProcessDpiAwareness(1)

####################################
#  Frames

headingFrame = Frame(win)
headingFrame.pack(fill=X)

selectionFrame = Frame(win)
selectionFrame.pack(fill=X)

buttonFrame = Frame(win)
buttonFrame.pack(fill=X)

resultFrame = Frame(win)
resultFrame.pack(fill=X)

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
headerList = ['Symboling', 'FuelType', 'DoorNumber', 'CarBody', 'DriveWheel', 'WheelBase',
              'CurbWeight', 'CylinderNumber', 'Horsepower', 'PeakRPM', 'CityMPL', 'HighwayMPL']


# Add a Combobox widget
currentSelected = list()
for i in range(5):
    ttk.Label(selectionFrame, text="Select your choice:",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=i, padx=20, pady=10)
    currentSelectedEach = StringVar()
    cb = ttk.Combobox(selectionFrame,
                      width=25,
                      values=headerList,
                      textvariable=currentSelectedEach)
    cb.bind('<<ComboboxSelected>>', lambda event, x=i: selectionOnCB(event, x))
    cb.grid(row=i, column=1, padx=20, pady=10)
    selectionCB.append(cb)


selButtons = {0: [],
              1: [],
              2: [],
              3: [],
              4: []}
radioValue = [None]*5





def selectionOnCB(event, row):
    radioDict = {'Symboling': ['Safe', 'Medium', 'Risk'],
                 'FuelType': ['Petrol', 'Diesel'],
                 'DoorNumber': ['Two', 'Four'],
                 'CarBody': ['Convertible', 'Sedan', 'Hatch Back', 'SUV'],
                 'DriveWheel': ['RWD', 'FWD', '4WD'],
                 'WheelBase': ['85-95', '95-105', '105-120'],
                 'CurbWeight': ['below 2200', 'above 2200'],
                 'CylinderNumber': ['two-three', 'four-six', 'eight-twelve'],
                 'Horsepower': ['less than 200', '200 to 250', '250 and above'],
                 'PeakRPM': ['4000-4750(low)', '4751-5000(medium)', '5000-6000(high)'],
                 'CityMPL': ['12-16', '17-24', '25-35', '36 and above'],
                 'HighwayMPL': ['14-18', '19-26', '27-35', '36 and above']}
    selectedOption = radioDict[selectionCB[row].get()]
    for i in selButtons[row]:
        i.destroy()

    def buildRadioButtons(selectedList):
        selected = StringVar()
        radioValue[row] = selected
        selButtons[row].clear()

        for each in range(len(selectedList)):
            r = ttk.Radiobutton(
                selectionFrame,
                text=selectedList[each],
                value=selectedList[each],
                variable=selected)
            r.grid(row=row, column=each+2, padx=5, pady=5, sticky=W)
            selButtons[row].append(r)
    buildRadioButtons(selectedOption)
    


def findCars():
    filters = dict()
    for i in range(5):
        key = selectionCB[i].get() 
        value = radioValue[i].get()
        filters[key] = value
    outputData = car.filterdata(filters)
    pt = Table(resultFrame, dataframe=outputData)
    pt.show()
        

findCarsButton = ttk.Button(buttonFrame,
                            text="Find Cars",
                            command=findCars)
findCarsButton.pack()




win.mainloop()

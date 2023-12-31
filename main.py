import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

Zone1700 = [36630.0,48390.0,76170.0,95270.0,94770.0,96990.0,100020.0,93700.0,83660.0,60750.0,40480.0,34850.0]
Zone1800 = [41870,55300,87050,108880,108310,110840,114310,107170,95610,69420,46260,39830]
Zone11000 = [52330,69120,108810,136110,135380,138550,142890,133960,119510,86780,57830,49790]
Zone11200 = [62800,82950,130580,163330,162460,166270,171470,160760,143420,104140,69390,59750]
Zone12400 = [62800*2,82950*2,130580*2,163330*2,162460*2,166270*2,171470*2,160760*2,143420*2,104140*2,69390*2,59750*2]

Zone2700 = [36470,47150,70410,83790,83560,80730,82490,77860,74200,56970,44530,35020]
Zone2800 = [41680,53890,80470,95760,95500,92260,94270,88980,84800,65110,50900,41170]
Zone21000 = [52100,67360,100590,119710,119370,115330,117840,111230,106000,81390,63620,51460]
Zone21200 = [62530,80830,120700,143650,143240,138400,141410,133470,127200,97670,76340,61750]
Zone22400 = [62530*2,80830*2,120700*2,143650*2,143240*2,138400*2,141410*2,133470*2,127200*2,97670*2,76340*2,61750*2]

Zone3700 = [30900,43850,66540,78460,82940,74590,79440,76440,67630,50800,38180,31540]
Zone3800 = [35310,50120,76040,89670,94790,85250,90790,87290,77290,58050,43630,36040]
Zone31000 = [44140,62640,95050,112090,118490,106560,113480,109110,96610,72570,54540,45050]
Zone31200 = [52970,75170,114060,134500,142190,127870,136180,130930,115930,87080,65450,54060]
Zone32400 = [52970*2,75170*2,114060*2,134500*2,142190*2,127870*2,136180*2,130930*2,115930*2,87080*2,65450*2,54060*2]

Zone4700 = [24200,40410,60230,77500,83530,74050,76620,69880,60610,45210,33000,22590]
Zone4800 = [27660,46180,68840,88570,95460,84630,87570,79870,69270,51670,37720,25820]
Zone41000 = [34570,57730,86050,110720,119330,105790,109460,99830,86590,64590,47150,32280]
Zone41200 = [41480,69270,103260,132860,143200,126950,131350,119800,103910,77510,56580,38730]
Zone42400 = [41480*2,69270*2,103260*2,132860*2,143200*2,126950*2,131350*2,119800*2,103910*2,77510*2,56580*2,38730*2]

camerasTypical = 0

camerasHigher = 0

camera1LastTypical = 0
camera1LastHigher = 0

camera2LastTypical = 0
camera2LastHigher = 0

camera3LastTypical = 0
camera3LastHigher = 0

camera4LastTypical = 0
camera4LastHigher = 0

camera5LastTypical = 0
camera5LastHigher = 0

camera6LastTypical = 0
camera6LastHigher = 0

unitZone = ""

ARCbaseline = 0

solarArray = ""

baselineLoadPerMonth = []

actualCameraLoadDayMonth = []

actualCameraLoadNightMonth = []

totalLoadMonth = []

surplusOrdeficit = []

cameras = [""]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

CameraPower = resource_path("CameraPower.txt")

ZonesImage = resource_path("Zones.png")

SunstoneLogo = resource_path("Sunstone_Logo.png")

with open(CameraPower, "r") as f:
    for line in f.readlines()[1:]:
        item = line.split()
        cameras.append(item[0])

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(SunstoneLogo))
        self.setWindowIconText("logo")

        self.setWindowTitle("Power Load Calculator")

        self.setGeometry(0, 0, 600, 700)

        layout = QGridLayout()

        # No Cameras and Models
        ###########################################################
        self.NoCamera = QLabel("No. Of Cameras:")
        layout.addWidget(self.NoCamera, 0, 0)

        self.NoCameraSelect = QComboBox()
        self.NoCameraSelect.addItems(["", "1", "2", "3", "4", "5", "6"])
        layout.addWidget(self.NoCameraSelect, 0, 1)

        self.NoCameraSelect.activated.connect(self.getNumCameras)

        self.camera1 = QLabel("Camera 1:")
        layout.addWidget(self.camera1, 1, 0)
        self.camera1.hide()

        self.camera1Select = QComboBox()
        layout.addWidget(self.camera1Select, 1, 1)
        self.camera1Select.addItems(cameras)
        self.camera1Select.hide()

        self.camera1Select.activated.connect(self.getCamera1)

        self.camera2 = QLabel("Camera 2:")
        layout.addWidget(self.camera2, 2, 0)
        self.camera2.hide()

        self.camera2Select = QComboBox()
        layout.addWidget(self.camera2Select, 2, 1)
        self.camera2Select.addItems(cameras)
        self.camera2Select.hide()

        self.camera2Select.activated.connect(self.getCamera2)

        self.camera3 = QLabel("Camera 3:")
        layout.addWidget(self.camera3, 3, 0)
        self.camera3.hide()

        self.camera3Select = QComboBox()
        layout.addWidget(self.camera3Select, 3, 1)
        self.camera3Select.addItems(cameras)
        self.camera3Select.hide()

        self.camera3Select.activated.connect(self.getCamera3)

        self.camera4 = QLabel("Camera 4:")
        layout.addWidget(self.camera4, 4, 0)
        self.camera4.hide()

        self.camera4Select = QComboBox()
        layout.addWidget(self.camera4Select, 4, 1)
        self.camera4Select.addItems(cameras)
        self.camera4Select.hide()

        self.camera4Select.activated.connect(self.getCamera4)

        self.camera5 = QLabel("Camera 5:")
        layout.addWidget(self.camera5, 5, 0)
        self.camera5.hide()

        self.camera5Select = QComboBox()
        layout.addWidget(self.camera5Select, 5, 1)
        self.camera5Select.addItems(cameras)
        self.camera5Select.hide()

        self.camera5Select.activated.connect(self.getCamera5)

        self.camera6 = QLabel("Camera 6:")
        layout.addWidget(self.camera6, 6, 0)
        self.camera6.hide()

        self.camera6Select = QComboBox()
        layout.addWidget(self.camera6Select, 6, 1)
        self.camera6Select.addItems(cameras)
        self.camera6Select.hide()

        self.camera6Select.activated.connect(self.getCamera6)

        ###########################################################

        # Image And Key
        ######################################################
        self.zoneImage = QLabel()
        pixmap = QPixmap(ZonesImage)
        self.zoneImage.setPixmap(pixmap)
        layout.addWidget(self.zoneImage, 0, 2, 4, 2)

        self.zone1 = QLabel("Zone 1")
        self.zone1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zone1.setStyleSheet("background-color:#627B95;"
                                 "color:white")
        layout.addWidget(self.zone1, 0, 3)

        self.zone2 = QLabel("Zone 2")
        self.zone2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zone2.setStyleSheet("background-color:#A8DD52;"
                                 "color:white")
        layout.addWidget(self.zone2, 1, 3)

        self.zone3 = QLabel("Zone 3")
        self.zone3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zone3.setStyleSheet("background-color:#24ACD1;"
                                 "color:white")
        layout.addWidget(self.zone3, 2, 3)

        self.zone4 = QLabel("Zone 4")
        self.zone4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zone4.setStyleSheet("background-color:#A25356;"
                                 "color:white")
        layout.addWidget(self.zone4, 3, 3)

        ######################################################

        self.zone = QLabel("Zone:")
        layout.addWidget(self.zone, 4, 2)

        self.zoneSelect = QComboBox()
        self.zoneSelect.addItems(["", "Zone1", "Zone2", "Zone3", "Zone4"])
        layout.addWidget(self.zoneSelect, 4, 3)

        self.zoneSelect.activated.connect(self.getZone)

        self.baseLine = QLabel("ARC Base Line (W)")
        layout.addWidget(self.baseLine, 5, 2)

        self.baseLineText = QLineEdit()
        self.baseLineText.textChanged.connect(self.getARCBaseline)
        layout.addWidget(self.baseLineText, 5, 3)

        self.solarArray = QLabel("Solar Array Size (W)")
        layout.addWidget(self.solarArray, 6, 2)

        self.solarArraySelect = QComboBox()
        self.solarArraySelect.addItems(["", "1", "700", "800", "1000", "1200", "2400"])
        layout.addWidget(self.solarArraySelect, 6, 3)

        self.solarArraySelect.activated.connect(self.getSolar)

        # Camera Power Values
        ####################################################
        self.typicalLabel = QLabel("Typical Camera Power:")
        layout.addWidget(self.typicalLabel, 8, 0)

        self.typicalValue = QLabel(f"{0}W")
        layout.addWidget(self.typicalValue, 8, 1)

        self.higherLabel = QLabel("Higher Camera Power:")
        layout.addWidget(self.higherLabel, 8, 2)

        self.higherValue = QLabel(f"{0}W")
        layout.addWidget(self.higherValue, 8, 3)
        ####################################################

        # Months Headings
        #######################################################
        self.heading1 = QLabel("Month - ")
        layout.addWidget(self.heading1, 10, 0)

        self.january = QLabel("January")
        layout.addWidget(self.january, 11, 0)

        self.february = QLabel("February")
        layout.addWidget(self.february, 12, 0)

        self.march = QLabel("March")
        layout.addWidget(self.march, 13, 0)

        self.april = QLabel("April")
        layout.addWidget(self.april, 14, 0)

        self.may = QLabel("May")
        layout.addWidget(self.may, 15, 0)

        self.june = QLabel("June")
        layout.addWidget(self.june, 16, 0)

        self.july = QLabel("July")
        layout.addWidget(self.july, 17, 0)

        self.august = QLabel("August")
        layout.addWidget(self.august, 18, 0)

        self.september = QLabel("September")
        layout.addWidget(self.september, 19, 0)

        self.october = QLabel("October")
        layout.addWidget(self.october, 20, 0)

        self.november = QLabel("November")
        layout.addWidget(self.november, 21, 0)

        self.december = QLabel("December")
        layout.addWidget(self.december, 22, 0)
        #######################################################

        self.heading1 = QLabel("System Surplus or Deficit - ")
        layout.addWidget(self.heading1, 10, 1)

        self.januarySystem = QLabel("")
        layout.addWidget(self.januarySystem, 11, 1)

        self.februarySystem = QLabel("")
        layout.addWidget(self.februarySystem, 12, 1)

        self.marchSystem = QLabel("")
        layout.addWidget(self.marchSystem, 13, 1)

        self.aprilSystem = QLabel("")
        layout.addWidget(self.aprilSystem, 14, 1)

        self.maySystem = QLabel("")
        layout.addWidget(self.maySystem, 15, 1)

        self.juneSystem = QLabel("")
        layout.addWidget(self.juneSystem, 16, 1)

        self.julySystem = QLabel("")
        layout.addWidget(self.julySystem, 17, 1)

        self.augustSystem = QLabel("")
        layout.addWidget(self.augustSystem, 18, 1)

        self.septemberSystem = QLabel("")
        layout.addWidget(self.septemberSystem, 19, 1)

        self.octoberSystem = QLabel("")
        layout.addWidget(self.octoberSystem, 20, 1)

        self.novemberSystem = QLabel("")
        layout.addWidget(self.novemberSystem, 21, 1)

        self.decemberSystem = QLabel("")
        layout.addWidget(self.decemberSystem, 22, 1)

        self.heading1 = QLabel("Methanol Requirements - ")
        layout.addWidget(self.heading1, 10, 2)

        self.januaryMethanol = QLabel("")
        layout.addWidget(self.januaryMethanol, 11, 2)

        self.februaryMethanol = QLabel("")
        layout.addWidget(self.februaryMethanol, 12, 2)

        self.marchMethanol = QLabel("")
        layout.addWidget(self.marchMethanol, 13, 2)

        self.aprilMethanol = QLabel("")
        layout.addWidget(self.aprilMethanol, 14, 2)

        self.mayMethanol = QLabel("")
        layout.addWidget(self.mayMethanol, 15, 2)

        self.juneMethanol = QLabel("")
        layout.addWidget(self.juneMethanol, 16, 2)

        self.julyMethanol = QLabel("")
        layout.addWidget(self.julyMethanol, 17, 2)

        self.augustMethanol = QLabel("")
        layout.addWidget(self.augustMethanol, 18, 2)

        self.septemberMethanol = QLabel("")
        layout.addWidget(self.septemberMethanol, 19, 2)

        self.octoberMethanol = QLabel("")
        layout.addWidget(self.octoberMethanol, 20, 2)

        self.novemberMethanol = QLabel("")
        layout.addWidget(self.novemberMethanol, 21, 2)

        self.decemberMethanol = QLabel("")
        layout.addWidget(self.decemberMethanol, 22, 2)

        self.heading1 = QLabel("Methanol Cost - ")
        layout.addWidget(self.heading1, 10, 3)

        self.januaryCost = QLabel("")
        layout.addWidget(self.januaryCost, 11, 3)

        self.februaryCost = QLabel("")
        layout.addWidget(self.februaryCost, 12, 3)

        self.marchCost = QLabel("")
        layout.addWidget(self.marchCost, 13, 3)

        self.aprilCost = QLabel("")
        layout.addWidget(self.aprilCost, 14, 3)

        self.mayCost = QLabel("")
        layout.addWidget(self.mayCost, 15, 3)

        self.juneCost = QLabel("")
        layout.addWidget(self.juneCost, 16, 3)

        self.julyCost = QLabel("")
        layout.addWidget(self.julyCost, 17, 3)

        self.augustCost = QLabel("")
        layout.addWidget(self.augustCost, 18, 3)

        self.septemberCost = QLabel("")
        layout.addWidget(self.septemberCost, 19, 3)

        self.octoberCost = QLabel("")
        layout.addWidget(self.octoberCost, 20, 3)

        self.novemberCost = QLabel("")
        layout.addWidget(self.novemberCost, 21, 3)

        self.decemberCost = QLabel("")
        layout.addWidget(self.decemberCost, 22, 3)

        # Calculate button
        ###############################################
        self.calulateButton = QPushButton("Calculate")
        self.calulateButton.clicked.connect(self.doCalculations)
        layout.addWidget(self.calulateButton, 23, 1)
        ###############################################

        self.methanolCost = QLabel("Total Methanol Cost: ")
        layout.addWidget(self.methanolCost, 23, 2)

        self.methanolTotal = QLabel("")
        layout.addWidget(self.methanolTotal, 23, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def getNumCameras(self):
        global camerasTypical
        global camerasHigher
        global camera1LastTypical
        global camera1LastHigher
        global camera2LastTypical
        global camera2LastHigher
        global camera3LastTypical
        global camera3LastHigher
        global camera4LastTypical
        global camera4LastHigher
        global camera5LastTypical
        global camera5LastHigher
        global camera6LastTypical
        global camera6LastHigher
        NumCameras = str(self.NoCameraSelect.currentText())
        if len(NumCameras) == 0:
            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.hide()
            self.camera1Select.hide()
            self.camera2.hide()
            self.camera2Select.hide()
            self.camera3.hide()
            self.camera3Select.hide()
            self.camera4.hide()
            self.camera4Select.hide()
            self.camera5.hide()
            self.camera5Select.hide()
            self.camera6.hide()
            self.camera6Select.hide()
        elif NumCameras == "1":

            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.show()
            self.camera1Select.show()
            self.camera2.hide()
            self.camera2Select.hide()
            self.camera3.hide()
            self.camera3Select.hide()
            self.camera4.hide()
            self.camera4Select.hide()
            self.camera5.hide()
            self.camera5Select.hide()
            self.camera6.hide()
            self.camera6Select.hide()
        elif NumCameras == "2":

            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.show()
            self.camera1Select.show()
            self.camera2.show()
            self.camera2Select.show()
            self.camera3.hide()
            self.camera3Select.hide()
            self.camera4.hide()
            self.camera4Select.hide()
            self.camera5.hide()
            self.camera5Select.hide()
            self.camera6.hide()
            self.camera6Select.hide()
        elif NumCameras == "3":

            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.show()
            self.camera1Select.show()
            self.camera2.show()
            self.camera2Select.show()
            self.camera3.show()
            self.camera3Select.show()
            self.camera4.hide()
            self.camera4Select.hide()
            self.camera5.hide()
            self.camera5Select.hide()
            self.camera6.hide()
            self.camera6Select.hide()
        elif NumCameras == "4":

            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.show()
            self.camera1Select.show()
            self.camera2.show()
            self.camera2Select.show()
            self.camera3.show()
            self.camera3Select.show()
            self.camera4.show()
            self.camera4Select.show()
            self.camera5.hide()
            self.camera5Select.hide()
            self.camera6.hide()
            self.camera6Select.hide()
        elif NumCameras == "5":

            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.show()
            self.camera1Select.show()
            self.camera2.show()
            self.camera2Select.show()
            self.camera3.show()
            self.camera3Select.show()
            self.camera4.show()
            self.camera4Select.show()
            self.camera5.show()
            self.camera5Select.show()
            self.camera6.hide()
            self.camera6Select.hide()
        elif NumCameras == "6":
            camera1LastTypical = 0
            camera1LastHigher = 0
            camera2LastTypical = 0
            camera2LastHigher = 0
            camera3LastTypical = 0
            camera3LastHigher = 0
            camera4LastTypical = 0
            camera4LastHigher = 0
            camera5LastTypical = 0
            camera5LastHigher = 0
            camera6LastTypical = 0
            camera6LastHigher = 0

            camerasTypical = 0
            camerasHigher = 0
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

            self.camera1Select.setCurrentText("")
            self.camera2Select.setCurrentText("")
            self.camera3Select.setCurrentText("")
            self.camera4Select.setCurrentText("")
            self.camera5Select.setCurrentText("")
            self.camera6Select.setCurrentText("")

            self.camera1.show()
            self.camera1Select.show()
            self.camera2.show()
            self.camera2Select.show()
            self.camera3.show()
            self.camera3Select.show()
            self.camera4.show()
            self.camera4Select.show()
            self.camera5.show()
            self.camera5Select.show()
            self.camera6.show()
            self.camera6Select.show()

    def getCamera1(self):
        global camerasTypical
        global camerasHigher
        global camera1LastTypical
        global camera1LastHigher
        camera1 = str(self.camera1Select.currentText())
        if len(camera1) == 0:
            camerasTypical -= camera1LastTypical
            camerasHigher -= camera1LastHigher
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
            camera1LastTypical = 0
            camera1LastHigher = 0
        if len(camera1) > 0:
            camerasTypical -= camera1LastTypical
            camerasHigher -= camera1LastHigher
            with open("CameraPower.txt") as f:
                datefile = f.readlines()
                for line in datefile:
                    if camera1 in line:
                        item = line.split()
                        typicalWatt = float(item[1])
                        higherWatt = float(item[2])
            camerasTypical += typicalWatt
            camerasHigher += higherWatt
            camera1LastTypical = typicalWatt
            camera1LastHigher = higherWatt
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

    def getCamera2(self):
        global camerasTypical
        global camerasHigher
        global camera2LastTypical
        global camera2LastHigher
        camera2 = str(self.camera2Select.currentText())
        if len(camera2) == 0:
            camerasTypical -= camera2LastTypical
            camerasHigher -= camera2LastHigher
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
            camera2LastTypical = 0
            camera2LastHigher = 0
        if len(camera2) > 0:
            camerasTypical -= camera2LastTypical
            camerasHigher -= camera2LastHigher
            with open("CameraPower.txt") as f:
                datefile = f.readlines()
                for line in datefile:
                    if camera2 in line:
                        item = line.split()
                        typicalWatt = float(item[1])
                        higherWatt = float(item[2])
            camera2LastTypical = typicalWatt
            camera2LastHigher = higherWatt
            camerasTypical += typicalWatt
            camerasHigher += higherWatt
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
    def getCamera3(self):
        global camerasTypical
        global camerasHigher
        global camera3LastTypical
        global camera3LastHigher
        camera3 = str(self.camera3Select.currentText())
        if len(camera3) == 0:
            camerasTypical -= camera3LastTypical
            camerasHigher -= camera3LastHigher
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
            camera3LastTypical = 0
            camera3LastHigher = 0
        if len(camera3) > 0:
            camerasTypical -= camera3LastTypical
            camerasHigher -= camera3LastHigher
            with open("CameraPower.txt") as f:
                datefile = f.readlines()
                for line in datefile:
                    if camera3 in line:
                        item = line.split()
                        typicalWatt = float(item[1])
                        higherWatt = float(item[2])
            camera3LastTypical = typicalWatt
            camera3LastHigher = higherWatt
            camerasTypical += typicalWatt
            camerasHigher += higherWatt
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

    def getCamera4(self):
        global camerasTypical
        global camerasHigher
        global camera4LastTypical
        global camera4LastHigher
        camera4 = str(self.camera4Select.currentText())
        if len(camera4) == 0:
            camerasTypical -= camera4LastTypical
            camerasHigher -= camera4LastHigher
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
            camera4LastTypical = 0
            camera4LastHigher = 0
        if len(camera4) > 0:
            camerasTypical -= camera4LastTypical
            camerasHigher -= camera4LastHigher
            with open("CameraPower.txt") as f:
                datefile = f.readlines()
                for line in datefile:
                    if camera4 in line:
                        item = line.split()
                        typicalWatt = float(item[1])
                        higherWatt = float(item[2])
            camera4LastTypical = typicalWatt
            camera4LastHigher = higherWatt
            camerasTypical += typicalWatt
            camerasHigher += higherWatt
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

    def getCamera5(self):
        global camerasTypical
        global camerasHigher
        global camera5LastTypical
        global camera5LastHigher
        camera5 = str(self.camera5Select.currentText())
        if len(camera5) == 0:
            camerasTypical -= camera5LastTypical
            camerasHigher -= camera5LastHigher
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
            camera5LastTypical = 0
            camera5LastHigher = 0
        if len(camera5) > 0:
            camerasTypical -= camera5LastTypical
            camerasHigher -= camera5LastHigher
            with open("CameraPower.txt") as f:
                datefile = f.readlines()
                for line in datefile:
                    if camera5 in line:
                        item = line.split()
                        typicalWatt = float(item[1])
                        higherWatt = float(item[2])
            camera5LastTypical = typicalWatt
            camera5LastHigher = higherWatt
            camerasTypical += typicalWatt
            camerasHigher += higherWatt
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
    def getCamera6(self):
        global camerasTypical
        global camerasHigher
        global camera6LastTypical
        global camera6LastHigher
        camera6 = str(self.camera6Select.currentText())
        if len(camera6) == 0:
            camerasTypical -= camera6LastTypical
            camerasHigher -= camera6LastHigher
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")
            camera6LastTypical = 0
            camera6LastHigher = 0
        if len(camera6) > 0:
            camerasTypical -= camera6LastTypical
            camerasHigher -= camera6LastHigher
            with open("CameraPower.txt") as f:
                datefile = f.readlines()
                for line in datefile:
                    if camera6 in line:
                        item = line.split()
                        typicalWatt = float(item[1])
                        higherWatt = float(item[2])
            camera6LastTypical = typicalWatt
            camera6LastHigher = higherWatt
            camerasTypical += typicalWatt
            camerasHigher += higherWatt
            self.typicalValue.setText(f"{str(camerasTypical)}W")
            self.higherValue.setText(f"{str(camerasHigher)}W")

    def getZone(self):
        global unitZone
        unitZone = str(self.zoneSelect.currentText())

    def getARCBaseLine(self, Baseline):
        global ARCbaseline
        ARCbaseline = Baseline

    def getSolar(self):
        global solarArray
        solarArray = str(self.solarArraySelect.currentText())

    def doCalculations(self):
        global camerasTypical
        global camerasHigher
        global solarArray
        global ARCbaseline
        global unitZone

        baselineLoadPerMonth.clear()
        actualCameraLoadDayMonth.clear()
        actualCameraLoadNightMonth.clear()
        totalLoadMonth.clear()
        surplusOrdeficit.clear()

        self.januarySystem.setText("")
        self.februarySystem.setText("")
        self.marchSystem.setText("")
        self.aprilSystem.setText("")
        self.maySystem.setText("")
        self.juneSystem.setText("")
        self.julySystem.setText("")
        self.augustSystem.setText("")
        self.septemberSystem.setText("")
        self.octoberSystem.setText("")
        self.novemberSystem.setText("")
        self.decemberSystem.setText("")

        months31 = int(ARCbaseline) * 24 * 31
        months30 = int(ARCbaseline) * 24 * 30
        febuary28 = int(ARCbaseline) * 24 * 28

        baselineLoadPerMonth.append(months31)
        baselineLoadPerMonth.append(febuary28)
        baselineLoadPerMonth.append(months31)
        baselineLoadPerMonth.append(months30)
        baselineLoadPerMonth.append(months31)
        baselineLoadPerMonth.append(months30)
        baselineLoadPerMonth.append(months31)
        baselineLoadPerMonth.append(months31)
        baselineLoadPerMonth.append(months30)
        baselineLoadPerMonth.append(months31)
        baselineLoadPerMonth.append(months30)
        baselineLoadPerMonth.append(months31)

        actualCameraLoadDayMonth.append(camerasTypical * 8.25 * 31)
        actualCameraLoadDayMonth.append(camerasTypical * 9.8 * 28)
        actualCameraLoadDayMonth.append(camerasTypical * 11.7 * 31)
        actualCameraLoadDayMonth.append(camerasTypical * 13.7 * 30)
        actualCameraLoadDayMonth.append(camerasTypical * 15.4 * 31)
        actualCameraLoadDayMonth.append(camerasTypical * 16.4 * 30)
        actualCameraLoadDayMonth.append(camerasTypical * 15.9 * 31)
        actualCameraLoadDayMonth.append(camerasTypical * 14.4 * 31)
        actualCameraLoadDayMonth.append(camerasTypical * 12.4 * 30)
        actualCameraLoadDayMonth.append(camerasTypical * 10.4 * 31)
        actualCameraLoadDayMonth.append(camerasTypical * 8.6 * 30)
        actualCameraLoadDayMonth.append(camerasTypical * 7.6 * 31)

        actualCameraLoadNightMonth.append(camerasHigher * 15.75 * 31)
        actualCameraLoadNightMonth.append(camerasHigher * 14.2 * 28)
        actualCameraLoadNightMonth.append(camerasHigher * 12.3 * 31)
        actualCameraLoadNightMonth.append(camerasHigher * 10.3 * 30)
        actualCameraLoadNightMonth.append(camerasHigher * 8.5 * 31)
        actualCameraLoadNightMonth.append(camerasHigher * 7.6 * 30)
        actualCameraLoadNightMonth.append(camerasHigher * 8.1 * 31)
        actualCameraLoadNightMonth.append(camerasHigher * 9.6 * 31)
        actualCameraLoadNightMonth.append(camerasHigher * 11.6 * 30)
        actualCameraLoadNightMonth.append(camerasHigher * 13.6 * 31)
        actualCameraLoadNightMonth.append(camerasHigher * 15.4 * 30)
        actualCameraLoadNightMonth.append(camerasHigher * 16.6 * 31)

        j = 0

        while j < 12:
            totalLoadMonth.append(baselineLoadPerMonth[j] + actualCameraLoadDayMonth[j] + actualCameraLoadNightMonth[j])
            j = j + 1

        w = 0

        while w < 12:
            surplusOrdeficit.append(globals()[f"{unitZone}{solarArray}"][w] - totalLoadMonth[w])
            w = w + 1

        self.januarySystem.setText(f"{'%.2f' % surplusOrdeficit[0]}W")
        self.februarySystem.setText(f"{'%.2f' % surplusOrdeficit[1]}W")
        self.marchSystem.setText(f"{'%.2f' % surplusOrdeficit[2]}W")
        self.aprilSystem.setText(f"{'%.2f' % surplusOrdeficit[3]}W")
        self.maySystem.setText(f"{'%.2f' % surplusOrdeficit[4]}W")
        self.juneSystem.setText(f"{'%.2f' % surplusOrdeficit[5]}W")
        self.julySystem.setText(f"{'%.2f' % surplusOrdeficit[6]}W")
        self.augustSystem.setText(f"{'%.2f' % surplusOrdeficit[7]}W")
        self.septemberSystem.setText(f"{'%.2f' % surplusOrdeficit[8]}W")
        self.octoberSystem.setText(f"{'%.2f' % surplusOrdeficit[9]}W")
        self.novemberSystem.setText(f"{'%.2f' % surplusOrdeficit[10]}W")
        self.decemberSystem.setText(f"{'%.2f' % surplusOrdeficit[11]}W")

        if surplusOrdeficit[0] < 0:
            januaryMethanol = '%.2f' % ((surplusOrdeficit[0] / 1000) * -1)
            januaryCost = '%.2f' % (float(januaryMethanol) * 10.68)
            self.januaryMethanol.setText(f"{januaryMethanol}L")
            self.januaryCost.setText(f"£{januaryCost}")
        else:
            januaryCost = 0
            self.januaryMethanol.setText("0L")
            self.januaryCost.setText("£0")

        if surplusOrdeficit[1] < 0:
            februaryMethanol = '%.2f' % ((surplusOrdeficit[1] / 1000) * -1)
            februaryCost = '%.2f' % (float(februaryMethanol) * 10.68)
            self.februaryMethanol.setText(f"{februaryMethanol}L")
            self.februaryCost.setText(f"£{februaryCost}")
        else:
            februaryCost = 0
            self.februaryMethanol.setText("0L")
            self.februaryCost.setText("£0")

        if surplusOrdeficit[2] < 0:
            marchMethanol = '%.2f' % ((surplusOrdeficit[2] / 1000) * -1)
            marchCost = '%.2f' % (float(marchMethanol) * 10.68)
            self.marchMethanol.setText(f"{marchMethanol}L")
        else:
            marchCost = 0
            self.marchMethanol.setText("0L")
            self.marchCost.setText("£0")

        if surplusOrdeficit[3] < 0:
            aprilMethanol = '%.2f' % ((surplusOrdeficit[3] / 1000) * -1)
            aprilCost = '%.2f' % (float(aprilMethanol)*10.68)
            self.aprilMethanol.setText(f"{aprilMethanol}L")
            self.aprilCost.setText(f"£{aprilCost}")
        else:
            aprilCost = 0
            self.aprilMethanol.setText("0L")
            self.aprilCost.setText("£0")

        if surplusOrdeficit[4] < 0:
            mayMethanol = '%.2f' % ((surplusOrdeficit[4] / 1000) * -1)
            mayCost = '%.2f' % (float(mayMethanol)*10.68)
            self.mayMethanol.setText(f"{mayMethanol}L")
            self.mayCost.setText(f"£{mayCost}")
        else:
            mayCost = 0
            self.mayMethanol.setText("0L")
            self.mayCost.setText("£0")

        if surplusOrdeficit[5] < 0:
            juneMethanol = '%.2f' % ((surplusOrdeficit[5] / 1000) * -1)
            juneCost = '%.2f' % (float(juneMethanol)*10.68)
            self.juneMethanol.setText(f"{juneMethanol}L")
            self.juneCost.setText(f"£{juneCost}")
        else:
            juneCost = 0
            self.juneMethanol.setText("0L")
            self.juneCost.setText("£0")

        if surplusOrdeficit[6] < 0:
            julyMethanol = '%.2f' % ((surplusOrdeficit[6] / 1000) * -1)
            julyCost = '%.2f' % (float(julyMethanol) * 10.68)
            self.julyMethanol.setText(f"{julyMethanol}L")
            self.julyCost.setText(f"£{julyCost}")
        else:
            julyCost = 0
            self.julyMethanol.setText("0L")
            self.julyCost.setText("£0")

        if surplusOrdeficit[7] < 0:
            augustMethanol = '%.2f' % ((surplusOrdeficit[7] / 1000) * -1)
            augustCost = '%.2f' % (float(augustMethanol)*10.68)
            self.augustMethanol.setText(f"{augustMethanol}L")
            self.augustCost.setText(f"£{augustCost}")
        else:
            augustCost = 0
            self.augustMethanol.setText("0L")
            self.augustCost.setText("£0")

        if surplusOrdeficit[8] < 0:
            septemberMethanol = '%.2f' % ((surplusOrdeficit[8] / 1000) * -1)
            septemberCost = '%.2f' % (float(septemberMethanol)*10.68)
            self.septemberMethanol.setText(f"{septemberMethanol}L")
            self.septemberCost.setText(f"£{septemberCost}")
        else:
            septemberCost = 0
            self.septemberMethanol.setText("0L")
            self.septemberCost.setText("£0")

        if surplusOrdeficit[9] < 0:
            octoberMethanol = '%.2f' % ((surplusOrdeficit[9] / 1000) * -1)
            octoberCost = '%.2f' % (float(octoberMethanol)*10.68)
            self.octoberMethanol.setText(f"{octoberMethanol}L")
            self.octoberCost.setText(f"£{octoberCost}")
        else:
            octoberCost = 0
            self.octoberMethanol.setText("0L")
            self.octoberCost.setText("£0")

        if surplusOrdeficit[10] < 0:
            novemberMethanol = '%.2f' % ((surplusOrdeficit[10] / 1000) * -1)
            novemberCost = '%.2f' % (float(novemberMethanol) * 10.68)
            self.novemberMethanol.setText(f"{novemberMethanol}L")
            self.novemberCost.setText(f"£{novemberCost}")
        else:
            novemberCost = 0
            self.novemberMethanol.setText("0L")
            self.novemberCost.setText("£0")

        if surplusOrdeficit[11] < 0:
            decemberMethanol = '%.2f' % ((surplusOrdeficit[11]/1000) * -1)
            decemberCost = '%.2f' % (float(decemberMethanol)*10.68)
            self.decemberMethanol.setText(f"{decemberMethanol}L")
            self.decemberCost.setText(f"£{decemberCost}")
        else:
            decemberCost = 0
            self.decemberMethanol.setText("0L")
            self.decemberCost.setText("£0")

        methanolTotal = '%.2f' % (float(januaryCost) + float(februaryCost) + float(marchCost) + float(aprilCost) + float(mayCost) + float(juneCost) + float(julyCost) + float(augustCost) + float(septemberCost) + float(octoberCost) + float(novemberCost) + float(decemberCost))

        self.methanolTotal.setText(f"£{methanolTotal}")
app = QApplication([])
app.setStyle('Fusion')
window = MainWindow()
window.show()
sys.exit(app.exec())
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

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

CameraPower = resource_path("CameraPower.txt")

ZonesImage = resource_path("Zones.png")

SunstoneLogo = resource_path("Sunstone_Logo.png")


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

        self.camera1 = QLabel("Camera 1:")
        layout.addWidget(self.camera1, 1, 0)

        self.camera1Select = QComboBox()
        layout.addWidget(self.camera1Select, 1, 1)

        self.camera2 = QLabel("Camera 2:")
        layout.addWidget(self.camera2, 2, 0)

        self.camera2Select = QComboBox()
        layout.addWidget(self.camera2Select, 2, 1)

        self.camera3 = QLabel("Camera 3:")
        layout.addWidget(self.camera3, 3, 0)

        self.camera3Select = QComboBox()
        layout.addWidget(self.camera3Select, 3, 1)

        self.camera4 = QLabel("Camera 4:")
        layout.addWidget(self.camera4, 4, 0)

        self.camera4Select = QComboBox()
        layout.addWidget(self.camera4Select, 4, 1)

        self.camera5 = QLabel("Camera 5:")
        layout.addWidget(self.camera5, 5, 0)

        self.camera5Select = QComboBox()
        layout.addWidget(self.camera5Select, 5, 1)

        self.camera6 = QLabel("Camera 6:")
        layout.addWidget(self.camera6, 6, 0)

        self.camera6Select = QComboBox()
        layout.addWidget(self.camera6Select, 6, 1)

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

        self.baseLine = QLabel("ARC Base Line (W)")
        layout.addWidget(self.baseLine, 5, 2)

        self.baseLineText = QLineEdit()
        layout.addWidget(self.baseLineText, 5, 3)

        self.solarArray = QLabel("Solar Array Size (W)")
        layout.addWidget(self.solarArray, 6, 2)

        self.solarArraySelect = QComboBox()
        self.solarArraySelect.addItems(["", "1", "700", "800", "1000", "1200", "2400"])
        layout.addWidget(self.solarArraySelect, 6, 3)

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

        #Calculate button
        ###############################################
        self.calulateButton = QPushButton("Calculate")

        layout.addWidget(self.calulateButton, 23,1)
        ###############################################

        self.methanolCost = QLabel("Total Methanol Cost: ")
        layout.addWidget(self.methanolCost, 23, 2)

        self.methanolTotal = QLabel("")
        layout.addWidget(self.methanolTotal, 23, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
app.setStyle('Fusion')
window = MainWindow()
window.show()
sys.exit(app.exec())
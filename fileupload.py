from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QMainWindow, QFileDialog, QListWidgetItem
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QPixmap
import sys, os
from PIL import Image
import boto3
import uuid
from mainGui import Ui_MainWindow

s3 = boto3.resource("s3")
s3Bucket = "newtestbucket25324dhfghgfhd8gds0"


# Main Window 
class Ui(QMainWindow):
    files = []
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("interface.ui", self) # Load the .ui file
        self.show() # Show the GUI
        self.pushButton_2.clicked.connect(self.openFiles)
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_3.clicked.connect(app.exit)
        self.Clear_All.clicked.connect(self.clearFiles)
        self.Delete_Selected.clicked.connect(self.clearSelectedFiles)
        
    def openFiles(self):
      
        file , check = QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileName()",
                                            "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if check:
            print("Selected Files: " + str(file))
            print(type(file))
            print(type(self.files))
            
            for i in file:
                self.files.append(i)

        self.showFiles(self.files)

    def showFiles(self, files):
            for i in files:
                listWidgetItem = QListWidgetItem(i)
                self.listWidget.addItem(listWidgetItem)
           
            print("Displaying Files")

    def upload(self):
        upload_files = self.files
        for i in upload_files:
            response = s3.meta.client.put_object(
                Bucket="newtestbucket25324dhfghgfhd8gds0", 
                Body= i, 
                Key= i
                )
            print(response)
    
    def clearFiles(self):
       self.listWidget.clear()
       
    def clearSelectedFiles(self):
        listItems = self.listWidget.selectedItems()
        print(listItems)
        print(type(listItems))
               
        for i in listItems:
            self.listWidget.takeItem(self.listWidget.row(i))

app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application

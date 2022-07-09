from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QMainWindow, QFileDialog
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QPixmap
import sys, os
from PIL import Image
import boto3
import uuid


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
        

    def openFiles(self):
        file , check = QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileName()",
                                               "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if check:
            print("Selected Files: " + str(file))
            
            #files = []
            print(type(file))
            print(type(self.files))
            
            for i in file:
                self.files.append(i)
            

            print("The selected files are ", self.files)

    def upload(self):
        upload_files = self.files
        for i in upload_files:
            response = s3.meta.client.put_object(
                Bucket="newtestbucket25324dhfghgfhd8gds0", 
                Body= i, 
                Key= i
                )
            print(response)

app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application

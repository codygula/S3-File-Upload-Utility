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
                self.StatusLabel.setText("Ready for upload")

        self.showFiles(self.files)
        self.files = []

    def showFiles(self, files):
            for i in files:
                listWidgetItem = QListWidgetItem(i)
                self.listWidget.addItem(listWidgetItem)
           
            print("Displaying Files")

    def upload(self):
        upload_files = self.files
        for i in upload_files:
            self.StatusLabel.setText(f"Uploading {i}")
            response = s3.meta.client.put_object(
                Bucket="newtestbucket25324dhfghgfhd8gds0", 
                Body= i, 
                Key= i
                )
            
            print(response)
        self.StatusLabel.setText(f"Done")
        self.listWidget.clear()
        self.files = []
    
    def clearFiles(self):
       self.listWidget.clear()
       self.files = []
       self.StatusLabel.setText("Files Cleared")
       
    def clearSelectedFiles(self):
        listItems = self.listWidget.selectedItems()
        print(listItems)
        print("type listItems = " + str(type(listItems)))


        #This still does not work       
        for i in listItems:
            if listItems[i] in self.files:
                self.files.pop(i)

            # self.listWidget.takeItem(self.listWidget.row(listItems[i + 1]))
            print("Type i = ", type(i))
            print("type listItems = ", type(listItems[i]))
            print(listItems[i])
           





# TODO Add options section to select S3 bucket, choose destination file names/paths, etc.

# TODO Add status indicators to StatusLabel 


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
# data
from code import proccess_image

widgets = {
    "gambar" : [],
    "start_button" : [],
    "select_button": [],
    "result_button": [],
    "before" : [],
    "after": [],
    "finish_text" : [],
    "before_text" : [],
    "after_text" : [],
    "select_text": []
}

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def start_app():
    clear_widgets()
    file_name = QFileDialog.getOpenFileName(
        window, 'Open File')
    frame2(file_name[0])

def start_procces(filename):
    clear_widgets()
    new_file = proccess_image(filename)
    frame3(filename, new_file)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Image Enhancement Application")
window.setFixedWidth(1000)
window.setFixedHeight(500)
window.setStyleSheet("background : #182732")

grid = QGridLayout()

def frame1():
    # Select Test
    text = QLabel()
    text.setText("Select an image !")
    text.setAlignment(QtCore.Qt.AlignCenter)
    text.setStyleSheet(
        "margin-top: 20px;" +
        "font-size: 40px;" +
        "color: white;")
    widgets["select_text"].append(text)

    # Button Widget 
    button = QPushButton("Select File")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid #1FBC2f;" +
        "border-radius: 10px;" +
        "font-size: 20px;" +
        "color: white;" +
        "padding: 10px 0;" +
        "margin: 50px 300px;}" +
        "*:hover {background: #1FBC2F;}"
    )
    button.clicked.connect(start_app)
    widgets["select_button"].append(button)

    grid.addWidget(widgets["select_text"][-1], 0, 0)
    grid.addWidget(widgets["select_button"][-1], 1, 0)

def frame2(filename):
    # Display 
    image = QPixmap(filename)
    image = image.scaled(500, 400, QtCore.Qt.KeepAspectRatio)
    gambar = QLabel()
    gambar.setPixmap(image)
    gambar.setAlignment(QtCore.Qt.AlignCenter)
    gambar.setStyleSheet("margin-top: 10px;")
    widgets["gambar"].append(gambar)

    # Button Widget 
    button = QPushButton("Start Processing")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid #1FBC2f;" +
        "border-radius: 10px;" +
        "font-size: 20px;" +
        "color: white;" +
        "padding: 10px 0;" +
        "margin: 50px 300px;}" +
        "*:hover {background: #1FBC2F;}"
    )
    button.clicked.connect(lambda x: start_procces(filename))
    widgets["start_button"].append(button)

    grid.addWidget(widgets["gambar"][-1], 0, 0)
    grid.addWidget(widgets["start_button"][-1], 1, 0)

def frame3(before, after):

    before_text = QLabel()
    before_text.setText("BEFORE")
    before_text.setAlignment(QtCore.Qt.AlignCenter)
    before_text.setStyleSheet(
        "margin-top: 5px;" +
        "font-size: 25px;" +
        "color: white;")
    widgets["before_text"].append(before_text)

    after_text = QLabel()
    after_text.setText("AFTER")
    after_text.setAlignment(QtCore.Qt.AlignCenter)
    after_text.setStyleSheet(
        "margin-top: 5px;" +
        "font-size: 25px;" +
        "color: white;")
    widgets["after_text"].append(after_text)

    # Display 
    beforeImage = QPixmap(before)
    beforeImage = beforeImage.scaled(500, 400, QtCore.Qt.KeepAspectRatio)
    before = QLabel()
    before.setPixmap(beforeImage)
    before.setAlignment(QtCore.Qt.AlignCenter)
    before.setStyleSheet("margin-top: 5px;")
    widgets["before"].append(before)

    # Display 
    afterImage = QPixmap(after)
    afterImage = afterImage.scaled(500, 400, QtCore.Qt.KeepAspectRatio)
    after = QLabel()
    after.setPixmap(afterImage)
    after.setAlignment(QtCore.Qt.AlignCenter)
    after.setStyleSheet("margin-top: 5px;")
    widgets["after"].append(after)

    grid.addWidget(widgets["before_text"][-1], 0, 0)
    grid.addWidget(widgets["after_text"][-1], 0, 1)
    grid.addWidget(widgets["before"][-1], 1, 0)
    grid.addWidget(widgets["after"][-1], 1, 1)

frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
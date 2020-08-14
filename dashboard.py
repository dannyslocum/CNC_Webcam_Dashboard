from PyQt5.QtWidgets import QApplication, QLabel, QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()

# Label + LineEdit for project name
# Slider (circular) for adjusting time lapse delay
# PushButton to save time lapse
# PushButton to reset time-lapse capture
# PushButton to shutdown the raspberry pi completely
# ???? to show temperature graph
from PyQt6.QtWidgets import*
app = QApplication([])
window = QWidget()
window.resize(700,500)
main_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
plus_btn = QPushButton("Плюс")
v1.addWidget(plus_btn)
minys_btn = QPushButton("Мінус")

mnogennya_btn = QPushButton("множення")
v1.addWidget(mnogennya_btn)
v1.addWidget(minys_btn)
main_line.addLayout(v1)
main_line.addLayout(v2)





window.setLayout(main_line)
window.show()
app.exec()
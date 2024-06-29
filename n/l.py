from PyQt6.QtWidgets import*

from res import app
from themes import theme1, theme2


def settings():
    window = QDialog()
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    br_btn = QPushButton("синьо-червона")
    pw_btn = QPushButton("рожево_біла")
    gp_btn = QPushButton("сіро-фіолетова")
    h1.addWidget(br_btn)
    h1.addWidget(pw_btn)
    h1.addWidget(gp_btn)
    main_line.addLayout(h1)

    def change():
        app.setStyleSheet(theme1)

    br_btn.clicked.connect(change)

    def change():
        app.setStyleSheet(theme2)

    pw_btn.clicked.connect(change)
    window.setLayout(main_line)
    window.show()
    window.exec()
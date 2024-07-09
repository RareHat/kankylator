from PyQt6.QtWidgets import*

from res import app
from themes import theme1, theme2, theme3, theme4


def settings():
    window = QDialog()
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h2 = QHBoxLayout()
    br_btn = QPushButton("синьо-червона")
    pw_btn = QPushButton("рожево_біла")
    gp_btn = QPushButton("сіро-фіолетова")
    st_btn = QPushButton("початкова тема")
    h1.addWidget(br_btn)
    h1.addWidget(pw_btn)
    h1.addWidget(gp_btn)
    h2.addWidget(st_btn)
    main_line.addLayout(h1)
    main_line.addLayout(h2)

    def change():
        app.setStyleSheet(theme1)

    br_btn.clicked.connect(change)

    def change():
        app.setStyleSheet(theme2)

    pw_btn.clicked.connect(change)

    def change():
        app.setStyleSheet(theme3)

    gp_btn.clicked.connect(change)
    def change():
        app.setStyleSheet(theme4)

    st_btn.clicked.connect(change)
    window.setLayout(main_line)
    window.show()
    window.exec()
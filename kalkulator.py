import sys
from PyQt5.QtWidgets import *


class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")

        vertikal_joylashuv = QVBoxLayout()

        self.ekran = QLineEdit()
        self.ekran.setReadOnly(True)
        vertikal_joylashuv.addWidget(self.ekran)

        kataklar = QGridLayout()

        tugmalar = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        for i, t in enumerate(tugmalar):
            btn = QPushButton(t)
            btn.clicked.connect(lambda _, x=t: self.bosish(x))
            kataklar.addWidget(btn, i // 4, i % 4)

        vertikal_joylashuv.addLayout(kataklar)

        tozalash = QPushButton("C")
        tozalash.clicked.connect(lambda: self.ekran.clear())
        vertikal_joylashuv.addWidget(tozalash)

        self.setLayout(vertikal_joylashuv)

    def bosish(self, belgi):
        if belgi == "=":
            try:
                self.ekran.setText(str(eval(self.ekran.text())))
            except Exception:
                self.ekran.setText("Xato")
        else:
            self.ekran.setText(self.ekran.text() + belgi)


app = QApplication(sys.argv)

oyna = Kalkulator()
oyna.show()

sys.exit(app.exec_())
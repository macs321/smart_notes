from PyQt6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow


app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)
# ------------------------------
NOTES{
    "нотатка №1 ": {
        "текст" "не забуть піти на треню Діма",
        "теги": ["в клуб", "на треню",],
    },
    "погудуй діму" :{
        "текст": "не забудь погудувати діму",
        "теги" : ["діма", "не піти",],
        }    
    }





# --------------------------------
win.show()
app.exec()
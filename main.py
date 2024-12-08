from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog

from ui import Ui_MainWindow
import json

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)
# ------------------------------
NOTES={
    "нотатка №1 ": {
        "текст": "не забуть піти на треню Діма",
        "теги": ["в клуб", "на треню",],
    },
    "погудуй діму" :{
        "текст": "не забудь погудувати діму",
        "теги" : ["діма", "не піти",],
        }    
    }




with open("notes_data.json", "r", encoding='UTF-8') as file:
    NOTES= json.load(file)


ui.Notes_list.addItems(NOTES)

def show_note():
    note_name = ui.Notes_list.selectedItems()[0].text()
    note = NOTES[note_name]
    ui.textEdit.setText(note["текст"])
    ui.Tags_list.clear()
    ui.Tags_list.addItems(note["теги"])

ui.Notes_list.itemClicked.connect(show_note)



def add_note():
    note_name, ok = QInputDialog.getText(
        win, "Введіть назву нотатки", "Назва нотатки:"
    )
    if ok:
        NOTES[note_name] = {

            "текст": "",
            "теги": [],

        }
        ui.Notes_list.addItem(note_name)

ui.btn_create_note.clicked.connect(add_note)

def save_note():
    if ui.Notes_list.selectedItems():
        note_name = ui.Notes_list.currentItem().text()
        note_text = ui.textEdit.toPlainText()


        # NOTES[note_name] = {
        #     "текст": note_text,
        #     "теги": []
#                                    нище краще
        # }
        NOTES[note_name]["текст"] = note_text



        with open("notes_data.json", "w", encoding = "UTF-8") as file:
            json.dump(NOTES, file)

ui.btn_safe_note.clicked.connect(save_note)


def del_note():
    if ui.Notes_list.selectedItems():
        note_name = ui.Notes_list.currentItem().text()

        del NOTES [note_name]
        ui.textEdit.clear()

        ui.Notes_list.clear()
        ui.Notes_list.addItems(NOTES)
        with open("notes_data.json","w", encoding = "UTF-8") as file:
            json.dump(NOTES, file)



ui.btn_delete_not.clicked.connect(del_note)


def add_tag():
     if ui.Notes_list.selectedItems():
         if ui.tag_search.text():
            note_name = ui.Notes_list.currentItem().text()
            new_tag = ui.tag_search.text()
            if not new_tag in NOTES[note_name]["теги"]:
                NOTES[note_name]["теги"].append(new_tag)

                ui.Tags_list.addItem(new_tag)
                ui.tag_search.clear()

                with open("notes_data.json", "w", encoding = "UTF-8") as file:
                    json.dump(NOTES, file)


ui.btn_add_tag.clicked.connect(add_tag)


def del_tag():
    if ui.Notes_list.selectedItems():
        note_name = ui.Notes_list.currentItem().Text()
        if ui.Tags_list.selectedItems():
            tag = ui.tags_list.curentItem().Text()
            NOTES[note_name]["теги"].remove(tag)

            ui.tags_list.clear()
            ui.tags_list.addItems(NOTES[note_name]["теги"])

            with open("notes_data.json", "w", encoding = "UTF-8") as file:
                    json.dump(NOTES, file)

def search_tag():
    if ui.btn_search.text() == "Шукати по Тегу":
        tag = ui.tag_search.text()
        filtered_notes = {}
        for note_name, note in NOTES.items():
            if tag in note["теги"]:
                filtered_notes[note_name] = note

        ui.Notes_list.clear()
        ui.Notes_list.addItems(filtered_notes)

        ui.btn_search.setText("Скинути пошук")

    elif ui.btn_search.text() == "Скинути пошук":
        ui.Notes_list.clear()
        ui.Notes_list.addItems(NOTES)
        ui.btn_search.setText("Шукати по Тегу")
        ui.tag_search.clear()




ui.btn_search.clicked.connect(search_tag)






































































































































































# --------------------------------
win.show()
app.exec()
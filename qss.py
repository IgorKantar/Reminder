def buttonHoverColor(color: str) -> str:
    style = """QPushButton{
        background: #16161E;
        color: #7aa2f7;
        font-size: 30px;
        min-width: 10px;
        max-width: 60px;
    }
    QPushButton:hover{
        color: """ + f"{color}" + """;
    }QPushButton:pressed{
        background: #16161E;
        border: none;
        color: #2ac3de;
    }"""
    return style

def textEditFontSize(size: int) -> str:
    style = """QTextEdit{
    background-color: #1A1B26;
    color: #9ECE6A;
    selection-background-color: #16161E;
    selection-color: red;
    font-size:""" + f"{size}" + """px;
    padding: 10px;
    margin-left: 10px;
    margin-right: 10px;
    border-radius: 5px;
    border: 1px solid;
    }"""
    return style

BUTTON_CONVERT = """
QPushButton{
    background:#1A1B26;
    color: #2ac3de;
    font-size: 24px;
    border: 1px solid;
    border-radius: 5px;
    padding-left: 20px;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-right: 20px;

}
QPushButton:hover{
    color: #16161E;
    background:#2ac3de;
}
QPushButton:pressed{
    background: #16161E;
    border: none;
    color: #2ac3de;
}
"""

DAY_QSS = """
QPushButton{
    font-size:15px;
}
QPushButton:hover{
    color: #2ac3de;
    background:#16161E;
}
QPushButton:pressed{
    background: #16161E;
    border: none;
    color: #2ac3de;
}
QFrame{
    border-radius: 5px;
    border: none;
}
QFrame:hover{
    border: 1px solid;
    border-color: #2ac3de;
}
QLabel{
    border:none;
    font-size: 15px;
}
QListView{
    padding:3px;
    background: #1A1B26;
    color:white;
    border:none;
}
"""
TRASH_BUTTON="""
QPushButton{
    background: #1A1B26;
    color: #7aa2f7;
    font-size: 24px;
    border: none;
}
QPushButton:hover{
    background: #1E202E;
}
QPushButton#listButton{
    background: #16161E;
    color: #7aa2f7;
    font-size: 24px;
    border-radius: 5px;
    border: 1px solid;
}
QPushButton#listButton:hover{
    color: #1A1B26;
}
QPushButton#listButton:pressed{
    background: #16161E;
    border: none;
    color: #2ac3de;
}
"""
LIST_BUTTON="""
QPushButton#listButton{
    background: #16161E;
    color: #7aa2f7;
    font-size: 24px;
    border-radius: 5px;
    border: 1px solid;
}
QPushButton#listButton:hover{
    color: #1A1B26;
}
QPushButton#listButton:pressed{
    background: #16161E;
    border: none;
    color: #2ac3de;
}
"""
DETAILS = """
QFrame{
    background: #1A1B26;
    border-radius: 5px;
    border: 2px solid;
    padding: 10px;
}
QFrame:hover{
    background: #1E202E;
}
QLabel{
    font-size:25px;
}
"""
QSS_STRING = """
QMainWindow{
    background-color: #16161E;
}
QMenuBar{
    background-color: #11111B;
    color: #A0A5CB;
}
QLineEdit{
    background: #1A1B26;
    color: #9ECE6A;
    selection-background-color: #16161E;
    selection-color: red;
    font-size: 24px;
    padding: 10px;
    border-radius: 5px;
    border: 2px solid;
}
QLineEdit:hover, QTextEdit:hover{
    background: #1E202E;
}
QTabWidget{
    background: #16161E;
}
QPushButton{
    background: #16161E;
    color: #7aa2f7;
    font-size: 24px;
    border-radius: 5px;
    border: 1px solid;
}
QPushButton:hover{
    color: #bb9af7;
}
QPushButton:pressed{
    background: #16161E;
    border: none;
    color: #2ac3de;
}

QLabel{
    background-color: #16161E;
    color: #a9b1d6;
    font-size: 25px;
}
QSlider{
    background-color: #1A1B26;
}
QListView{
    background: #1A1B26;
    border-radius: 5px;
    border: 2px solid;
    padding: 10px;
}
QListView:hover{
    background: #1E202E;
}
QListView:item:selected{
    background:#1A1B26;
}
QTableView{
    background: #1A1B26;
    border-radius: 5px;
    border: 2px solid;
    padding: 10px;
    color: #a9b1d6;
    font-size: 20px;
}
QTableView:hover{
    background: #1E202E;
}
QHeaderView::section{
    background-color:#16161E;
    color: #2ac3de;
    font-size: 18px;
}
"""

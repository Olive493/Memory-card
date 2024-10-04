QSS = '''
QWidget{
background-color: rgb(180, 134, 159); 
    border-width: 10px;
    border-radius: 10px;
    border-color: purple;

}
QPushButton { 
    background-color: rgb(190, 90, 100); 
    border-width: 10px;
    border-radius: 10px;
    border-color: purple;
    font: 18px "Montserrat";
    min-width: 5em;
    padding: 10px;
}
QPushButton:pressed {
    background-color: pink;
    border-style: dotted;
}
QGroupBox {
    color: orange;
    font: 20px;
    border-radius: 10px;
    border: 5px purple;
    margin-top: 5ex;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}
QRadioButton {
    font: bold 20px;
}
QRadioButton::indicator {
    width: 20px;
    height: 20px;
    border-radius: 10px;
}
QRadioButton::indicator::unchecked {
    border: 4px solid; 
    border-color: blue;
    background-color: yellow;
    border-radius: 7px;
}
QRadioButton::indicator:unchecked:hover {
    border-color: yellow;
    background-color: pink;
    border-radius: 7px;
}
QRadioButton::indicator::checked {
    border: 7px; 
    border-color: green;
    background-color: green;
    border-radius: 7px;
}
QLabel { 
    font: 20px "Montserrat";
}
'''

QSS_OK = '''
QPushButton { background-color: rgb(38, 30, 170); 
    border-width: 5px;
    border-radius: 10px;
    border-color: cyan;
    font: bold 10px "Montserrat";
    min-width: 5em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: red;
    border-style: inset;
}
'''

QSS_TextCardQuestion = '''QLabel { 
    font: bold 16px "Montserrat";
}'''

QSS_TextResult = '''QLabel {
    font: italic 12px "Montserrat";
}'''

QSS_TextHeader = '''QLabel {
    font: 18px ;
}'''

QSS_menu = '''
QWidget{
background-color: rgb(120, 170, 110); 
    border-width: 10px;
    border-radius: 10px;
    border-color: purple;
    font: 20px "Montserrat";
    min-width: 5em;
    padding: 1px;

}
QPushButton { background-color: rgb(78, 105, 43); 
    border-width: 10px;
    border-radius: 10px;
    border-color: beige;
    font: bold 15px "Montserrat";
    min-width: 50em;
    padding: 1px;
}
QPushButton:pressed {
    background-color: purple;
    border-style: inset;

}


QLineEdit{
    background-color: rgb(90, 120, 70); ;
}'''

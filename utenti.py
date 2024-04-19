import client_style
import Pyro5.client
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from datetime import datetime

global username_data, user_visualized

def set_user(self, username):
    self.ui.dash.setCurrentWidget(self.ui.seguiti)
    set_followed_user(self, username, None)
    self.ui.check_seguiti.setChecked(True)

def search(self, username):
    to_search = self.ui.ricerca_utente.text()
    if(self.ui.check_seguiti.isChecked()):  
        if(len(to_search) == 0):
            set_followed_user(self, username, None)
        else:
            set_followed_user(self, username, to_search)     
    else:
        set_followed_user(self, username, to_search)  

def set_followed_user(self, username, to_search):
    self.ui.table_utenti.clear()
    self.ui.table_utenti_info.clear()
    self.ui.utente_msg_list.clear()
    self.ui.follow_btn.setText("")
    data = None
    global username_data
    if to_search == None:
        reg = Pyro5.client.Proxy("PYRONAME:mythingy")
        data = reg.personal_data(username) 
        username_data = data
    else:
        reg = Pyro5.client.Proxy("PYRONAME:mythingy")
        followed = reg.matching_user(to_search) 
        user = []
        for f in followed:
            if(f["username"] != username):
                user.append(f["username"])
        data = {"utenti_seguiti": user}
     
    self.ui.table_utenti.setRowCount(len(data["utenti_seguiti"])) 
    row=0
    for user in data["utenti_seguiti"]:
        self.ui.table_utenti.setItem(row, 0, QtWidgets.QTableWidgetItem(user))
        user_btn = QPushButton("PROFILO", self) 
        client_style.profile_btn_style(user_btn)                      
        self.ui.table_utenti.setCellWidget(row, 1, user_btn)        
        user_btn.clicked.connect(lambda checked, i=row: show_profile(self, i, data["utenti_seguiti"], username))
        row = row+1
    
def show_profile(self, i, user_info, username):
    global username_data
    self.ui.utente_msg_list.clear()
    follow = False
    for f in username_data["utenti_seguiti"]:
        if f == user_info[i]:
            follow = True

    if follow:
        self.ui.follow_btn.setText("SMETTI DI SEGUIRE")
    else:
        self.ui.follow_btn.setText("SEGUI ORA")

    reg = Pyro5.client.Proxy("PYRONAME:mythingy")
    data = reg.personal_data(user_info[i]) 
    
    self.ui.table_utenti_info.setRowCount(6) 
    row=0
    global user_visualized
    user_visualized = data["username"]
    while row < 6:
        if row == 0:
            self.ui.table_utenti_info.setItem(row, 0, QtWidgets.QTableWidgetItem("NOME UTENTE: " + data["username"]))
            self.ui.table_utenti_info.setItem(row, 1, QtWidgets.QTableWidgetItem("CITTA: " + data["citta"]))
        if row == 1:
            self.ui.table_utenti_info.setItem(row, 0, QtWidgets.QTableWidgetItem("NOME: " + data["nome"]))
            self.ui.table_utenti_info.setItem(row, 1, QtWidgets.QTableWidgetItem("TEMPO LIBERO: " + data["tempo libero"]))
        if row == 2:
            self.ui.table_utenti_info.setItem(row, 0, QtWidgets.QTableWidgetItem("COGNOME: " + data["cognome"]))
            self.ui.table_utenti_info.setItem(row, 1, QtWidgets.QTableWidgetItem("ISCRIZIONE: " + data["iscrizione"]))
        if row == 3:
            self.ui.table_utenti_info.setItem(row, 0, QtWidgets.QTableWidgetItem("ETA: " + data["eta"]))
            self.ui.table_utenti_info.setItem(row, 1, QtWidgets.QTableWidgetItem("SEGUITI: " + str(data["seguiti"])))
        if row == 4:
            self.ui.table_utenti_info.setItem(row, 0, QtWidgets.QTableWidgetItem("SESSO: " + data["sesso"]))
            self.ui.table_utenti_info.setItem(row, 1, QtWidgets.QTableWidgetItem("SEGUACI: " + str(data["seguaci"])))
        if row == 5:
            self.ui.table_utenti_info.setItem(row, 0, QtWidgets.QTableWidgetItem("NAZIONALITA: " + data["nazionalita"]))
            self.ui.table_utenti_info.setItem(row, 1, QtWidgets.QTableWidgetItem("MESSAGGI: " + str(len(data["messaggi"]))))
        row = row+1
    
    follow_or_not = self.ui.follow_btn.text()
    if(follow_or_not == "SMETTI DI SEGUIRE"):
        self.ui.title_msg_utenti.setText("MESSAGGI UTENTE")
        show_user_msg(self, data)
    else:
        if(follow_or_not == "SEGUI ORA"):
            self.ui.title_msg_utenti.setText("UTENTE NON SEGUITO - MESSAGGI NON VISIBILI")

def follow(self, username):
    global user_visualized
    follow_or_not = self.ui.follow_btn.text()
    time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    if(follow_or_not == "SEGUI ORA"):
        reg = Pyro5.client.Proxy("PYRONAME:mythingy")        
        data = reg.un_follow([username, user_visualized, True, time]) 
        self.ui.follow_btn.setText("SMETTI DI SEGUIRE")
        self.ui.title_msg_utenti.setText("MESSAGGI UTENTE")
        show_user_msg(self, data)
        
    else:
        if(follow_or_not == "SMETTI DI SEGUIRE"):
            reg = Pyro5.client.Proxy("PYRONAME:mythingy")
            data = reg.un_follow([username, user_visualized, False, time])
            self.ui.follow_btn.setText("SEGUI ORA")
            self.ui.utente_msg_list.clear()
            seguaci = self.ui.table_utenti_info.item(4, 1).text()
            seguaci = seguaci.replace('SEGUACI: ', '')        
            self.ui.table_utenti_info.setItem(4, 1, QtWidgets.QTableWidgetItem("SEGUACI: "+ str(int(seguaci)-1)))
            self.ui.title_msg_utenti.setText("UTENTE NON SEGUITO - MESSAGGI NON VISIBILI")
            self.ui.check_seguiti.setChecked(False)

def show_user_msg(self, data):
    global user_visualized
    msg_to_order = []
    for msg in data["messaggi"]:
        msg_to_order.append(msg)
        
    self.ui.table_utenti_info.setItem(4, 1, QtWidgets.QTableWidgetItem("SEGUACI: " + str(data["seguaci"])))
    
    list_ordered = sorted(msg_to_order, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d %H:%M:%S'), reverse = True)

    for i in list_ordered:
        time = datetime.strptime(i["data"], '%Y-%m-%d %H:%M:%S')    
        self.ui.utente_msg_list.addItem(i["testo"] + "\n" + str(time.strftime("%H:%M  %d-%m-%Y")))      
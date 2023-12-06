import PySimpleGUI as sg
import sqlite3 as db

class Logs():
    def __init__(self):
        self.test = 10
        with db.connect('salons.db') as con:
            cur = con.cursor()
            cur.execute(""" SELECT sakuma_laiks FROM pieraksts """)
            self.pierakst = cur.fetchall()
            cur.execute(""" SELECT pakalpojuma_nosaukums FROM pakalpojums """)
            self.pakalp = cur.fetchall()
            cur.execute(""" SELECT vards FROM klients """)
            self.klient = cur.fetchall()
            cur.execute(""" SELECT produkta_nosaukums FROM produkti""")
            self.produkt = cur.fetchall()
    
    def izkarto(self):
        self.layout =[[sg.Text('Izvēlieties pierakstu vai izveidojiet jaunu pierakstu')],
                [sg.Text('pieraksts'), sg.Listbox(values=self.pierakst, key='-PIERAKST-', enable_events=True),
                sg.InputText(key='T-PIERAKST-')],
                [sg.Text('pakalpojums', size=(15,1)), sg.Listbox(values=self.pakalp, size=(20,1), key='-PAKALP-', enable_events=True),
                sg.InputText(key='T-PAKALP-')],
                [sg.Text('klients'), sg.Listbox(values=self.klient, size=(30,1), sey='-KLIENT-', enable_events=True),
                sg.InputText(key='T-KLIENT-')],
                [sg.Text('produkti', size=(7,11)), sg.Listbox(values=self.produkt, size=(30,1), key='-PRODUKT-', enable_events=True),
                sg.InputText(key='T-PRODUKT-')],
                [sg.Button('Ievadīt'), sg.Button('Atcelt')]]
        
    def logu_veido(self):
        Logs.izkarto(self)
        window = sg.Window('Salona pieraksti', self.layout)
        return(window)
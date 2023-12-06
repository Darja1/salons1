import PySimpleGUI as sg
import sqlite3 as db

class Logs():
    def __init__(self):
        self.test = 10
        with db.connect('salons.db') as con:
            cur = con.cursor()
            cur.execute("""  """)
            self.pierakst = cur.fetchall()
            cur.execute("""  """)
            self.pakalp = cur.fetchall()
            cur.execute("""  """)
            self.klient = cur.fetchall()
            cur.execute(""" """)
            self.produkt = cur.fetchall()
    
    def izkarto(self):
        self.layout = [
            
        ]
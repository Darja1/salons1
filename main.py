import PySimpleGUI as sg
import sqlite3 as db
from logs import*

def druka_tab(vards, saturs):
    print('\nTabula', vards)
    for rinda in saturs:
        print(rinda)

with db.connect('salons.db') as con:
    cur = con.cursor()
    cur.execute("""SELECT * FROM pieraksts""")
    pierakst = cur.fetchall()
    cur.execute("""SELECT * FROM pakalpojums""")
    pakalp = cur.fetchall()
    cur.execute("""SELECT * FROM klients""")
    klient = cur.fetchall()
    cur.execute("""SELECT * FROM produkti""")
    produkt = cur.fetchall()

druka_tab('pieraksts', pierakst)
druka_tab('pakalpojums', pierakst)
druka_tab('klients', klient)
druka_tab('produkti', produkt)

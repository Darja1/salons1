import sqlite3 as db 
from logs import *
from saglaba import *
import PySimpleGUI as sg

key_ievad = ('T-PIERAKST-','T-PAKALP-','T-KLIENT-','T-PRODUKT-')
key_li = ('-PIERAKST-','-PAKALP-','-KLIENT-','-PRODUKT-')
tab_nosauk =['pieraksts', 'pakalpopjums', 'klients', 'produkti', ]
id_visi = ['pieraksta_id', '', 'klienta_id','pakalpojuma_id' , 'produkta_id']
kolonu_nosauk = ['pieraksts', 'klients', 'pakalpojums']
pakalpojuma_id = []
klienta_id = []
pieraksta_id = []

with db.connect('salons.db') as con:
  cur = con.cursor()
  logs = Logs(cur)
  window = logs.logu_veido()
  event = ""
  while event != sg.WIN_CLOSED and event != 'Atcelt':
    event, values = window.read()
    if event in key_li: 
      text_event = 'T'+event
      values[event] = values[event][0][0] 
      window[text_event].update(values[event]) 
    elif (event == "Ievadīt"): 
      flag = 1; 
      saglabat =[] 
      for x in key_ievad:
        if values[x] == '':
          flag = 0 ; break
        else:
          saglabat.append(values[x]) 
      if flag : 
        sg.popup(saglabat, background_color='#007733') 
        prod1= Saglaba(cur,saglabat[0],tab_nosauk[0],id_visi[0],kolonu_nosauk[0])
        for nr in range(3): 
          pakalpojuma_id.append(
            prod1.saglaba_jauno(cur,saglabat[nr],tab_nosauk[nr],id_visi[nr],kolonu_nosauk[nr])
          ) 
          klienta_id.append(
            prod1.saglaba_jauno(cur,saglabat[nr],tab_nosauk[nr],id_visi[nr],kolonu_nosauk[nr])
          ) 
          pieraksta_id.append(
            prod1.saglaba_jauno(cur,saglabat[nr],tab_nosauk[nr],id_visi[nr],kolonu_nosauk[nr])
          ) 
        print("id_produktiem[nr] = ",pakalpojuma_id)
        prod1.pakalpojums_tab(pakalpojuma_id,saglabat[3])
        prod1.klients_tab(klienta_id,saglabat[1])
        prod1.pieraksts_tab(pieraksta_id,saglabat[2])
        con.commit()  
        for vards in tab_nosauk:
          prod1.druka_tab(vards)
        prod1.produkt_dzesh() 
        con.commit()  
        for vards in tab_nosauk:
          prod1.druka_tab(vards)
      else:
        sg.popup('Kļūda', 'Aizpildīt visus laukus', background_color='#FF0000')
    


















'''with db.connect('salons.db') as con:
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
'''

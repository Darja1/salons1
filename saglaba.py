import sqlite3 as db 
from logs import *
class Saglaba(Logs):
    def __init__(self,cur,jaunu_saglabat,tab_nosauk,id,kolonu_nosauk):
        self.tab_nosauk = tab_nosauk
        self.kolonu_nosauk = kolonu_nosauk
        self.cur = cur
        self.jaunu_saglabat = jaunu_saglabat
        self.id=id
        super().__init__(self.cur)

    def druka_tab(self, tab_nosauk):
        self.tab_nosauk = tab_nosauk
        print('\nTabula ', self.tab_nosauk)
        self.cur.execute(f"""  SELECT  * FROM '{self.tab_nosauk}' """)
        self.saturs = self.cur.fetchall()
        for rinda in self.saturs:
            print (rinda) 

    def saglaba_jauno(self,cur,jaunu_saglabat,tab_nosauk,id,kolonu_nosauk): 
        self.cur.execute(f""" INSERT INTO '{self.tab_nosauk}' ('{self.kolonu_nosauk}') SELECT '{self.jaunu_saglabat}' WHERE NOT EXISTS(SELECT 1 FROM '{self.tab_nosauk}' WHERE "{self.kolonu_nosauk}" = '{self.jaunu_saglabat}') """)

        self.cur.execute(f""" SELECT "{self.id}" FROM '{self.tab_nosauk}' WHERE "{self.kolonu_nosauk}" IN ('{self.jaunu_saglabat}') """)
        return(self.cur.fetchone()[0])
    
    def pakalpojums_tab(self,pakalpojuma_id, produkta_nosaukums):
        self.pakalpojuma_id = pakalpojuma_id
        self.produkta_nosaukums = produkta_nosaukums
        sql = "INSERT INTO pakalpojums( id_kategorija, id_nosaukums, id_tehn_rakstur, nomas_cena_dienaa) VALUES( ?, ?, ?, ?)"
        val = (pakalpojuma_id[0], pakalpojuma_id[1], pakalpojuma_id[2], self.produkta_nosaukums)
        self.cur.execute(sql, val)

    def klients_tab(self,klienta_id ,vards ):
        self.klienta_id = klienta_id
        self.vards = vards
        sql = "INSERT INTO klients ( id_nosaukums, vards) VALUES( ?, ?)"
        val = (klienta_id[0], self.vards)
        self.cur.execute(sql, val)

    def pieraksts_tab(self,pieraksta_id, sakuma_laiks):
        self.pieraksta_id = pieraksta_id
        self.sakuma_laiks = sakuma_laiks
        sql = "INSERT INTO pieraksts ( id_tehn_rakstur, sakuma_laiks) VALUES( ?, ?)"
        val = (pieraksta_id[1], self.sakuma_laiks)
        self.cur.execute(sql, val)

    def produkt_dzesh(self):
        print("====================================")
        ped_ieraksts = self.cur.lastrowid 
        print( "pēdējās rindas id= ",ped_ieraksts)
        self.cur.execute("DELETE FROM klients WHERE klienta_id = 1")
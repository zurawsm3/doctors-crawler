# -*- coding: utf-8 -*-
import psycopg2

class doctorsProjectPipeline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        """
            PARAMETRY BAZY DANYCH
        """
        hostname = 'db'
        username = 'postgres'
        password = 'postgres123' # your password
        database = 'baza_lekarzy'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        self.cur.execute("DROP TABLE IF EXISTS staze;")
        self.cur.execute("DROP TABLE IF EXISTS choroby;")
        self.cur.execute("DROP TABLE IF EXISTS nagrody;")
        self.cur.execute("DROP TABLE IF EXISTS publikacje;")
        self.cur.execute("DROP TABLE IF EXISTS jezyki;")
        self.cur.execute("DROP TABLE IF EXISTS szkoly;")
        self.cur.execute("DROP TABLE IF EXISTS specjalizacje;")
        self.cur.execute("DROP TABLE IF EXISTS opinie;")
        self.cur.execute("DROP TABLE IF EXISTS adresy;")
	self.cur.execute("DROP TABLE IF EXISTS zawod;")
        self.cur.execute("DROP TABLE IF EXISTS tablica;")


        self.cur.execute("CREATE TABLE tablica(id_lekarz serial PRIMARY KEY, imie VARCHAR , nazwisko_lekarza VARCHAR, tytuly VARCHAR, o_mnie VARCHAR);")
        self.cur.execute("CREATE TABLE staze(id_staz serial PRIMARY KEY, nazwa_stazu VARCHAR , id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE choroby(id_choroby serial PRIMARY KEY, leczona_choroba VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE nagrody(id_nagrody serial PRIMARY KEY, nagroda VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE publikacje(id_publikacji serial PRIMARY KEY, publikacja VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE jezyki(id_jezyka serial PRIMARY KEY, jezyk VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE szkoly(id_szkoly serial PRIMARY KEY, szkola VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE specjalizacje(id_specjalizacji serial PRIMARY KEY, specjalizacja VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
        self.cur.execute("CREATE TABLE opinie(id_opinii serial PRIMARY KEY, id_lekarza INTEGER REFERENCES tablica(id_lekarz), ocena INTEGER, opinia VARCHAR);")
        self.cur.execute("CREATE TABLE adresy(id_adresu serial PRIMARY KEY, nazwa_firmy VARCHAR, wojewodztwo VARCHAR, miasto VARCHAR, ulica VARCHAR, kod_pocztowy VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")
	self.cur.execute("CREATE TABLE zawod(id_zawodu serial PRIMARY KEY, zawod VARCHAR, id_lekarza INTEGER REFERENCES tablica(id_lekarz));")


    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


    def process_item(self, item, spider):
        """
            WRZUCANIE DANYCH DO TABLICY
        """
        self.cur.execute("insert into tablica(imie, nazwisko_lekarza, tytuly, o_mnie ) VALUES (%s, %s, %s, %s) RETURNING id_lekarz;", (item['imie'], item['nazwisko'], item['tytuly'], item['o_mnie']))
        id_lekarskie = self.cur.fetchone()
        for i in item['staze']:
            self.cur.execute("insert into staze(nazwa_stazu, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i in item['choroby']:
            self.cur.execute("insert into choroby(leczona_choroba, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i in item['nagrody_i_wyroznienia']:
            self.cur.execute("insert into nagrody(nagroda, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i in item['publikacje']:
            self.cur.execute("insert into publikacje(publikacja, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i in item['znajomosc_jezykow']:
            self.cur.execute("insert into jezyki(jezyk, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i in item['ukonczone_szkoly']:
            self.cur.execute("insert into szkoly(szkola, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i in item['specjalizacje']:
            self.cur.execute("insert into specjalizacje(specjalizacja, id_lekarza) values(%s, %s)", (i, id_lekarskie))
        for i, k in zip(item['ocena'], item['tresc_opinii']):
            self.cur.execute("insert into opinie(id_lekarza, ocena, opinia) values(%s, %s, %s)", (id_lekarskie, i, k))
        for i, k, x, y, z in zip(item['nazwa_firmy'], item['wojewodztwo'], item['miasto'], item['kod_pocztowy'], item['ulica']):
            self.cur.execute("insert into adresy(id_lekarza, nazwa_firmy, wojewodztwo, miasto, kod_pocztowy, ulica) values(%s, %s, %s, %s, %s, %s)", (id_lekarskie, i, k, x, y, z))
	for i in item['zawod']:
	    self.cur.execute("insert into zawod(zawod, id_lekarza) values(%s, %s)", (i, id_lekarskie))

        self.connection.commit()


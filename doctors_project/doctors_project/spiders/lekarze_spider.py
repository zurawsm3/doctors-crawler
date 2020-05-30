#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from doctors_project.items import doctorsProjectItem
import os 
import scrapy
# import selenium
# from selenium import selenium

#from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
class QuotesSpider(scrapy.Spider):


    name = "doctors"
    allowed_domains = ["doctors.pl"]
    """
        MIASTA
    """
    miejscowosci = []
	### zmiana do dockera ####

    

#    with open('/home/marcin/Pulpit/scrapy_pro/doctors_project/doctors_project/spiders/niepowtarzajace_mazowieckie.csv', 'rb') as csvfile:
    with open('/doctors_project/spiders/no_repea_city_pol.csv', 'rb') as csvfile:
        czytnik = csv.reader(csvfile, delimiter=' ')
        for i in czytnik:
            miejscowosci.append(i[0])

#    miejscowosci = ['wegrow', 'minsk-mazowiecki', 'sokolow-podlaski', 'siedlce', 'warszawa']
    tablica_linkow = []
    for miasto in miejscowosci:
        tablica_linkow.append('https://www.doctors.pl/lokalizacja/{}-polska/stomatolog'.format(miasto)),
	tablica_linkow.append('https://www.doctors.pl/lokalizacja/{}-polska/ortodonta'.format(miasto))

    start_urls = tablica_linkow
    #
    # def __init__(self):
    #     self.driver = webdriver.Firefox()

    def parse(self, response):
	global nazwisko, imie, tytuly
        if response.xpath('//*[@class="col-xs-9 col-sm-10  col-md-9 content"]'):
            for lekarz in response.xpath('//*[@class="col-xs-9 col-sm-10  col-md-9 content"]'):
                item = doctorsProjectItem()

                lista_stringow = lekarz.xpath('h3/a/span/text()').extract_first().split()
		#global nazwisko, imie, tytuly
		imie = ''
		tytuly = ''
		### naz - naz
		if lista_stringow[-2] == '-':
		    nazwisko = lista_stringow[-3]+lista_stringow[-2]+lista_stringow[-1]
		    del lista_stringow[-3], lista_stringow[-2], lista_stringow[-1]
		    for i in lista_stringow:
			if (i[-1] != '.') and (i != 'dr'):        
			    imie += i
			    if (len(lista_stringow) == 2) and (i != lista_stringow[-1]):
				imie += ' '
			else:
			    tytuly = tytuly + i + ' '
		### naz- naz
		### naz -naz
		elif (lista_stringow[-2][-1] == '-') or (lista_stringow[-1][0] == '-'):
		    nazwisko = lista_stringow[-2] + lista_stringow[-1]
		    del lista_stringow[-2], lista_stringow[-1]
		    for i in lista_stringow:
			if (i[-1] != '.') and (i != 'dr'):        
			    imie += i
			    if (len(lista_stringow) == 2) and (i != lista_stringow[-1]):
				imie += ' '
			else:
			    tytuly = tytuly + i + ' '
		### naz-naz
		else:
		    nazwisko = lista_stringow[-1]
		    del lista_stringow[-1]
		    for i in lista_stringow:
			if (i[-1] != '.') and (i != 'dr'):        
			    imie += i
			    if (len(lista_stringow) == 2) and (i != lista_stringow[-1]):
				imie += ' '
			else:
			    tytuly = tytuly + i + ' '





               # item['nazwisko'] = (nazwa[-1])
                #del nazwa[-1]
                #imie = ''
                #tytuly = ''
                #for i in nazwa:
                #    if (i[-1] != '.') and (i != 'dr'):
                #        imie = imie + i + ' '
                #    else:
                #        tytuly = tytuly + i + ' '
#
		item['nazwisko'] = nazwisko
                item['imie'] = imie
                item['tytuly'] = tytuly
                item['nazwa'] = lekarz.xpath('h3/a/span/text()').extract_first()

                link_do_profilu = lekarz.xpath('h3/a[@class="rank-element-name__link"]/@href').extract_first()
                item['tresc_opinii'] = []
                item['ocena'] = []
                item['miasto'] = []
                item['nazwa_firmy'] = []
                item['o_mnie'] = ''
                item['specjalizacje'] = []
                item['ukonczone_szkoly'] = []
                item['znajomosc_jezykow'] = []
                item['publikacje'] = []
                item['nagrody_i_wyroznienia'] = []
                item['staze'] = []
                item['choroby'] = []
                item['ulica'] = []
                item['kod_pocztowy'] = []
                item['wojewodztwo'] = []
		item['zawod'] = []
               # item['telefon'] = ''
               # item['link'] = ''
                request = scrapy.Request(link_do_profilu, callback=self.parse_page_profil)
                request.meta['item'] = item
                yield request
            # self.ini_profil(response.xpath('//*[@class="col-xs-9 col-sm-10  col-md-9 content"]'))
        if response.xpath('//*[@class="col-xs-9 col-sm-10  col-md-10 content"]'):
            # self.ini_profil(response.xpath('//*[@class="col-xs-9 col-sm-10  col-md-10 content"]'))
            for lekarz in response.xpath('//*[@class="col-xs-9 col-sm-10  col-md-10 content"]'):
                item = doctorsProjectItem()
                lista_stringow = lekarz.xpath('h3/a/span/text()').extract_first().split()
		#global nazwisko, imie, tytuly
		imie = ''
		tytuly = ''
		### naz - naz
		if lista_stringow[-2] == '-':
		    nazwisko = lista_stringow[-3]+lista_stringow[-2]+lista_stringow[-1]
		    del lista_stringow[-3], lista_stringow[-2], lista_stringow[-1]
		    for i in lista_stringow:
			if (i[-1] != '.') and (i != 'dr'):        
			    imie += i
			    if (len(lista_stringow) == 2) and (i != lista_stringow[-1]):
				imie += ' '
			else:
			    tytuly = tytuly + i + ' '
		### naz- naz
		### naz -naz
		elif (lista_stringow[-2][-1] == '-') or (lista_stringow[-1][0] == '-'):
		    nazwisko = lista_stringow[-2] + lista_stringow[-1]
		    del lista_stringow[-2], lista_stringow[-1]
		    for i in lista_stringow:
			if (i[-1] != '.') and (i != 'dr'):        
			    imie += i
			    if (len(lista_stringow) == 2) and (i != lista_stringow[-1]):
				imie += ' '
			else:
			    tytuly = tytuly + i + ' '
		### naz-naz
		else:
		    nazwisko = lista_stringow[-1]
		    del lista_stringow[-1]
		    for i in lista_stringow:
			if (i[-1] != '.') and (i != 'dr'):        
			    imie += i
			    if (len(lista_stringow) == 2) and (i != lista_stringow[-1]):
				imie += ' '
			else:
			    tytuly = tytuly + i + ' '


               
		# for i in nazwa:
		#    if (i[-1] != '.') and (i!='dr'):

		#item['nazwisko'] = (nazwa[-1])
                #del nazwa[-1]
                #imie = ''
                #tytuly = ''
                #for i in nazwa:
                #    if (i[-1] != '.') and (i != 'dr'):
                #        imie = imie + i + ' '
                #    else:
                #        tytuly = tytuly + i + ' '
		item['nazwisko'] = nazwisko
                item['imie'] = imie
                item['tytuly'] = tytuly
                item['nazwa'] = lekarz.xpath('h3/a/span/text()').extract_first()
                link_do_profilu = lekarz.xpath('h3/a[@class="rank-element-name__link"]/@href').extract_first()
                item['tresc_opinii'] = []
                item['ocena'] = []
                item['miasto'] = []
                item['nazwa_firmy'] = []
                item['o_mnie'] = ''
                item['specjalizacje'] = []
                item['ukonczone_szkoly'] = []
                item['znajomosc_jezykow'] = []
                item['publikacje'] = []
                item['nagrody_i_wyroznienia'] = []
                item['staze'] = []
                item['choroby'] = []
                item['ulica'] = []
                item['kod_pocztowy'] = []
                item['wojewodztwo'] = []
		item['zawod'] = []
               # item['telefon'] = ''
               # item['link'] = []
                request = scrapy.Request(link_do_profilu, callback=self.parse_page_profil)
                request.meta['item'] = item
                yield request

        next_page = response.css('link[rel="next"]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



    def parse_page_profil(self, response):

            item = response.meta['item']


            """
            OCENY I 

            """
            if not response.xpath('//*[@class="list-unstyled col-md-12"]'):
                for opinia in response.xpath('//*[@class="list-unstyled col-md-9"]/li[@class="opinion "]/div[@class="opinion__content"]'):
                    opinia_klienta = ''
                    tablica_opinii = opinia.xpath('p/text()').extract()
                    for i in map(unicode.strip, tablica_opinii):
                        # opinia_klienta += '\n'
                        opinia_klienta += i
                    item['tresc_opinii'].append(opinia_klienta)
                    item['ocena'].append(opinia.xpath('div[@class="opinion__details"]/div[@class="rating rating--md"]/@data-score').extract_first())

            else:
                for opinia in response.xpath('//*[@class="list-unstyled col-md-12"]/li[@class="opinion "]/div[@class="opinion__content"]'):
                    opinia_klienta = ''
                    tablica_opinii = opinia.xpath('p/text()').extract()
                    for i in map(unicode.strip, tablica_opinii):
                        opinia_klienta += i
                    item['tresc_opinii'].append(opinia_klienta)
                    item['ocena'].append(opinia.xpath('div[@class="opinion__details"]/div[@class="rating rating--md"]/@data-score').extract_first())



            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                request2 = scrapy.Request(next_page, callback=self.parse_page_profil)
                request2.meta['item'] = item
                yield request2
            else:
                """ 
                    DANE ADRESOWE FIRMY
                """
                if response.xpath('//*[@class="non-commercial-address  "]'):
                    for adres in response.xpath('//div[@class="non-commercial-address__content col-sm-12 padding-right-0 padding-left-0"]'):
                        if adres.xpath('h2/a[@class="text-base-color"]'):
                            item['nazwa_firmy'].append(adres.xpath('h2/a[@class="text-base-color"]/span/text()').extract_first())  ############
                        elif adres.xpath('h2/span/text()'):
                            if adres.xpath('h2/span/text()'):
                                item['nazwa_firmy'].append((adres.xpath('h2/span/text()').extract_first().lstrip()).rstrip())
                        if adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="streetAddress"]/text()'):
			    ###ZABAWA Z UL NA POCZATKU######!!!!!!!!!!!!!!!!!!!!!!####
			    ulica = adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="streetAddress"]/text()').extract_first()
			    #if ulica is not None:
			       #  ulicast = ulica.encode('ascii', 'ignore')
			         # if ulicast.startswith("ul."):
				    #    ulicast = ulicast[3:]
				    #item['ulica'].append(ulicast)
                            item['ulica'].append(ulica)
                        if adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="postalCode"]/text()'):
			    ###WARUNEK n/a i telefon###
			    kod_pocztowy = adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="postalCode"]/text()').extract_first()
			    if kod_pocztowy is not None: 
			        if  (('N' not in kod_pocztowy) and (len(kod_pocztowy)<=8)):
                            	    item['kod_pocztowy'].append(kod_pocztowy)
                        if adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="addressLocality"]/text()'):
                            item['miasto'].append(adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="addressLocality"]/text()').extract_first())
                        if adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="addressRegion"]/text()'):
                            item['wojewodztwo'].append(adres.xpath('p[@class="offset-bottom-0 text-muted"]/span[@itemprop="addressRegion"]/text()').extract_first())
                elif response.xpath('//*[@class="name-header h5"]'):
                    for nazwa_firmy  in response.xpath('//*[@class="name-header h5"]'):
                        if nazwa_firmy.xpath('a/span'):
                            item['nazwa_firmy'].append(nazwa_firmy.xpath('a/span/text()').extract_first())
                        if nazwa_firmy.xpath('span'):
                            item['nazwa_firmy'].append((nazwa_firmy.xpath('span/text()').extract_first().lstrip()).rstrip())
                if response.xpath('//*[@class="adrData"]'):
                    for adresy in response.xpath('//*[@class="adrData"]'):
                        # if adresy.xpath('span[@itemprop="streetAddress"]/text()'):
                        #     item['ulica'].append(adresy.xpath('span[@itemprop="streetAddress"]/text()').extract_first())
                        # if adresy.xpath('span[@itemprop="postalCode"]/text()'):
                        #     item['kod_pocztowy'].append(adresy.xpath('span[@itemprop="postalCode"]/text()').extract_first())
                        # if adresy.xpath('span[@itemprop="addressLocality"]/text()'):
                        #     item['miasto'].append(adresy.xpath('span[@itemprop="addressLocality"]/text()').extract_first())
                        # if adresy.xpath('span[@itemprop="addressRegion"]/text()'):
                        #     item['wojewodztwo'].append(adresy.xpath('span[@itemprop="addressRegion"]/text()').extract_first())
                        #if adresy.xpath('span[@itemprop="streetAddress"]/text()'):
			###ZABAWA Z ULICA###
			ulica = adresy.xpath('span[@itemprop="streetAddress"]/text()').extract_first()
    			#if ulica is not None:
			   # ulicast = ulica.encode('ascii', 'ignore')
			    #if ulicast.startswith("ul."):
			     #   # print("WESZLO DRUGIE UNICODE")
    			      #  ulicast = ulicast[3:]
                            #item['ulica'].append(ulicast)
                        item['ulica'].append(ulica)

                        # item['ulica'].append()
                        # if adresy.xpath('span[@itemprop="postalCode"]/text()'):
			###DODANIE WARUNKU #n/a###
			kod_pocztowy = adresy.xpath('span[@itemprop="postalCode"]/text()').extract_first()
			#print(type(kod_pocztowy))
			if kod_pocztowy is not None: 
			    if  (('N' not in kod_pocztowy) and (len(kod_pocztowy)<=8)):
                                item['kod_pocztowy'].append(kod_pocztowy)
                        # if adresy.xpath('span[@itemprop="addressLocality"]/text()'):
                        item['miasto'].append(adresy.xpath('span[@itemprop="addressLocality"]/text()').extract_first())
                        # if adresy.xpath('span[@itemprop="addressRegion"]/text()'):
                        item['wojewodztwo'].append(adresy.xpath('span[@itemprop="addressRegion"]/text()').extract_first())

                """
                    O MNIE
                """
                if response.xpath('//*[@data-expander-detail-class="about-me-detail"]'):
                    omnie = ''
                    tablica = response.xpath('//*[@data-expander-detail-class="about-me-detail"]/text()').extract()
                    for i in map(unicode.strip, tablica):
                        omnie += i
                    if omnie:
                        item['o_mnie'] = omnie
                """
                    SPECJALIZACJE
                """
                if response.xpath('//*[@class="item item--specialization"]'):
                    for specjalizacja in response.xpath('//*[@class="item item--specialization"]/div/ul/li'):
                        item['specjalizacje'].append((specjalizacja.xpath('text()').extract_first().lstrip()).rstrip())
		else:
		    brak=['brak specjalizacji']
		    item['specjalizacje'].append(brak[0])
                """
                    UKONCZONE SZKOLY
                """
                if response.xpath('//*[@class="item item--school"]'):
                    for szkola in response.xpath('//*[@class="item item--school"]/div/ul/li'):
                        item['ukonczone_szkoly'].append((szkola.xpath('text()').extract_first().lstrip()).rstrip())
                """
                    ZNANE JEZYKI
                """
                if response.xpath('//*[@class="item item--language"]'):
                    for jezyk in response.xpath('//*[@class="item item--language"]/div/ul/li'):
                        item['znajomosc_jezykow'].append((jezyk.xpath('text()').extract_first().lstrip()).rstrip())
                """
                    PUBLIKACJE
                """
                if response.xpath('//*[@class="item item--publication"]'):
                    for publikacja in response.xpath('//*[@class="item item--publication"]/div/ul/li'):
                        item['publikacje'].append((publikacja.xpath('text()').extract_first().lstrip()).rstrip())
                """
                    NAGRODY_I_WYROZNIENIA
                """
                if response.xpath('//*[@class="item item--prize"]'):
                    for nagroda in response.xpath('//*[@class="item item--prize"]/div/ul/li'):
                        item['nagrody_i_wyroznienia'].append((nagroda.xpath('text()').extract_first().lstrip()).rstrip())
                """
                    STAZE
                """
                if response.xpath('//*[@class="item item--practice"]'):
                    for staz in response.xpath('//*[@class="item item--practice"]/div/ul/li'):
                        item['staze'].append((staz.xpath('text()').extract_first().lstrip()).rstrip())
                """
                    CHOROBY
                """
                if response.xpath('//*[@class="item item--doctor_disease"]'):
                    for choroby in response.xpath('//*[@class="item item--doctor_disease"]/div/ul/li'):
                        if choroby.xpath('a/text()'):
                            item['choroby'].append((choroby.xpath('a/text()').extract_first().lstrip()).rstrip())
                        elif choroby.xpath('text()'):
                            item['choroby'].append((choroby.xpath('text()').extract_first().lstrip()).rstrip())
		"""
		   ZAWOD
		"""
		if response.xpath('//h2[@class="text-muted h5 text-base-weight offset-bottom-0"]/a[@class="text-muted"]'):
		    for zawodzik in response.xpath('//h2[@class="text-muted h5 text-base-weight offset-bottom-0"]/a'):
			item['zawod'].append(zawodzik.xpath('text()').extract_first())
		elif response.xpath('//h2[@class="h4 text-muted text-base-weight"]'):
		    for zawodzik in response.xpath('//h2[@class="h4 text-muted text-base-weight"]/a'):
			item['zawod'].append(zawodzik.xpath('text()').extract_first())

                yield item




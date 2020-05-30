# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class doctorsProjectItem(scrapy.Item):
    ulica = scrapy.Field()
    kod_pocztowy = scrapy.Field()
    nazwa = scrapy.Field()
    tresc_opinii = scrapy.Field()
    ocena = scrapy.Field()
    nazwisko = scrapy.Field()
    miasto = scrapy.Field()
    wojewodztwo = scrapy.Field()
    nazwa_firmy = scrapy.Field()
    o_mnie = scrapy.Field()
    specjalizacje = scrapy.Field()
    ukonczone_szkoly = scrapy.Field()
    znajomosc_jezykow = scrapy.Field()
    publikacje = scrapy.Field()
    nagrody_i_wyroznienia = scrapy.Field()
    staze = scrapy.Field()
    choroby = scrapy.Field()
    imie = scrapy.Field()
    #telefon = scrapy.Field()
    #link = scrapy.Field()
    tytuly = scrapy.Field()
    zawod = scrapy.Field()
    # "-----------------------------"
    image_urls = scrapy.Field()
    images = scrapy.Field()



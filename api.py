##############################################################################################################################
from tkinter import E
from xml.etree.ElementTree import QName
import bs4
import urllib.request
import pandas as pd
#import lxml
#import cchardet
import pymysql
import mysql.connector
import configparser
import concurrent.futures
import re
import numpy as np
import time
from datetime import datetime
from tqdm import tqdm #progress bar
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from optparse import Values
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from random import randrange
from tqdm import tqdm #progress bar
import glob
import os
import datetime
import time
import pandas as pd
import numpy as np
import re
import itertools
from selenium.webdriver.firefox.options import Options
from icecream import ic
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json
from pandas import json_normalize

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {'Return' : "Home"}, 200
    def post(self):
        #ic(request.data)  # raw data
        #ic(request.json)  # json (if content-type of application/json is sent with the request)
        #ic(request.get_json(force=True))  # json (if content-type of application/json is not sent)
        r = request.json
        #ic(r) # dict

        df = pd.DataFrame.from_dict([r]) 
        ic(df) # df

        brand = df.brand.to_string(index=False)
        ic(brand)
        model = df.model.to_string(index=False)
        ic(model)
        bodyType = df.bodyType.to_string(index=False)
        ic(bodyType)
        fuelTypes = df.fuelTypes.to_string(index=False)
        ic(fuelTypes)
        gearBoxes = df.gearBoxes.to_string(index=False)
        ic(gearBoxes)
        doors = df.doors.to_string(index=False)
        ic(doors)
        kilometerFrom = df.kilometerFrom.to_string(index=False)
        ic(kilometerFrom)
        kilometerTo = df.kilometerTo.to_string(index=False)
        ic(kilometerTo)
        yearFrom = df.yearFrom.to_string(index=False)
        ic(yearFrom)
        yearTo = df.yearTo.to_string(index=False)
        ic(yearTo)
        powerFrom = df.powerFrom.to_string(index=False)
        ic(powerFrom)
        powerTo = df.powerTo.to_string(index=False)
        ic(powerTo)

        mydb = mysql.connector.connect(
            host="localhost", #127.0.0.1  #65.108.125.124
            user="root",
            password="Wiveda2023!",
            database="price_prediction"
            )
        mycursor = mydb.cursor()


        #def mobile(self):

        sql_brand_from_form = " select id from `car_brands` where `name` = %s "
        tuple1 = (brand,)
        mycursor.execute(sql_brand_from_form,tuple1)
        columns = [desc[0] for desc in mycursor.description]
        brand_from_form  = pd.DataFrame(mycursor.fetchall(), columns=columns)
        brand_form = brand_from_form.id.to_string(index=False)
        ic(brand_form)
        ############################################################################################################################
        sql_brand = " select * from `transforms` where `relation_type` = 'brand' and `relation_id` = %s and `target_system` = 'mobilede' "
        tuple_brand_m = (brand_form,)
        mycursor.execute(sql_brand,tuple_brand_m) 
        columns = [desc[0] for desc in mycursor.description]
        brands = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkBrandforMobile = brands.target_value.to_string(index=False)
        ic(linkBrandforMobile)
        ############################################################################################################################
        sql_model_from_form = " select id from `car_brand_models` where `name` = %s " 
        tuple2 = (model,)
        mycursor.execute(sql_model_from_form,tuple2)
        columns = [desc[0] for desc in mycursor.description]
        model_from_form  = pd.DataFrame(mycursor.fetchall(), columns=columns)
        model_form = model_from_form.id.to_string(index=False)
        ic(model_form)
        ############################################################################################################################
        sql_model = " select * from `transforms` where `relation_type` = 'model' and `relation_id` = %s and `target_system` = 'mobilede' "
        tuple_model_m = (model_form,)
        mycursor.execute(sql_model,tuple_model_m) 
        columns = [desc[0] for desc in mycursor.description]
        models = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkModelforMobile = models.target_value.to_string(index=False)
        ic(linkModelforMobile)
        ############################################################################################################################
        sql_bodyType_from_form = " select id from `bodytype` where `bodyType` = %s "
        tuple3 = (bodyType,)
        mycursor.execute(sql_bodyType_from_form,tuple3)                             
        columns = [desc[0] for desc in mycursor.description]
        bodyType_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        bodyType_form = bodyType_from_form.id.to_string(index=False)
        ic(bodyType_form)
        ############################################################################################################################
        sql_bodyType = " select * from `transforms` where `relation_type` = 'bodyType'and `relation_id` = %s and `target_system` = 'mobilede' "
        tuple_bodyType_m = (bodyType_form,)
        mycursor.execute(sql_bodyType,tuple_bodyType_m)
        columns = [desc[0] for desc in mycursor.description]
        bodyTypes = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkBodyTypeforMobile = bodyTypes.target_value.to_string(index=False)
        ic(linkBodyTypeforMobile)
        ############################################################################################################################
        sql_fuelTypes_from_form = " select id from `fueltypes` where `fuelTypes` = %s "
        tuple4 = (fuelTypes,)
        mycursor.execute(sql_fuelTypes_from_form,tuple4)
        columns = [desc[0] for desc in mycursor.description]
        fuelTypes_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        fuelType_form = fuelTypes_from_form.id.to_string(index=False)
        ic(fuelType_form)
        ############################################################################################################################
        sql_fuelType = " select * from `transforms` where `relation_type` = 'fuelTypes' and `relation_id` = %s and `target_system` = 'mobilede' "
        tuple_fuelType_m = (fuelType_form,)
        mycursor.execute(sql_fuelType,tuple_fuelType_m)
        columns = [desc[0] for desc in mycursor.description]
        fuelType = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkfuelTypesforMobile = fuelType.target_value.to_string(index=False)
        ic(linkfuelTypesforMobile)
        ############################################################################################################################
        sql_gearBoxes_from_form = " select id from `gearboxes` where `gearBoxes` = %s " 
        tuple5 = (gearBoxes,)
        mycursor.execute(sql_gearBoxes_from_form,tuple5)
        columns = [desc[0] for desc in mycursor.description]
        gearBoxes_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        gearBox_form = gearBoxes_from_form.id.to_string(index=False)
        ic(gearBox_form)
        ############################################################################################################################
        sql_gearBox = " select * from `transforms` where `relation_type` = 'gearBoxes' and `relation_id` = %s and `target_system` = 'mobilede' "
        tuple_gearBox_m = (gearBox_form,)
        mycursor.execute(sql_gearBox,tuple_gearBox_m)
        columns = [desc[0] for desc in mycursor.description]
        gearBox = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkGearBoxesforMobile = gearBox.target_value.to_string(index=False)
        ic(linkGearBoxesforMobile)
        ############################################################################################################################
        sql_doors_from_form = " select id from `doors` where `doors` = %s " 
        tuple6 = (doors,)
        mycursor.execute(sql_doors_from_form,tuple6)
        columns = [desc[0] for desc in mycursor.description]
        doors_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        door_form = doors_from_form.id.to_string(index=False)
        ic(door_form)
        ############################################################################################################################
        sql_door = " select * from `transforms` where `relation_type` = 'doors' and `relation_id` = %s and `target_system` = 'mobilede' "
        tuple_door_m = (door_form,)
        mycursor.execute(sql_door,tuple_door_m)
        columns = [desc[0] for desc in mycursor.description]
        door = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkdoorsforMobile = door.target_value.to_string(index=False)
        ic(linkdoorsforMobile)
        ############################################################################################################################

        mobileDeUrl  = "https://suchen.mobile.de/fahrzeuge/search.html"

        mobileDeLastUrl = mobileDeUrl + "?" +"isSearchRequest=true&dam=0&" + "ms=" + linkBrandforMobile + ";" + linkModelforMobile + "&sortOption.sortBy=searchNetGrossPrice&sortOption.sortOrder=ASCENDING&cn=DE" + "&ml=" + kilometerFrom + ":" + kilometerTo + "&fr=" + yearFrom + ":" + yearTo + "&ft=" + linkfuelTypesforMobile + "&tr=" + linkGearBoxesforMobile + "&powertype=kW"  + "&pw=" + powerFrom + ":" + powerTo + "&c=" + linkBodyTypeforMobile + "&" + linkdoorsforMobile

        ic(mobileDeLastUrl)


#        options = webdriver.ChromeOptions()
#        prefs = {"profile.managed_default_content_settings.images": 2}
#        #options.add_argument('headless')
         #options.headless = True
#        options.add_experimental_option("prefs", prefs)
#        service = Service(executable_path = '/usr/bin/chromium-browser')
#        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
###########
        fireFoxOptions = Options()
        #fireFoxOptions.binary_location = "/usr/bin/firefox"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        fireFoxOptions.FirefoxBinary = "/usr/bin/firefox"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        #fireFoxOptions.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        fireFoxOptions.add_argument("--headless")
        # fireFoxOptions.add_argument("--window-size=1920,1080")
        # fireFoxOptions.add_argument('--start-maximized')
        fireFoxOptions.add_argument('--disable-gpu')
        fireFoxOptions.add_argument('--no-sandbox')
 
        driver = webdriver.Firefox(options=fireFoxOptions)

        pricelist_mobile = []

        # get the link
        driver.get(mobileDeLastUrl)
        #ic(mobileDeLastUrl)

#        driver.delete_all_cookies()
        time.sleep(1)    #BAK #5

#        driver.find_element(By.XPATH, '/html/body/div[10]/div[2]/div[2]/div[1]/button').click()

#        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.ID, "dsp-upper-search-btn")).click()

        base_source = driver.page_source
        base_soup = BeautifulSoup(base_source, 'html.parser')


        for prices in base_soup.findAll('span', {'class': re.compile('h3 u-block')}):
            pricelist_mobile.append(prices.get_text())

        pricelist_mobile = list(map(lambda x: x.replace('.', ''), pricelist_mobile))
        pricelist_mobile = list(map(lambda x: x.replace('\xa0', ''), pricelist_mobile))
        pricelist_mobile = list(map(lambda x: x.replace('€', ''), pricelist_mobile))
        ic(pricelist_mobile)

        driver.close()   #BAK  

        if pricelist_mobile != []:
            int_pricelist_mobile = [eval(i) for i in pricelist_mobile]
            averageprice_mobile = int(sum(int_pricelist_mobile) / len(pricelist_mobile))
            ic(averageprice_mobile)
        else:
            averageprice_mobile = 0
            ic(averageprice_mobile)
        #
        #    return {'averageprice_mobile:': averageprice_mobile}, 200  # return data and 200 OK
        #else:
        #    return {'averageprice_mobile:': 0}, 200

        #def autoscout(self):

        ic("---------------------------------------------------------------")

        sql_brand_from_form = " select id from `car_brands` where `name` = %s " 
        tuple7 = (brand,)
        mycursor.execute(sql_brand_from_form,tuple7)
        columns = [desc[0] for desc in mycursor.description]
        brand_from_form  = pd.DataFrame(mycursor.fetchall(), columns=columns)
        brand_form = brand_from_form.id.to_string(index=False)
        ic(brand_form)
        ############################################################################################################################
        sql_brand = " select * from `transforms` where `relation_type` = 'brand' and `relation_id` = %s and `target_system` = 'autoscout' "
        tuple_brand_as = (brand_form,)
        mycursor.execute(sql_brand,tuple_brand_as)                                                       
        columns = [desc[0] for desc in mycursor.description]
        brands = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkBrandforAutoscout = brands.target_value.to_string(index=False)
        ic(linkBrandforAutoscout)
        ############################################################################################################################
        sql_model_from_form = " select id from `car_brand_models` where `name` = %s " 
        tuple8 = (model,)
        mycursor.execute(sql_model_from_form,tuple8)
        columns = [desc[0] for desc in mycursor.description]
        model_from_form  = pd.DataFrame(mycursor.fetchall(), columns=columns)
        model_form = model_from_form.id.to_string(index=False)
        ic(model_form)
        ############################################################################################################################
        sql_model = " select * from `transforms` where `relation_type` = 'model' and `relation_id` = %s and `target_system` = 'autoscout' "
        tuple_model_as = (model_form,)
        mycursor.execute(sql_model,tuple_model_as)                                                               
        columns = [desc[0] for desc in mycursor.description]
        models = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkModelforAutoscout = models.target_value.to_string(index=False)
        ic(linkModelforAutoscout)
        ############################################################################################################################
        sql_bodyType_from_form = " select id from `bodytype` where `bodyType` = %s " 
        tuple9 = (bodyType,)
        mycursor.execute(sql_bodyType_from_form,tuple9)                             
        columns = [desc[0] for desc in mycursor.description]
        bodyType_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        bodyType_form = bodyType_from_form.id.to_string(index=False)
        ic(bodyType_form)
        ############################################################################################################################
        sql_bodyType = " select * from `transforms` where `relation_type` = 'bodyType'and `relation_id` = %s and `target_system` = 'autoscout' "
        tuple_bodyType_as = (bodyType_form,)
        mycursor.execute(sql_bodyType,tuple_bodyType_as)                                                                                                 
        columns = [desc[0] for desc in mycursor.description]
        bodyTypes = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkBodyTypeforAutoscout = bodyTypes.target_value.to_string(index=False)
        ic(linkBodyTypeforAutoscout)
        ############################################################################################################################
        sql_fuelTypes_from_form = " select id from `fueltypes` where `fuelTypes` = %s " #form
        tuple10 = (fuelTypes,)
        mycursor.execute(sql_fuelTypes_from_form,tuple10)
        columns = [desc[0] for desc in mycursor.description]
        fuelTypes_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        fuelType_form = fuelTypes_from_form.id.to_string(index=False)
        ic(fuelType_form)
        ############################################################################################################################
        sql_fuelTypes = " select * from `transforms` where `relation_type` = 'fuelTypes' and `relation_id` = %s and `target_system` = 'autoscout' "
        tuple_fuelType_as = (fuelType_form,)
        mycursor.execute(sql_fuelTypes,tuple_fuelType_as)                                                                  
        columns = [desc[0] for desc in mycursor.description]
        fuelType = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkfuelTypesforAutoscout = fuelType.target_value.to_string(index=False)
        ic(linkfuelTypesforAutoscout)
        ############################################################################################################################
        sql_gearBoxes_from_form = " select id from `gearboxes` where `gearBoxes` = %s "
        tuple11 = (gearBoxes,)
        mycursor.execute(sql_gearBoxes_from_form,tuple11)
        columns = [desc[0] for desc in mycursor.description]
        gearBoxes_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        gearBox_form = gearBoxes_from_form.id.to_string(index=False)
        ic(gearBox_form)
        ############################################################################################################################
        sql_gearBoxes = " select * from `transforms` where `relation_type` = 'gearBoxes' and `relation_id` = %s and `target_system` = 'autoscout' "
        tuple_gearBox_as = (gearBox_form,)
        mycursor.execute(sql_gearBoxes,tuple_gearBox_as)                                                                  
        columns = [desc[0] for desc in mycursor.description]
        gearBox = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkGearBoxesforAutoscout = gearBox.target_value.to_string(index=False)
        ic(linkGearBoxesforAutoscout)
        ############################################################################################################################
        sql_doors_from_form = " select id from `doors` where `doors` = %s " 
        tuple12 = (doors,)
        mycursor.execute(sql_doors_from_form,tuple12)
        columns = [desc[0] for desc in mycursor.description]
        doors_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        door_form = doors_from_form.id.to_string(index=False)
        ic(door_form)
        ############################################################################################################################
        sql_doors = " select * from `transforms` where `relation_type` = 'doors' and `relation_id` = %s and `target_system` = 'autoscout' "
        tuple_door_as = (door_form,)
        mycursor.execute(sql_doors,tuple_door_as)                                                          
        columns = [desc[0] for desc in mycursor.description]
        door = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkdoorsforAutoscout = door.target_value.to_string(index=False)
        ic(linkdoorsforAutoscout)
        ############################################################################################################################

        autoScoutUrl = "https://www.autoscout24.com.tr/lst"
        autoScoutLastUrl = autoScoutUrl + "/" + linkBrandforAutoscout + "/" + linkModelforAutoscout + "?" + "sort=price&desc=0&ustate=N,U&atype=C&sort=price&desc=0" +  "&kmfrom=" + kilometerFrom +  "&kmto=" + kilometerTo +  "&fregfrom=" + yearFrom +  "&fregto=" + yearTo + "&fuel=" + linkfuelTypesforAutoscout + "&gear=" + linkGearBoxesforAutoscout + "&powertype=kw" + "&powerfrom=" + powerFrom + "&powerto=" + powerTo + "&body=" + linkBodyTypeforAutoscout + "&sort=price&desc=0&cy=D" + "&" + linkdoorsforAutoscout

        ic(autoScoutLastUrl)



        fireFoxOptions = Options()
        #fireFoxOptions.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        fireFoxOptions.FirefoxBinary = "/usr/bin/firefox"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        fireFoxOptions.add_argument("--headless")
        # fireFoxOptions.add_argument("--window-size=1920,1080")
        # fireFoxOptions.add_argument('--start-maximized')
        fireFoxOptions.add_argument('--disable-gpu')
        fireFoxOptions.add_argument('--no-sandbox')

        driver = webdriver.Firefox(options=fireFoxOptions)

        pricelist_autoscout = []

        # get the link
        driver.get(autoScoutLastUrl)
        #ic(autoScoutLastUrl)
        time.sleep(0)

        base_source = driver.page_source
        base_soup = BeautifulSoup(base_source, 'html.parser')


        for prices in base_soup.findAll('p', {'class': re.compile('Price_price__WZayw')}):
            pricelist_autoscout.append(prices.get_text())


        pricelist_autoscout = list(map(lambda x: x.replace('.-', ''), pricelist_autoscout))
        pricelist_autoscout = list(map(lambda x: x.replace('-', ''), pricelist_autoscout))
        pricelist_autoscout = list(map(lambda x: x.replace(',', ''), pricelist_autoscout))
        pricelist_autoscout = list(map(lambda x: x.replace('\xa0', ''), pricelist_autoscout))
        pricelist_autoscout = list(map(lambda x: x.replace('€', ''), pricelist_autoscout))
        pricelist_autoscout = list(map(lambda x: x.replace(' ', ''), pricelist_autoscout))
        pricelist_autoscout = list(map(lambda x: x.replace('.', ''), pricelist_autoscout))
        ic(pricelist_autoscout)

        driver.close()

        if pricelist_autoscout != []:
            int_pricelist_autoscout = [eval(i) for i in pricelist_autoscout]
            averageprice_autoscout = int(sum(int_pricelist_autoscout) / len(pricelist_autoscout))
            ic(averageprice_autoscout)
        else:
            averageprice_autoscout = 0
            ic(averageprice_autoscout)
        #
        #    return {'averageprice_autoscout:': averageprice_autoscout}, 200  # return data and 200 OK
        #else:
        #    return {'averageprice_autoscout:': 0}, 200

        ic("-----------------------------------------------------------------")

        r = request.json
        #ic(r) # dict

        df = pd.DataFrame.from_dict([r]) 
        ic(df) # df

        brand = df.brand.to_string(index=False)
        ic(brand)
        model = df.model.to_string(index=False)
        ic(model)
        bodyType = df.bodyType.to_string(index=False)
        ic(bodyType)
        fuelTypes = df.fuelTypes.to_string(index=False)
        ic(fuelTypes)
        gearBoxes = df.gearBoxes.to_string(index=False)
        ic(gearBoxes)
        doors = df.doors.to_string(index=False)
        ic(doors)
        kilometerFrom = df.kilometerFrom.to_string(index=False)
        ic(kilometerFrom)
        kilometerTo = df.kilometerTo.to_string(index=False)
        ic(kilometerTo)
        yearFrom = df.yearFrom.to_string(index=False)
        ic(yearFrom)
        yearTo = df.yearTo.to_string(index=False)
        ic(yearTo)
        powerFrom = df.powerFrom.to_string(index=False)
        ic(powerFrom)
        powerTo = df.powerTo.to_string(index=False)
        ic(powerTo)

        #def autouncle(self):

        sql_brand_from_form = " select id from `car_brands` where `name` = %s "
        tuple1 = (brand,)
        mycursor.execute(sql_brand_from_form,tuple1)
        columns = [desc[0] for desc in mycursor.description]
        brand_from_form  = pd.DataFrame(mycursor.fetchall(), columns=columns)
        brand_form = brand_from_form.id.to_string(index=False)
        ic(brand_form)
        ############################################################################################################################
        sql_brand = " select * from `transforms` where `relation_type` = 'brand' and `relation_id` = %s and `target_system` = 'autouncle' "
        tuple_brand_au = (brand_form,)
        mycursor.execute(sql_brand,tuple_brand_au) 
        columns = [desc[0] for desc in mycursor.description]
        brands = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkBrandforAutouncle = brands.target_value.to_string(index=False)
        ic(linkBrandforAutouncle)
        ############################################################################################################################
        sql_model_from_form = " select id from `car_brand_models` where `name` = %s " 
        tuple2 = (model,)
        mycursor.execute(sql_model_from_form,tuple2)
        columns = [desc[0] for desc in mycursor.description]
        model_from_form  = pd.DataFrame(mycursor.fetchall(), columns=columns)
        model_form = model_from_form.id.to_string(index=False)
        ic(model_form)
        ############################################################################################################################
        sql_model = " select * from `transforms` where `relation_type` = 'model' and `relation_id` = %s and `target_system` = 'autouncle' "
        tuple_model_au = (model_form,)
        mycursor.execute(sql_model,tuple_model_au) 
        columns = [desc[0] for desc in mycursor.description]
        models = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkModelforAutouncle = models.target_value.to_string(index=False)
        ic(linkModelforAutouncle)
        ############################################################################################################################
        sql_bodyType_from_form = " select id from `bodytype` where `bodyType` = %s "
        tuple3 = (bodyType,)
        mycursor.execute(sql_bodyType_from_form,tuple3)                             
        columns = [desc[0] for desc in mycursor.description]
        bodyType_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        bodyType_form = bodyType_from_form.id.to_string(index=False)
        ic(bodyType_form)
        ############################################################################################################################
        sql_bodyType = " select * from `transforms` where `relation_type` = 'bodyType'and `relation_id` = %s and `target_system` = 'autouncle' "
        tuple_bodyType_au = (bodyType_form,)
        mycursor.execute(sql_bodyType,tuple_bodyType_au)
        columns = [desc[0] for desc in mycursor.description]
        bodyTypes = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkBodyTypeforAutouncle = bodyTypes.target_value.to_string(index=False)
        ic(linkBodyTypeforAutouncle)
        ############################################################################################################################
        sql_fuelTypes_from_form = " select id from `fueltypes` where `fuelTypes` = %s "
        tuple4 = (fuelTypes,)
        mycursor.execute(sql_fuelTypes_from_form,tuple4)
        columns = [desc[0] for desc in mycursor.description]
        fuelTypes_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        fuelType_form = fuelTypes_from_form.id.to_string(index=False)
        ic(fuelType_form)
        ############################################################################################################################
        sql_fuelType = " select * from `transforms` where `relation_type` = 'fuelTypes' and `relation_id` = %s and `target_system` = 'autouncle' "
        tuple_fuelType_au = (fuelType_form,)
        mycursor.execute(sql_fuelType,tuple_fuelType_au)
        columns = [desc[0] for desc in mycursor.description]
        fuelType = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkfuelTypesforAutouncle = fuelType.target_value.to_string(index=False)
        ic(linkfuelTypesforAutouncle)
        ############################################################################################################################
        sql_gearBoxes_from_form = " select id from `gearboxes` where `gearBoxes` = %s " 
        tuple5 = (gearBoxes,)
        mycursor.execute(sql_gearBoxes_from_form,tuple5)
        columns = [desc[0] for desc in mycursor.description]
        gearBoxes_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        gearBox_form = gearBoxes_from_form.id.to_string(index=False)
        ic(gearBox_form)
        ############################################################################################################################
        sql_gearBox = " select * from `transforms` where `relation_type` = 'gearBoxes' and `relation_id` = %s and `target_system` = 'autouncle' "
        tuple_gearBox_au = (gearBox_form,)
        mycursor.execute(sql_gearBox,tuple_gearBox_au)
        columns = [desc[0] for desc in mycursor.description]
        gearBox = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkGearBoxesforAutouncle = gearBox.target_value.to_string(index=False)
        ic(linkGearBoxesforAutouncle)
        ############################################################################################################################
        sql_doors_from_form = " select id from `doors` where `doors` = %s " 
        tuple6 = (doors,)
        mycursor.execute(sql_doors_from_form,tuple6)
        columns = [desc[0] for desc in mycursor.description]
        doors_from_form = pd.DataFrame(mycursor.fetchall(), columns=columns)
        door_form = doors_from_form.id.to_string(index=False)
        ic(door_form)
        ############################################################################################################################
        sql_door = " select * from `transforms` where `relation_type` = 'doors' and `relation_id` = %s and `target_system` = 'autouncle' "
        tuple_door_au = (door_form,)
        mycursor.execute(sql_door,tuple_door_au)
        columns = [desc[0] for desc in mycursor.description]
        door = pd.DataFrame(mycursor.fetchall(), columns=columns)
        linkdoorsforAutouncle = door.target_value.to_string(index=False)
        ic(linkdoorsforAutouncle)
        ############################################################################################################################

        autoUncleLastUrl = "https://www.autouncle.de/en/cars_search/" + linkBrandforAutouncle + "/" + linkModelforAutouncle + "/f-" + linkfuelTypesforAutouncle + "/g-" + linkGearBoxesforAutouncle + "/b-" + linkBodyTypeforAutouncle + "?s[doors]=" + linkdoorsforAutouncle + "&s[max_km]=" + kilometerTo + "&s[min_km]=" + kilometerFrom + "&s[max_year]=" + yearTo + "&s[min_year]=" + yearFrom + "&s[min_hp]=" + powerFrom + "&s[max_hp]=" + powerTo + "&s[order_by]=cars.price+ASC" 
        ic(autoUncleLastUrl)


        fireFoxOptions = Options()
        #fireFoxOptions.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        fireFoxOptions.FirefoxBinary = "/usr/bin/firefox"  # r'C:\Program Files\Firefox Developer Edition\firefox.exe' # PC"ye Firefox Developer yüklenmelidir.
        fireFoxOptions.add_argument("--headless")
        # fireFoxOptions.add_argument("--window-size=1920,1080")
        # fireFoxOptions.add_argument('--start-maximized')
        fireFoxOptions.add_argument('--disable-gpu')
        fireFoxOptions.add_argument('--no-sandbox')

        driver = webdriver.Firefox(options=fireFoxOptions)

        pricelist_autouncle = []

        # get the link
        driver.get(autoUncleLastUrl)
        #ic(autoUncleLastUrl) 
        time.sleep(1)    #BAK

        base_source = driver.page_source
        base_soup = BeautifulSoup(base_source, 'html.parser')

        for prices in base_soup.findAll('div', {'class': re.compile('listing-item-price')}):
            #ic(prices)
            #prices.split('-')[0]
            #ic(prices)
            price_with_hyphen = prices.get_text()
            #ic(price_with_hyphen)
            price_without_hyphen = price_with_hyphen.split('-')[0]
            #ic(price_without_hyphen)
            price_without_hyphen_and_new = price_without_hyphen.split('New')[0]
            #ic(price_without_hyphen_and_new)
            price_without_hyphen_and_new_and_percentage = price_without_hyphen_and_new.split('0%')[0]
            pricelist_autouncle.append(price_without_hyphen_and_new_and_percentage)#[0:11])
            #ic(pricelist)

            pricelist_autouncle = list(map(lambda x: x.replace(',', ''), pricelist_autouncle))
            #pricelist_autouncle = list(map(lambda x: x.replace('-', ''), pricelist_autouncle))
            #pricelist_autouncle = list(map(lambda x: x.replace('%', ''), pricelist_autouncle))
            pricelist_autouncle = list(map(lambda x: x.replace('\xa0', ''), pricelist_autouncle))
            pricelist_autouncle = list(map(lambda x: x.replace('€', ''), pricelist_autouncle))
            pricelist_autouncle = list(map(lambda x: x.replace('\n', ''), pricelist_autouncle))
            pricelist_autouncle = list(map(lambda x: x.replace(' ', ''), pricelist_autouncle))

        ic(pricelist_autouncle)
        #print(pricelist_autouncle)

        driver.close()   #BAK

        if pricelist_autouncle != []:
            int_pricelist_autouncle = [eval(i) for i in pricelist_autouncle]
            averageprice_autouncle = int(sum(int_pricelist_autouncle) / len(pricelist_autouncle))
            ic(averageprice_autouncle)
        else:
            averageprice_autouncle = 0
            ic(averageprice_autouncle)
        #
        #    return {'averageprice_autouncle:': averageprice_autouncle}, 200  # return data and 200 OK
        #else:
        #    return {'averageprice_autouncle:': 0}, 200

        if averageprice_mobile != 0 or averageprice_autoscout != 0 or averageprice_autouncle != 0 :
                #final_averageprices = [averageprice_mobile,averageprice_autoscout,averageprice_autouncle]
                #ic(final_averageprices)
                return {
                    #'averageprice:': int(sum(final_averageprices) / len(final_averageprices))
                    #'final_averageprices:' : final_averageprices
                    "averageprice_mobile"    : averageprice_mobile,
                    "mobileDeLastUrl"        : mobileDeLastUrl,
                    "averageprice_autoscout" : averageprice_autoscout,
                    "autoScoutLastUrl"       : autoScoutLastUrl,
                    "averageprice_autouncle" : averageprice_autouncle,
                    "autoUncleLastUrl"       : autoUncleLastUrl
                       }, 200  # return data and 200 OK
        else:
            return {'averageprice:': 0}, 200



api.add_resource(Users, '/api')  # add endpoints

if __name__ == '__main__':
    app.run(host='65.108.125.124')  # run our Flask app
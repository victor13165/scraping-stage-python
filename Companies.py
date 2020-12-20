# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:55:50 2020

@author: Victor

Ajouter les classes de chaque boite ici
"""
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import datetime
import requests
import bs4

class Safran():
    
    def __init__(self):
        self.url = "https://www.safran-group.com/fr/emplois?contrat=Stage&profession=M%C3%A9canique%20des%20fluides";
        self.name = "Safran";
        self.parsing_mode = "date";
        self.scrapping_mode = "bs";
    
    #Requête et récupère les annonces
    def bs_procedure(self):
        try:
            response = requests.get(self.url); #Requête à l'url
            print(self.name + " url request status : success");
            soup = bs4.BeautifulSoup(response.text, 'html.parser'); #Object beautifulsoup
            return soup.find_all("a",{"class":"offer-card"})
            print(self.name + ": database set");
        except:
            print(self.name + " url request status : fail");
    
    #Cherche la date à partir d'une annonce
    def get_date(self,annonce):
        date = annonce.find_all("span",{"class":"date"})[0].getText()[10:];
        return datetime.datetime.strptime(date, '%d/%m/%Y').date();
    
    #Cherche le titre à partir d'une annonce
    def get_titre(self,annonce):
        return annonce.find_all("div",{"class":"title"})[0].getText()
    
    #Cherche l'url à partir de l'annonce
    def get_url(self,annonce):
        return annonce['href'];
    
    def get_annonces(self):
        self.init_annonces();
        return self.annonces;

class Volvo():
    
    def __init__(self):
        self.url = "https://xjobs.brassring.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=25079&siteid=5171&PageType=searchResults&SearchType=linkquery&LinkID=3078496&codes=Volvo#keyWordSearch=&Country=France_or_Sweden&Functional%20Area=Manufacturing%20Engineering_or_Technology";
        self.name = "Volvo";
        self.parsing_mode = "title";
        self.scrapping_mode = "selenium";

    def get_date(self,annonce):
        return datetime.datetime.now().date();
    
    def get_titre(self,annonce):
        return annonce.find_element_by_xpath('.//a').text;
    
    def get_url(self,annonce):
        return annonce.find_element_by_xpath('.//a').get_property('href');
    
    def close_driver(self):
        self.driver.quit();
    
    def selenium_procedure(self,driver):
        self.driver = driver;
        driver.get(self.url);
        
        country = driver.find_element_by_xpath("//h3[@aria-label='Filter search results by Country']/..");
        area = driver.find_element_by_xpath("//h3[@aria-label='Filter search results by Functional Area']/..");
        country.click();
        area.click();
        tab = driver.find_elements_by_xpath("//fieldset[@class='ng-scope']");
        tab[4].find_elements_by_tag_name('input')[5].click()
        print('France : clicked');
        time.sleep(0.5)
        tab[4].find_elements_by_tag_name('input')[9].click();
        print('Sweden : clicked');
        time.sleep(0.5)
        tab[6].find_elements_by_tag_name('input')[12].click();
        #Attendre que le boutton soit clickable et cliquer dessus : Technology
        print('Option 1 : clicked');
        time.sleep(0.5)
        tab[6].find_elements_by_tag_name('input')[19].click();
        #Attendre que le boutton soit clickable et cliquer dessus : Engineering
        print('Option 2 : clicked');  
        print('Sleeping for 3 seconds');
        time.sleep(3);
        annonces = driver.find_elements_by_xpath("//li[@class='job baseColorPalette ng-scope']");
        
        return annonces;

class ESA():
    
    def __init__(self):
        self.url = "https://career2.successfactors.eu/portalcareer?company=esa&career%5fns=job%5flisting%5fsummary&navBarLevel=JOB%5fSEARCH&_s.crb=d2ZjhqsMzH6LNA3No2KcL5hM3vGvNQF5YMZ6sMteBtU%3d";
        self.name = "ESA";
        self.parsing_mode = "date";
        self.scrapping_mode = "selenium";
    
    #Requête et récupère les annonces
    def selenium_procedure(self,driver):
        
        self.driver = driver;
        
        driver.get(self.url);           
        time.sleep(2);
        span = driver.find_element_by_xpath("//input[@id='57:']");
        span.send_keys('Mechanical engineering');
        time.sleep(1)
        driver.find_element_by_xpath("//button[@id='dlgButton_69:']").click();
        time.sleep(1)
        driver.find_element_by_xpath("//select[@id='41:']/option[text()='25']").click()
        time.sleep(1);        
        annonces = driver.find_elements_by_xpath("//tr[@class='jobResultItem']");
        
        return annonces;
    
    #Cherche la date à partir d'une annonce
    def get_date(self,annonce):
        date = annonce.find_elements_by_xpath(".//span[@class='jobContentEM']")[-1].text[10:];
        return datetime.datetime.strptime(date, '%d/%m/%Y').date();
    
    #Cherche le titre à partir d'une annonce
    def get_titre(self,annonce):
        return annonce.find_element_by_xpath(".//a").text
    
    #Cherche l'url à partir de l'annonce
    def get_url(self,annonce):
        return annonce.find_element_by_xpath(".//a").get_attribute('href')
    
    def close_driver(self):
        self.driver.quit();
       
# class Ariane():
    
#     def __init__(self):
#         self.url = "https://arianegroup.wd3.myworkdayjobs.com/EXTERNALALL/1/refreshFacet/318c8bb6f553100021d223d9780d30be";
#         self.name = "Ariane";
#         self.parsing_mode = "title";
#         self.scrapping_mode = "selenium";

#     def get_date(self,annonce):
#         return datetime.datetime.now().date();
    
#     def get_titre(self,annonce):
#         return annonce.text
    
#     def get_url(self,annonce):
#         action = ActionChains(self.driver);
#         annonce.location_once_scrolled_into_view;
#         time.sleep(1);
#         action.context_click(annonce).perform();
#         context = self.driver.find_element_by_xpath("//div[@data-uxi-element-id='popupInfo']");
#         tr = context.find_elements_by_tag_name('tr');
#         return tr[1].find_elements_by_tag_name('div')[0].get_attribute('data-clipboard-text')
    
#     def close_driver(self):
#         self.driver.quit();
    
#     def selenium_procedure(self,driver):
#         self.driver = driver;
           
#         driver.get(self.url);
#         time.sleep(3);
        
#           #Clicker sur Engineering
        
#         div_tot = driver.find_element_by_xpath('//div[@id="wd-Facet-jobFamilyGroup-wd-FieldSet"]');
#         WebDriverWait(div_tot, 1000000).until(EC.element_to_be_clickable((By.XPATH,
#                                             ".//div[@class='WJIF']"))).click();
#         print('Engineering : clicked');  
#         time.sleep(2);
#         div_tot = driver.find_element_by_xpath('//div[@id="wd-Facet-workerSubType-wd-FieldSet"]');
#         WebDriverWait(div_tot, 1000000).until(EC.element_to_be_clickable((By.XPATH,
#                                             ".//div[@class='WJIF']"))).click();
#         print('Stage : clicked'); 
#         time.sleep(2);
#         annonces = driver.find_elements_by_tag_name('ul')[6].find_elements_by_tag_name('li')[1::2];
#         return annonces;

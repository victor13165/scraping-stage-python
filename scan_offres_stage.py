# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:14:00 2020

@author: Victor
"""
import inspect
from parsing_lib import parse_and_print
import Companies as c
import datetime
import WSInternship as w

def get_classes(module):
    return [m[1] for m in inspect.getmembers(c, inspect.isclass) if m[1].__module__ == c.__name__];

def init_companies(module):
    classes = get_classes(module);
    companies = [];
    for clas in classes:
        companies.append(clas());
    return companies;


rep = input("Voulez-vous lancer l'outil de webscraping? (O/n) : ")

if (rep == 'O'):
    print("Lancement de l'outil webscraping");
    filename = 'nouvelles_offres.xlsx';
    companies = init_companies(c);
    
    log_file = open("new_internships_log.txt","w");
    log_file.write(datetime.datetime.now().strftime('%Y/%m/%d %H:%M')+'\n');
    
    for company in companies:
        ws = w.WSInternship(company);
        data = parse_and_print(filename,company,ws);
        log_file.write(company.name + ": " + str(len(data)) + " nouvelles offres"+'\n');
    
    log_file.close();
else:
    print("Terminé")
@echo off
cls

cd C:\Users\user\Documents\scraping_stage_python

start /wait C:\Users\user\anaconda3\python.exe C:\Users\user\Documents\scraping_stage_python\scan_offres_stage.py

start %windir%\system32\notepad.exe C:\Users\user\Documents\scraping_stage_python\new_internships_log.txt

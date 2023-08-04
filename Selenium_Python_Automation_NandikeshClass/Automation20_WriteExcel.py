import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#install openPyExcel  --->> File -- settings --- python inperpreter  ----- install openPyExcel package
#Writing data into Excel
path = "D:\data2.xlsx"
#load the workbook
workbook=openpyxl.load_workbook(path)

#Fetch sheetName from workbook
sheet=workbook.get_sheet_by_name("Sheet1")
#sheet=workbook.active

for r in range(1,6):       #for loop for rows iteration - 1 is for first row
    for c in range(1,4):    #for loop for coloumns
        sheet.cell(row=r,column=c).value="welcome to selenium world"
workbook.save(path)
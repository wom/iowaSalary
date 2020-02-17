from selenium import webdriver
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
url = "https://www.legis.iowa.gov/publications/fiscal/salaryBook"
response = requests.get(url)
driver.get(url)

# After getting select to work, then use loop to generate other combinations

# select year
yrselect = Select(driver.find_element_by_id('fiscalYearSelect'))

select.select_by_index(1)

# select department
yrselect = Select(driver.find_element_by_name('aid'))
select.select_by_index(4)


soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("table",{"class":"standard sortable"})

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

  # for year in range(1993,2004)
  #		select('year')
  #    for dept in depts
  #    	select('dept')



# driver = webdriver.Chrome("C:/Python27/Scripts/chromedriver_win32/chromedriver.exe")

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# import os;
# os.environ["PATH"] += os.pathsep + r'C:\Python27\Scripts\chromedriver_win32';

# from selenium import webdriver;
# browser = webdriver.Chrome();
# browser.get('http://localhost:8000')
# assert 'Django' in browser.title
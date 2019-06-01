#Download url from the website "https://www.donorschoose.org"
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import datetime
import shutil
import os

chromeoptions = Options()
#driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)
#chromeoptions.add_argument('headless')
try:
	driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)

except:
	pass
base_url="https://www.donorschoose.org/donors/search.html?page="
page_counter=1

list_m = []
while(True):
    try:
        now = datetime.datetime.now()
        current_date = now.strftime("%Y%m%d")
        driver.get(base_url+str(page_counter))
        time.sleep(10)
        #all_urls = driver.find_elements_by_xpath("//div[@class='search-results']")
        #div_m=driver.find_elements_by_xpath("//div[@data-reactid='218']")
        all_urls1 = driver.find_elements_by_xpath("//a[@class='project-card']")
        all_urls2 = driver.find_elements_by_xpath("//a[@class='project-card match-dyi with-match']")
        for a in all_urls1:
            # print(a.get_attribute('href'))
            list_m.append(a.get_attribute('href'))
            #b=pd.DataFrame(b)
        for a in all_urls2:
            # print(a.get_attribute('href'))
            list_m.append(a.get_attribute('href'))
            #b=pd.DataFrame(b)

            #list.to_csv(csvFile,sep=',')
        print('total urls '+str(len(all_urls1) + len(all_urls2))+'page '+str(page_counter))
        page_counter+=1
        if (page_counter>3):
            break
    except:
         print('')


#image_path='D:\\USF\\Selenium\\'				#path of the folder
csvFile=os.path.join(current_date + '.csv')			#file being name with today's date
#os.makedirs(csvFile)				#folder getting created with name destionation hence can be ignored

#csvFile = "ReferenceLinks.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list_m:
        writer.writerow([val])
from selenium import webdriver
import os.path
import time

Collect()
selection = input("(1) Every Day  \n (2) Every Two Days (3) Every Week ")
if selection[0] == '1':
    while True:
        time.sleep(3600)
        Collect()
elif selection[0]== '2':
     while True:
        time.sleep(7200)
        Collect()
elif selection[0] == '3':
    while True:
        time.sleep(604800)
        Collect()
def Collect():
    if(os.path.exists('XPaths.txt') and os.path.exists('Websites.txt')):
        xpaths_f = open("XPaths.txt","r")
        Websites_f = open("Websites.txt","r")
        urls = []
        temp = []
        xpaths_per_site =[]
        for line in Websites_f:
            urls.append(line)

        for line in xpaths_f:
            temp.append(line)
        for text in temp:
            xpaths_per_site.append(text.split("|"))
        browser = webdriver.Chrome(r'C:\Users\ZackO\source\repos\WebScraper\chromedriver\chromedriver.exe')
        del temp[:]
        temp = []
        Data = [] 
        for url in urls:
            browser.get(url)
        for XList in xpaths_per_website:
            for xpath in XList:
              temp.append(browser.find_element_by_xpath(xpath).text.strip())
            Data.append(temp)
        if os.path.exists('Data.txt'):
           Data_f = open("Data.txt","a")
           Data_f.write(Data)
        else:
            Data_f = open("Data.txt","w")
       

    else:
        print("NO DATA FOUND")






    xpaths_f.close()
    Websites_f.close()
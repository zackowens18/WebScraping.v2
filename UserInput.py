from selenium import webdriver
import os.path


urls = []
xpaths_per_website = []

while True:
    url = input("Paste in URLs of webiste to get data from:")
    urls.append(url)
    keepgoing = input("Keep going? Y/N")
    if keepgoing[0] == 'N' or keepgoing[0]=='n':
        break
   
for url in urls:    
    xpath = []
    while True:
        xpath.append(input("Enter XPath"))
        keepgoing = input("Keep going? Y/N")
        if keepgoing[0] == 'N' or keepgoing[0]=='n':
            xpaths_per_website.append(xpath)
            del xpath[:]
            break

browser = webdriver.Chrome(r'C:\Users\ZackO\source\repos\WebScraper\chromedriver\chromedriver.exe')
for url in urls:
    browser.get(url)
    for XList in xpaths_per_website:
        for xpath in XList:
            browser.find_element_by_xpath(xpath).text.strip()

if(os.path.exists('Websites.txt')):
    Websites_f = open("Websites.txt","a")
else:
    Websites_f = open("Websites.txt","w")

for url in urls:
    Websites_f.write(url+"\n")

if(os.path.exists('XPaths.txt')):
    xpaths_f = open("XPaths.txt","a")
else:
    xpaths_f = open("XPaths.txt","w")

for xpaths in xpaths_per_website:
    for xpath in xpaths:
        xpaths_f.write(xpath+"|")
    xpaths_f.write("\n")

print("Data stored")
xpaths_f.close()
Websites_f.close
browser.quit()
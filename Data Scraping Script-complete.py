
# coding: utf-8

# In[52]:

# import libraries
import urllib
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


# In[53]:

## open the website of dx_label: Acne Vulgaris
## since there is an issue to soup the website url directly, I use a webdriver to simulate the browser
## for simplicity I don't use loop, but for large number of labels, can use a loop for the following steps
# use webdriver to open the website

driver = webdriver.Chrome(executable_path="/Users/shao/Desktop/Tools/chromedriver")
driver.get("https://www.dermquest.com/image-library/image-search")

# close cookie window
cookie = driver.find_element_by_xpath("//*[@id='cookiesDirectiveBox']/div/div[3]/a")
cookie.click()

# select "diagnosis"
diagnosis = driver.find_element_by_xpath("//*[@id='filter-selection']/div[1]/div[1]/ul/li[5]/a")
diagnosis.click()

# select "alphabet": A
alphabet = driver.find_element_by_xpath("//*[@id='diagnosis']/div/div[2]/div/div[1]/ul/li[1]/a")
alphabet.click()

# choose the diagnosis label as Acne Vulgaris
label = driver.find_element_by_xpath("//*[@id='alpha-A']/div/ul/li[7]/label")
label.click()

view = driver.find_element_by_xpath("//*[@id='diagnosis']/div/div[2]/div/div[2]/a")
view.click()

time.sleep(3)

itemsPerPage = driver.find_element_by_xpath("//*[@id='image-results']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li[4]/a")
itemsPerPage.click()

time.sleep(1)

# soup the webpage
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")


# In[56]:

# extract the case id
case_id = []

for p in soup.find_all("p", {"class": "asset-name"}):
    for a in p.find_all("a"):
        href = a["href"]
        case_id.append(href)
        #print(href)
        

# creat the list of case urls
case_url = []

for i in range(len(case_id)):
    url = "https://www.dermquest.com/" + case_id[i]
    case_url.append(url)
    #print(url)
    

# choose first 100 url
case_url_100 = case_url[:100]
len(case_url_100)


print(len(case_id))
print(len(case_url))
print(len(case_url_100))


# In[57]:

# extract the image url, dx label and lesion label from each image page
image_url = []
dx_label = []
lesion_label = []

for url in case_url_100:
    image_id = url[-24:]
    # print(url)
    #print(image_id)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    # print(soup.prettify())
    
    # extract image url
    for li in soup.find_all("li", {"data-image-id": image_id}):
        for a in li.find_all("a", {"class": "preview-image"}):
            # print(a)
            href = a["href"]
            url = "https://www.dermquest.com" + href
            image_url.append(url)
            print(url)
            
    # extract dx label   
    for div in soup.find_all("div", {"id": "image_" + image_id}):
        table = div.find_all("table")[2]
    # print(table)
    
        td = table.find_all("td")
        dx = td[1].text.strip()
        dx_label.append(dx)
        #print(dx)
        
    
    # extract lesion label
    for div in soup.find_all("div", {"id": "image_" + image_id}):
        ul = div.find_all("ul")
        lesions = ul[0]
    
        li = lesions.find_all("li")
        
        lesion = li[0].text.strip()
        for i in range(1, len(li)):
            lesion = lesion + ", " + li[i].text.strip()
            
        lesion_label.append(lesion)
             
print(image_url)
print(dx_label)
print(lesion_label)


# In[71]:

# create fisrt data sheet
d1 = {'image url': image_url, 'dx_label': dx_label, 'lesion_label': lesion_label}
df1 = pd.DataFrame(data=d1,  columns={'image url', 'dx_label', 'lesion_label'})
print(df1.shape)


# In[61]:

## open the website of dx_label: Dermatofibroma
# use webdriver to open the website
driver = webdriver.Chrome(executable_path="/Users/shao/Desktop/Tools/chromedriver")
driver.get("https://www.dermquest.com/image-library/image-search")

# close cookie window
cookie = driver.find_element_by_xpath("//*[@id='cookiesDirectiveBox']/div/div[3]/a")
cookie.click()

# select "diagnosis"
diagnosis = driver.find_element_by_xpath("//*[@id='filter-selection']/div[1]/div[1]/ul/li[5]/a")
diagnosis.click()

# select "alphabet": D
alphabet = driver.find_element_by_xpath("//*[@id='diagnosis']/div/div[2]/div/div[1]/ul/li[4]/a")
alphabet.click()

# choose the diagnosis label as Dermatofibroma
label = driver.find_element_by_xpath("//*[@id='alpha-D']/div/ul/li[5]/label")
label.click()

view = driver.find_element_by_xpath("//*[@id='diagnosis']/div/div[2]/div/div[2]/a")
view.click()

time.sleep(3)

itemsPerPage = driver.find_element_by_xpath("//*[@id='image-results']/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li[4]/a")
itemsPerPage.click()

time.sleep(1)

# soup the webpage
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")


# In[62]:

# extract the case id
case_id = []

for p in soup.find_all("p", {"class": "asset-name"}):
    for a in p.find_all("a"):
        href = a["href"]
        case_id.append(href)
        # print(href)

print(len(case_id))
    

# creat the list of case urls
case_url = []

for i in range(len(case_id)):
    url = "https://www.dermquest.com/" + case_id[i]
    case_url.append(url)
    # print(url)

print(len(case_url))



# choose first 100 url
case_url_100 = case_url[:100]
print(len(case_url_100))


# In[63]:

# extract the image url, dx label and lesion label from each image page
image_url = []
dx_label = []
lesion_label = []

for url in case_url_100:
    image_id = url[-24:]
    # print(url)
    #print(image_id)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    # print(soup.prettify())
    
    # extract image url
    for li in soup.find_all("li", {"data-image-id": image_id}):
        for a in li.find_all("a", {"class": "preview-image"}):
            # print(a)
            href = a["href"]
            url = "https://www.dermquest.com" + href
            image_url.append(url)
            print(url)
            
    # extract dx label   
    for div in soup.find_all("div", {"id": "image_" + image_id}):
        table = div.find_all("table")[2]
    # print(table)
    
        td = table.find_all("td")
        dx = td[1].text.strip()
        dx_label.append(dx)
        #print(dx)
        
    
    # extract lesion label
    for div in soup.find_all("div", {"id": "image_" + image_id}):
        ul = div.find_all("ul")
        lesions = ul[0]
    
        li = lesions.find_all("li")
        
        lesion = li[0].text.strip()
        for i in range(1, len(li)):
            lesion = lesion + ", " + li[i].text.strip()
            
        lesion_label.append(lesion)
        
        
print(image_url)
print(dx_label)
print(lesion_label)


# In[77]:

# create second data sheet, merge two sheets into one and export to csv file
d2 = {'image url': image_url, 'dx_label': dx_label, 'lesion_label': lesion_label}
df2 = pd.DataFrame(data=d2,  columns={'image url', 'dx_label', 'lesion_label'})
print(df2.shape)
df = [df1, df2]
sheet = pd.concat(df)
sheet = sheet[['image url', 'dx_label', 'lesion_label']]
print(sheet.shape)
sheet.to_csv('sheet_complete.csv', index=False)


# In[ ]:




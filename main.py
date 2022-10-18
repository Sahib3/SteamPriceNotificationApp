import requests 
import re
from bs4 import BeautifulSoup



#url = 'https://store.steampowered.com/app/1490890/Demon_Slayer_Kimetsu_no_Yaiba_The_Hinokami_Chronicles/'
#url =  'https://store.steampowered.com/app/1332010/Stray/'

urls = ['https://store.steampowered.com/app/1490890/Demon_Slayer_Kimetsu_no_Yaiba_The_Hinokami_Chronicles/','https://store.steampowered.com/app/1332010/Stray/',
     ]



headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en"}


# scrape data from steam
def scrape():
    for url in urls:
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.content,"html.parser")
        
        title = soup.find(id="appHubAppName").get_text()
        print(title)
        #return price from string, get rid of all whitespaces, splice string to inculde only the dollar value
        #use try/except to differnate titles that are on sale and not on sale, as steam changes the html for the price based on the fact that they're is a sale
        try:
            org_priceText = soup.find(class_="game_purchase_price price").get_text().replace(' ','')
            org_priceText = ''.join(org_priceText.split())
            org_price = float(org_priceText[4:])
            print(org_price) 
        except:    
            sale_priceText = soup.find(class_="discount_final_price").get_text()
            sale_price = float(sale_priceText[5:])
            print(sale_price)
     
    
    


        
   


scrape()
     








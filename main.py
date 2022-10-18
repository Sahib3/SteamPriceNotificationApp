import requests 
from bs4 import BeautifulSoup
from other import password
import smtplib,ssl

price = 0.00
email_pass = password

urls = ['https://store.steampowered.com/app/1490890/Demon_Slayer_Kimetsu_no_Yaiba_The_Hinokami_Chronicles/',
'https://store.steampowered.com/app/1091500/Cyberpunk_2077/'    
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
            sale_priceText = soup.find(class_="discount_final_price").get_text()
            sale_price = float(sale_priceText[5:])
            #send_email(title,sale_price)
            print(sale_price)
        except:    
            org_priceText = soup.find(class_="game_purchase_price price").get_text().replace(' ','')
            org_priceText = ''.join(org_priceText.split())
            org_price = float(org_priceText[4:])
            print(org_price) 
           
        
#send email if there is a sale    
def send_email(title,sale_price):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "pproj1238@gmail.com"
    password = email_pass

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        message = f'{title} is on sale for {sale_price}'
        server.sendmail(sender_email, sender_email,message)
    except Exception as e:
        print(e)
    finally:
        server.quit()     


        
   


scrape()
     








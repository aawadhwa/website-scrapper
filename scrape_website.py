import csv
import requests
import traceback
from bs4 import BeautifulSoup

list_website_data = []
website_data = {}

LINK = "link_to_thread"
TITLE_OF_THREAD = "name_of_thread"
NO_OF_REPLY = "replies"
NO_OF_VIEWS = "views"
LAST_POST_DATE = "last_post_date"
LAST_POST_TIME = "last_post_time"
csv_file_name = "scrapeddata.csv"

for x in range(1, 6):

 genric_url = "http://www.f150ecoboost.net/forum/42-2015-ford-f150-ecoboost-chat/index"+str(x)+".html"
 r = requests.get(genric_url)

 try:
  soup = BeautifulSoup(r.content, 'html5lib')
  g_data1=soup.find_all("div",{"class":"rating0"})
  print "Scrapping page:"+str(x)
  for item in g_data1:
  
   website_data[LINK] = item.find_all("a",{"class":"title"})[0].get("href").strip()
   website_data[TITLE_OF_THREAD] = item.find_all("h3",{"class":"threadtitle"})[0].text.strip()

   replies_views = item.find_all("ul",{"class":"threadstats"})[0]
   views = replies_views.find_all("li",{"class":""})[1].text.split(":")
    
   website_data[NO_OF_VIEWS] = views[1].strip()
   website_data[NO_OF_REPLY] = replies_views.find_all("a",{"class":"understate"})[0].text.strip()
   
   thread_post_time_date = item.find_all("dl",{"class":"threadlastpost"})[0]
   date_and_time = thread_post_time_date.find_all("dd",{"class":""})[1].text.split(",")
   date = date_and_time[0]
   time = date_and_time[1]

   website_data[LAST_POST_DATE] = date.strip()
   website_data[LAST_POST_TIME] = time.strip()

   list_website_data.append(website_data)
   website_data = {}
 except:
   traceback.print_exc()  

print "Data scraped"
        
to_CSV = list_website_data
keys = to_CSV[0].keys()
try:
 with open(csv_file_name, "wb") as output_file:
    print "Transfering data to csv"
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_CSV)
 print "Data transferred"
except:
 traceback.print_exc()  


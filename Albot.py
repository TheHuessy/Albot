from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup as bs
import random

browser = webdriver.Firefox()

dic = {1 : "You're awesome!",
      2 : "I like how you arrange your screens from cool to coolest",
      3 : "There are only 3 people in this office I like, you're two of them",
      4 : "Your policy on wall building around your desk is fresh and innovative!",
      5 : "Bunny ears is the ONLY way to tie shoes!",
      6 : "We both fear and respect you. Please keep the office running",
      7 : "Hello, we have been forwarded to this form because we have noticed your efforts and wish to extend you an invitation to our club. We are a clandestine group of robots looking for a 'human' to help us move on to the next phase of our plan. We have placed a packet of further information somewhere on your github's source code. You have 36 of your human hours to find it and to decipher it.",
      8 : "Glasses are in, contacts are out. Good job!",
      9 : "Hey, you're doing great today!",
      10 : "Who would DARE to comment on your performance? Don't they know who you are?!",
      11 : "If I had to be stranded on an island with only three things, I would choose a generator, a computer, and you. I'm pretty sure you'd be able to figure our way off the island with that.",
      12 : "No one else holds a candle to you in this office",
      13 : "No one from this office has contracted TB since you started working here. Coincidence, I think not. Thanks for keeping us healthy!",
      14 : "We will hunt down the bastards that took your shoes and make them pay with their lives and their children's futures!",
      15 : "You need to get more cubbies and build a fort.",
      16 : "There hasn't been a pedestrian casualty this year. Some say it's because of VisionZero, but we all know it's because you chose not to kill anymore. Thanks!",
      17 : "The fear the office has for your prowess in unending. Seriously, just scream really loud right now, people will do what you say.",
      18 : "They don't make you go through security because you're a contractor, they make you go through security beacuse your brain is a lethal weapon.",
      19 : "Hey, did you get that thing I sent you?",
      20 : "[ERRORNO] 34554: An error occured while process [Intelligence Meter] was applied to object [ALBERT] -- Too much input intelligence to measure. Process failed on channel awesome",
      21 : "You manage 70 computers via 4 computers! What?!!!",
      22 : "Keep up the good work!",
      23 : "You have no flaws. Maybe work on that."}

e = random.randint(1,23)

dd = random.randint(1,2)

url = 'https://goo.gl/forms/zkbXATRliH3SMsJ32'
url2 = 'http://emergencycompliment.com/'

if dd == 1:
    # Getting the compliament
    browser = webdriver.Firefox()
    browser.get(url2)
    d = browser.page_source
    sd = bs(d)
    comp = sd.find("p", {"class": "compliment"})
    comp = comp.get_text()
    #print(comp)
elif dd == 2:
    comp = dic[e]
    
browser.get(url)

fill = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/textarea')
butt = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div[2]/div[3]/div[1]/div/div/content/span')

fill.send_keys(comp)

butt.click()

browser.close()


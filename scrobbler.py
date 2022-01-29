from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time
from os.path import exists

PATH = "chromedriver" #add path to  your chromedriver
driver = webdriver.Chrome(PATH)

driver.get("https://openscrobbler.com/")
#time.sleep(10)


def readFile():
    with open("Apple Music Library Tracks.json") as musicFile: #path to your Apple Music Library Tracks json
        data = musicFile.read()
    arrayOfMusicData = json.loads(data)
    print(arrayOfMusicData)
    arrayOfMusic = {}
    for i in arrayOfMusicData:
        if ("Eminem" in str(i["Artist"])) :
            title = i["Title"]
            arrayOfMusic[title] = {}
            arrayOfMusic[title]["Artist"] = i["Artist"]
            arrayOfMusic[title]["Album"] = i["Album"]
            arrayOfMusic[title]["Album Artist"] = i["Album Artist"]
            arrayOfMusic[title]["Track Play Count"] = i["Track Play Count"]
    return(arrayOfMusic)

def readTestFile():
    with open("test.json") as musicFile: #add the path to the folder you cloned this in and then add test.json
        data = musicFile.read()
    arrayOfMusicData = json.loads(data)
    #print(arrayOfMusicData)
    arrayOfMusic = {}
    for i in arrayOfMusicData:
        title = str(i)
        try:
            print(arrayOfMusicData[str(i)]["Album Artist"])
            arrayOfMusic[title] = {}
            arrayOfMusic[title]["Artist"] = arrayOfMusicData[str(i)]["Artist"]
            arrayOfMusic[title]["Album"] = arrayOfMusicData[str(i)]["Album"]
            arrayOfMusic[title]["Album Artist"] = arrayOfMusicData[str(i)]["Album Artist"]
            arrayOfMusic[title]["Track Play Count"] = arrayOfMusicData[str(i)]["Track Play Count"]
    return(arrayOfMusic)

if exists("/home/garv/programming/scrobbler/test.json"):
    musicDict = readTestFile()
else:
    musicDict = readFile()
print(musicDict)
removedMusic = []


try:
    loginButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div/main/div[1]/div[1]/div/p[3]/button")))
    loginButton.click()
    time.sleep(1)
    username = driver.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div[5]/div[2]/div/div/form/div[1]/div/input')
    username.send_keys("") #username or email
    passwordBox = driver.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div[5]/div[2]/div/div/form/div[2]/div/input')
    passwordBox.send_keys("") #password for lastfm
    passwordBox.send_keys(Keys.RETURN)
    driver.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div[5]/div[3]/div/div/section/form/div/div/button').click()
    try:
        scrobbleManually = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Scrobble manually")))
        scrobbleManually.click()
        for songGroup in musicDict:
            i = 0
            #print(songGroup)
            #time.sleep(10)
            lim = int(musicDict[songGroup]["Track Play Count"])
            while (i < lim):
                print(lim)
                driver.find_element_by_xpath(
                        '/html/body/div/div/main/div/div[1]/form/div[1]/div[1]/input').send_keys(musicDict[songGroup]["Artist"])
                driver.find_element_by_xpath(
                        '/html/body/div/div/main/div/div[1]/form/div[2]/input').send_keys(songGroup)
                driver.find_element_by_xpath(
                        '/html/body/div/div/main/div/div[1]/form/div[3]/div/input').send_keys(musicDict[songGroup]["Album"])
                driver.find_element_by_xpath(
                        '/html/body/div/div/main/div/div[1]/form/div[4]/div/input').send_keys(musicDict[songGroup]["Album Artist"])
                driver.find_element_by_xpath(
                        '/html/body/div/div/main/div/div[1]/form/button').click()
                time.sleep(1)
                i += 1
                print(i)
            print("here")
            removedMusic.append(songGroup)
        try:
            for removedSong in removedMusic:
                musicDict.pop(removedSong)
            print(musicDict)
        except:
            print("error here")

        with open("test.json", "w") as output:
            #print(musicDict)
            json.dump(musicDict, output, indent=3)
        driver.quit()
    except:
        print("failure on scrobble manually")
        musicDict[songGroup]["Track Play Count"] = int(musicDict[songGroup]["Track Play Count"]) - i
        try:
            for removedSong in removedMusic:
                musicDict.pop(removedSong)
        except:
            print("failed in exception to add")
        with open("test.json", "w") as output:
            #print(musicDict)
            json.dump(musicDict, output, indent=3)
        driver.quit()
    time.sleep(10)
except:
    print("failed")
    time.sleep(50)
    time.sleep(50)

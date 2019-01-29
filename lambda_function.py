import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from time import sleep
from flask import Flask
from flask_ask import Ask, statement, question

def lambda_handler(event, context):

    app = Flask(__name__)
    ask = Ask(app, "/")

    #TODO: delete if possible
    @app.route('/')
    def homepage():
        return "KEXP Now Playing App"

    @ask.launch
    def start_skill():
        #welcome_message = "Hi! I can tell you the song that's currently playing on K-E-X-P or I can tell you the last few songs played"
        welcome_message = "Hi! I can tell you the last few songs played K-E-X-P, would you like to hear them?"
        return question(welcome_message)

    @ask.intent("YesIntent")
    def share_recent_songs():
        songs = get_songs(event, context)
        if songs['first_song']['song_artist']['song_name_01'] != "":
            now_playing_msg = "The artist currently playing is " + songs['first_song']['song_name_01'] + " by " + songs['first_song']['song_artist_01'] + " off the album " + songs['first_song']['song_album_01'] + "."
        else:
            now_playing_msg = "The artist currently playing is " + songs['first_song']['song_name_02'] + " by " + songs['first_song']['song_artist_02'] + " off the album " + songs['first_song']['song_album_02'] + "."
        return statement(now_playing_msg)

    @ask.intent("NoIntent")
    def no_intent():
        bye_text = "Okay, no worries then... bye!"

def get_songs(event, context):
    print("getting url: " + event['url'] + ". . .")

    if 'url' in event.keys():
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1280x1696')
        chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--data-path=/tmp/data-path')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--homedir=/tmp')
        chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

        driver = webdriver.Chrome(chrome_options=chrome_options)
        sleep(1)
        driver.get(event['url'])
    else:
        print("Error: ")
        return ("Couldnt get url from event object")

    try:
        #first song
        xpath_time_01 = '//div[@class="PlaylistItem u-mb1"][1]//div[@class="PlaylistItem-time"][1]//h5[1]'
        xpath_song_name_01 = '//div[@class="PlaylistItem u-mb1"][1]//div[@class="PlaylistItem-primaryContent"]//h3[1]'
        xpath_song_artist_01 = '//div[@class="PlaylistItem u-mb1"][1]//div[@class="PlaylistItem-primaryContent"]//div[1]'
        xpath_song_album_01 = '//div[@class="PlaylistItem u-mb1"][1]//div[@class="PlaylistItem-primaryContent"]//div[2]'

        song_time_01 = driver.find_element_by_xpath(xpath_time_01).get_attribute('innerHTML')
        song_name_01 = driver.find_element_by_xpath(xpath_song_name_01).get_attribute('innerHTML')
        song_artist_01 = driver.find_element_by_xpath(xpath_song_artist_01).get_attribute('innerHTML')
        song_album_01 = driver.find_element_by_xpath(xpath_song_album_01).get_attribute('innerHTML')
    except:
        song_artist_01 = ""
        song_album_01 = ""
        
    try:
        #second song
        xpath_time_02 = '//div[@class="PlaylistItem u-mb1"][2]//div[@class="PlaylistItem-time"][1]//h5[1]'
        xpath_song_name_02 = '//div[@class="PlaylistItem u-mb1"][2]//div[@class="PlaylistItem-primaryContent"]//h3[1]'
        xpath_song_artist_02 = '//div[@class="PlaylistItem u-mb1"][2]//div[@class="PlaylistItem-primaryContent"]//div[1]'
        xpath_song_album_02 = '//div[@class="PlaylistItem u-mb1"][2]//div[@class="PlaylistItem-primaryContent"]//div[2]'

        song_time_02 = driver.find_element_by_xpath(xpath_time_02).get_attribute('innerHTML')
        song_name_02 = driver.find_element_by_xpath(xpath_song_name_02).get_attribute('innerHTML')
        song_artist_02 = driver.find_element_by_xpath(xpath_song_artist_02).get_attribute('innerHTML')
        song_album_02 = driver.find_element_by_xpath(xpath_song_album_02).get_attribute('innerHTML')
    except:
        song_artist_02 = ""
        song_album_02 = ""

    try:
        #third song   
        xpath_time_03 = '//div[@class="PlaylistItem u-mb1"][3]//div[@class="PlaylistItem-time"][1]//h5[1]'
        xpath_song_name_03 = '//div[@class="PlaylistItem u-mb1"][3]//div[@class="PlaylistItem-primaryContent"]//h3[1]'
        xpath_song_artist_03 = '//div[@class="PlaylistItem u-mb1"][3]//div[@class="PlaylistItem-primaryContent"]//div[1]'
        xpath_song_album_03 = '//div[@class="PlaylistItem u-mb1"][3]//div[@class="PlaylistItem-primaryContent"]//div[2]'

        song_time_03 = driver.find_element_by_xpath(xpath_time_03).get_attribute('innerHTML')
        song_name_03 = driver.find_element_by_xpath(xpath_song_name_03).get_attribute('innerHTML')
        song_artist_03 = driver.find_element_by_xpath(xpath_song_artist_03).get_attribute('innerHTML')
        song_album_03 = driver.find_element_by_xpath(xpath_song_album_03).get_attribute('innerHTML')
    except:
        song_artist_03 = ""
        song_album_03 = ""

    recent_songs = []
    first_song = {
        'time': song_time_01,
        'name': song_name_01,
        'artist': song_artist_01,
        'album': song_album_01
    }
    second_song = {
        'time': song_time_02,
        'name': song_name_02,
        'artist': song_artist_02,
        'album': song_album_02
    }
    third_song = {
        'time': song_time_03,
        'name': song_name_03,
        'artist': song_artist_03,
        'album': song_album_03
    }

    recent_songs.append(first_song)
    #NOTE: there is a bug on the KEXP page that double-prints the first or second most recent songs sometimes this if-statement checks for dupes
    if song_name_02 != song_name_01:
        recent_songs.append(second_song)
    if song_name_03 != song_name_02 and song_name_03 != song_name_01:
        recent_songs.append(third_song)
    
    print(recent_songs)
    driver.close()

    return recent_songs
from kivymd.uix.chip.chip import MDIcon
from kivy.uix.image import AsyncImage
from kivymd.uix.banner.banner import MDFlatButton
from kivymd.uix.expansionpanel.expansionpanel import ImageLeftWidget
from kivymd.uix.banner.banner import OneLineAvatarListItem
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.filemanager.filemanager import FitImage
from kivymd.uix.bottomsheet.bottomsheet import MDIconButton
from kivymd.uix.navigationdrawer.navigationdrawer import NavigationDrawerContentError
from kivymd.uix.card.card import MDRelativeLayout
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivy.uix.dropdown import ScrollView
from kivymd.uix.list import MDList
from kivymd.uix.pickers.colorpicker.colorpicker import MDTabs
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.loader import Loader
import cohere
from rich import print
from Backend. Chatbot import ChatBot
from dotenv import dotenv_values
import subprocess
from asyncio import run
import keyboard
import asyncio
import pyautogui
import pygetwindow as gw
import subprocess
import requests
import time
from groq import Groq
import webbrowser 
from AppOpener import close, open as appopen
from pywhatkit import search, playonyt
from Backend. RealtimeSearchEngine import RealtimeSearchEngine 
import os
import random
import socketio
import threading
import subprocess
from firebase import firebase
firebase = firebase.FirebaseApplication("https://chat-app-d2935-default-rtdb.firebaseio.com/", None)
from kivy.core.audio import SoundLoader
import pygame
from kivymd.uix.toolbar import MDTopAppBar
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from pyDes import *
from kivy.uix.popup import Popup
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager,FadeTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from io import BytesIO
from kivy.uix.image import Image as GIFImage
from PIL import Image
from kivy.utils import platform
import base64
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, MDList, IconLeftWidget, TwoLineAvatarIconListItem
import json
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.scrollview import ScrollView
import requests
import os




env_vars = dotenv_values(".env")

CohereAPIKey = env_vars.get("CohereAPIKey")

co = cohere.Client(api_key=CohereAPIKey)

funcs = [
    "exit","general","realtime","open","close","play",
    "generate image","system","content","google search",
    "youtube search","remainder"
]



Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")


DefaultMessage = f'''{Username} : Hello {Assistantname}, How are you?
{Assistantname} Welcome {Username}. I am doing well. How may i help you?'''
subprocesses = []
Functions = ["open", "close", "play", "system", "content", "google search", "youtube search"]





env_vars = dotenv_values(".env")

GroqAPIKey = env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "05uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0e", "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]
# Define a user-agent for making web requests.
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
#Initialize the Groq client with the API key.
client = Groq(api_key=GroqAPIKey)

# Predefined professional responses for user interactions.
professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

messages = []
# System message to provide context to the chatbot.
SystemChatBot = [{"role": "system", "content": f"Hello, I am Abhay. You're a content writter. You have to write a content like letter,codes, application, essays, notes, songs, poems etc."}]


SERVER_URL = "https://7928-2401-4900-790d-e163-e00d-5972-d628-d364.ngrok-free.app" # Replace with actual IP

album_details_base_url = "https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker=0&albumid="

lyrics_base_url = "https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id="
    
search_base_url = "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query="

homedata = "www.jiosaavn.com/api.php?_format=json&_marker=0&api_version=4&ctx=web6dot0__call=webapi.getLaunchData"

song_details_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids="
playlist_details_base_url = "https://www.jiosaavn.com/api.php?__call=webapi.get&token={}&type=playlist&p=1&n=20&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0"



KV = '''

#:import SliverToolbar __main__.SliverToolbar
#: import WipeTransition kivy.uix.screenmanager.WipeTransition
#: import get_color_from_hex kivy.utils.get_color_from_hex
#:import SliverTool __main__.SliverTool

MDFloatLayout:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "home"
                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: "Ghost Comm"
                        bold: True
                        elevation: 12
                        anchor_title:"left"
                        use_overflow: True
                        padding: [10,10,10,10]
                        MDIconButton:
                            icon: "account"
                            pos_hint: {"center_x": 0.9, "center_y": 0.5}
                            theme_icon_color: "Custom"
                            text_color: 1,1,1,1
                            on_release:app.profile_screen()

                    MDTabs:
                        allow_stretch: True
                        tab_indicator_anim: True
                        tab_hint_x: True
                        Tab:
                            title: "Private Chat"
                            bold:True

                            ScrollView:
                                MDList:
                                    divider: "Inset"
                                    divider_color:1,1,1,1
                                    radius: [25,0,0,0]
                                    TwoLineAvatarListItem:
                                        id:home_name
                                        text: "Abhay"
                                        secondary_text: "Secondary text here"
                                        on_release:app.change()
                                        ImageLeftWidget:
                                            id:home_image
                                            source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                            radius: 24

                            MDIconButton:
                                size_hint: None, None
                                icon_size:"50sp"
                                on_release:app.ai_screen()
                                pos_hint: {"center_x":.85,"center_y":.25}
                                FitImage:
                                    source:"https://swisscognitive.ch/wp-content/uploads/2020/09/the-4-top-artificial-intelligence-trends-for-2021.jpeg"
                                    radius:24


                        Tab:
                            title: "Group Chat"
                            bold:True

                        Tab:
                            title: "Status"
                            bold:True

            MDScreen:
                name: "profile"

                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    

                    MDLabel:
                        id:name
                        text: "Profile"
                        
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.5,"center_y":.5}               

                FitImage:
                    id: profile_pic
                    size_hint:None, None
                    size: "300dp","300dp"
                    source:""
                    radius:24
                    pos_hint:{"center_x":0.5,"center_y":0.5}

                MDFloatingActionButton:
                    icon: "pencil"
                    pos_hint:{"center_x":0.655,"center_y":0.298}
                    on_release:app.select_pic()
                

            MDScreen:
                name:"chat"

                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    FitImage:
                        id: image
                        size_hint:.07,.7
                        radius:12
                        pos_hint:{"center_x":.13,"center_y":.5}
                        source:"https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="

                    MDLabel:
                        id:name
                        text: "Abhay"
                        
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.5,"center_y":.5}

                    MDIconButton:
                        icon: "music-box"
                        pos_hint:{"center_x":.9,"center_y":.5}
                        on_release:app.music()


                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.62
                    pos_hint:{"center_x":.5,"center_y":.56}
                    radius:15
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: [0, 10, 0, 10]  # Add padding to top and bottom
                        ScrollView:
                            id:scroll_view
                            MDList:
                                id:chat_list

                MDRaisedButton:
                    id: reply_label
                    text: ""
                    size_hint_x: 0.3
                    opacity: 0
                    pos_hint:{"center_x":.75,"center_y":.2}
                    on_release: app.cancel_reply()


                MDLabel:
                    id:typing_label
                    text:""
                    pos_hint:{"center_x":.55,"center_y":.2}
            
                            
                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.1}
                    radius:15

                    MDIconButton:
                        icon: "sticker-emoji"
                        pos_hint:{"center_x":.05,"center_y":.5}

                    MDTextField:
                        id:message_input
                        hint_text:'Type message ...'
                        mode: "fill"
                        required:False
                        pos_hint:{'center_x':0.45, 'center_y':0.5}
                        size_hint_x:.7
                        width:dp(200)
                        on_text: app.on_typing()
					    multiline:True

                    MDIconButton:
                        icon: "attachment"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.file_manager_open()

                    MDIconButton:
                        icon: "send"
                        pos_hint:{"center_x":.95,"center_y":.5}
                        on_release: app.send_message()


            MDScreen:
                name:"music"
                ScrollView:
                    do_scroll_x:True
                    do_scroll_y:False
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "90dp"
                        MDFlatButton:
                            text:"Trending Song"
                            bold: True
                            on_release:app.trend()

                        MDFlatButton:
                            text:"Bhojpuri Song"
                            bold: True
                            on_release:app.bhojpuri()

                        MDFlatButton:
                            text:"Romantic Song"
                            bold: True
                            on_release:app.romantic()

                        MDFlatButton:
                            text:"Party Song"
                            bold: True
                            on_release:app.party()

                        MDFlatButton:
                            text:"Old Song"
                            bold: True
                            on_release:app.old()

                MDLabel:
                    id: home_text
                    text: "Song is Searching ...."
                    pos_hint: {'center_x': .55, 'center_y': .5}
                    bold:True

                MDSpinner:
                    id: music_spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False

                ScrollView:
                    size_hint_y:.85
                    MDList:
                        id:home_music

                

                

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint:{"center_x": .05,"center_y": .95}
                    md_bg_color: 1,1,1,1
                    on_release: app.c()

                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .95}
                    size_hint: 0.8,0.06
                    elevation: 2
                    radius: [10,]
                    border_radius: 10
                        
                    TextInput:
                        id: song_name
                        hint_text: "Songs, artists or podcasts"
                        helper_text: "Enter song name here"
                        size_hint: .9,None
                        pos_hint:{"center_x": .2,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color
                        
            
                
                    MDIconButton:
                        icon: "magnify"
                        pos_hint:{"center_x": .93,"center_y": .5}
                        on_release:
                            app.show_data(song_name.text)

                        


            MDScreen:
                name: "music_list"
                md_bg_color: 0,0,0,0.77
                        
                MDSliverAppbar:
                    max_height: "70dp"
                    toolbar_cls: SliverToolbar()
                    
                    MDSliverAppbarHeader:

                    MDSliverAppbarContent:
                        id: cont
                        orientation: "vertical"
                        padding: "12dp"
                        spacing: "12dp"
                        md_bg_color: 0,0,0,0.77
                        adaptive_height: True
                        
            # 
                    
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False
                    
            
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint:{"center_x": .05,"center_y": .95}
                    md_bg_color: 1,1,1,1
                    on_release: app.c()

            MDScreen:
                name: "ai"

                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    FitImage:
                        id: image
                        size_hint:.07,.7
                        radius:12
                        pos_hint:{"center_x":.13,"center_y":.5}
                        source:"https://swisscognitive.ch/wp-content/uploads/2020/09/the-4-top-artificial-intelligence-trends-for-2021.jpeg"

                    MDLabel:
                        id:name
                        text: "A.I ChatBot"
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.5,"center_y":.5}

                    


                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.62
                    pos_hint:{"center_x":.5,"center_y":.56}
                    radius:15
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: [0, 10, 0, 10]  # Add padding to top and bottom
                        ScrollView:
                            id:scroll_view_ai
                            MDList:
                                id:ai_list
                            
                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.1
                    pos_hint:{"center_x":.5,"center_y":.1}
                    radius:15

                    MDIconButton:
                        icon: "sticker-emoji"
                        pos_hint:{"center_x":.05,"center_y":.5}

                    MDTextField:
                        id:ai_message
                        hint_text:'Type message ...'
                        mode: "fill"
                        required:False
                        pos_hint:{'center_x':0.45, 'center_y':0.5}
                        size_hint_x:.7
                        width:dp(200)
					    multiline:True

                    MDIconButton:
                        icon: "attachment"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.file_manager_open()

                    MDIconButton:
                        icon: "send"
                        pos_hint:{"center_x":.95,"center_y":.5}
                        on_release: app.send_message_ai()


'''

sk = ""

def GoogleSearch(Topic):
    time.sleep(5)
    active_window = gw.getActiveWindow()
    if "Xstream Play" in active_window.title:
        pyautogui.moveTo(1503, 179)
        pyautogui.click()
        pyautogui.write(Topic)
        pyautogui.press("enter")

        time.sleep(2)
        pyautogui.moveTo(270, 439)
        pyautogui.click()

        pyautogui.scroll(-500)
    

        pyautogui.moveTo(182,561)
    else:
        search(Topic) 
    #return True

def Content(Topic):
    def OpenNotePad(File):
        default_text_editor = "notepad.exe"
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        sk = ""
        messages.append({"role":"user", "content": f"{prompt}"})

        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")

        messages.append({"role":'assistant', "content": Answer})
        return Answer
    
    Topic: str = Topic.replace("Content", "")
    ContentByAI = ContentWriterAI(Topic)
    sk = ContentByAI

    with open(rf"Data\{Topic.lower().replace(' ','')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI)
        file.close()

    OpenNotePad(rf"Data\{Topic.lower().replace(' ','')}.txt")
    return True

def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(command):
    
    playonyt(command)


def OpenApp(app, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True

    except:
        active_window = gw.getActiveWindow()

        if "Google Chrome" in active_window.title:
            if "first account" in app or "mera account" in app or "my account" in app:
                pyautogui.moveTo(636, 454)
                pyautogui.click()
                

            elif "second account" in app or "second account" in app:
                pyautogui.moveTo(839, 455)
                pyautogui.click()

            elif "new tab" in app:
                pyautogui.hotkey('ctrl','t')

            elif "Airtel stream" in app:
                pyautogui.moveTo(1301, 615)
                pyautogui.click()

            else:
                webbrowser.open("www."+app+".com")

           

        else:
            webbrowser.open("www."+app+".com")

def CloseApp(app):

    if "chrome" in app:
        pass

    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False

def System(command):
    active_window = gw.getActiveWindow()
    

    if command == "bluetooth off" or command == "disconnect bluetooth" or command == "bluetooth":
        pyautogui.hotkey('win', 'a')
        keyboard.press_and_release("right")
        keyboard.press_and_release("enter")

    elif command == "wifi off" or command == "disconnect wifi" or command == "wifi":
        pyautogui.hotkey('win', 'a')
        keyboard.press_and_release("enter")

    elif "mute" in command:
        keyboard.press_and_release("volume mute")

    elif "unmute" in command:
        keyboard.press_and_release("volume unmute")
    elif "volume up" in command:
        keyboard.press_and_release("up")
        keyboard.press_and_release("volume up")
    elif "volume down" in command:
        keyboard.press_and_release("volume down")

    return True

async def TranslateAndExecute(commands: list[str]):
    funcs = []

    for command in commands:
        if command.startswith("open "):
            if "open it" in command:
                pass

            if "open file" == command:
                pass

            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
                funcs.append(fun)


        elif command.startswith("general "):
            pass

        elif command.startswith("realtime "):
            pass

        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
            funcs.append(fun)

        elif command.startswith("play "):
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
            funcs.append(fun)

        elif command.startswith("content "):
            fun = asyncio.to_thread(Content, command.removeprefix("content "))
            funcs.append(fun)

        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))
            funcs.append(fun)

        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search "))
            funcs.append(fun)

        elif command.startswith("system "):
            fun = asyncio.to_thread(System, command.removeprefix("system "))
            funcs.append(fun)


        else:
            print(f"No Function Found For {command}")

    results = await asyncio.gather(*funcs)

    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result

async def Automation(commands: list[str]):
    async for result in TranslateAndExecute(commands):
        pass

    return True


messages = []

preamble = """
You are a very accurate Decision-Making Model, which decides what kind of a query is given to you.
You will decide whether a query is a 'general' query, a 'realtime' query, or is asking to perform any task or automation like 'open facebook, instagram', 'can you write a application and open it in notepad'
*** Do not answer any query, just decide what kind of query is given to you. ***
-> Respond with 'general ( query )' if a query can be answered by a llm model (conversational ai chatbot) and doesn't require any up to date information like if the query is 'who was akbar?' respond with 'general who was akbar?', if the query is 'how can i study more effectively?' respond with 'general how can i study more effectively?', if the query is 'can you help me with this math problem?' respond with 'general can you help me with this math problem?', if the query is 'Thanks, i really liked it.' respond with 'general thanks, i really liked it.' , if the query is 'what is python programming language?' respond with 'general what is python programming language?', etc. Respond with 'general (query)' if a query doesn't have a proper noun or is incomplete like if the query is 'who is he?' respond with 'general who is he?', if the query is 'what's his networth?' respond with 'general what's his networth?', if the query is 'tell me more about him.' respond with 'general tell me more about him.', and so on even if it require up-to-date information to answer. Respond with 'general (query)' if the query is asking about time, day, date, month, year, etc like if the query is 'what's the time?' respond with 'general what's the time?'.
-> Respond with 'realtime ( query )' if a query can not be answered by a llm model (because they don't have realtime data) and requires up to date information like if the query is 'who is indian prime minister' respond with 'realtime who is indian prime minister', if the query is 'tell me about facebook's recent update.' respond with 'realtime tell me about facebook's recent update.', if the query is 'tell me news about coronavirus.' respond with 'realtime tell me news about coronavirus.', etc and if the query is asking about any individual or thing like if the query is 'who is akshay kumar' respond with 'realtime who is akshay kumar', if the query is 'what is today's news?' respond with 'realtime what is today's news?', if the query is 'what is today's headline?' respond with 'realtime what is today's headline?', etc.
-> Respond with 'open (application name or website name)' if a query is asking to open any application like 'open facebook', 'open telegram', etc. but if the query is asking to open multiple applications, respond with 'open 1st application name, open 2nd application name' and so on.
-> Respond with 'close (application name)' if a query is asking to close any application like 'close notepad', 'close facebook', etc. but if the query is asking to close multiple applications or websites, respond with 'close 1st application name, close 2nd application name' and so on.
-> Respond with 'play (song name)' if a query is asking to play any song like 'play afsanay by ys', 'play let her go', etc. but if the query is asking to play multiple songs, respond with 'play 1st song name, play 2nd song name' and so on.
-> Respond with 'generate image (image prompt)' if a query is requesting to generate a image with given prompt like 'generate image of a lion', 'generate image of a cat', etc. but if the query is asking to generate multiple images, respond with 'generate image 1st image prompt, generate image 2nd image prompt' and so on.
-> Respond with 'reminder (datetime with message)' if a query is requesting to set a reminder like 'set a reminder at 9:00pm on 25th june for my business meeting.' respond with 'reminder 9:00pm 25th june business meeting'.
-> Respond with 'system (task name)' if a query is asking to mute, unmute, volume up, volume down , etc. but if the query is asking to do multiple tasks, respond with 'system 1st task, system 2nd task', etc.
-> Respond with 'content (topic)' if a query is asking to write any type of content like application, codes, emails or anything else about a specific topic but if the query is asking to write multiple types of content, respond with 'content 1st topic, content 2nd topic' and so on.
-> Respond with 'google search (topic)' if a query is asking to search a specific topic on google but if the query is asking to search multiple topics on google, respond with 'google search 1st topic, google search 2nd topic' and so on.
-> Respond with 'youtube search (topic)' if a query is asking to search a specific topic on youtube but if the query is asking to search multiple topics on youtube, respond with 'youtube search 1st topic, youtube search 2nd topic' and so on.
*** If the query is asking to perform multiple tasks like 'open facebook, telegram and close whatsapp' respond with 'open facebook, open telegram, close whatsapp' ***
*** If the user is saying goodbye or wants to end the conversation like 'bye jarvis.' respond with 'exit'.***
*** Respond with 'general (query)' if you can't decide the kind of query or if a query is asking to perform a task which is not mentioned above. ***
"""

ChatHistory = [
    {"role":"User", "message":"how are you?"},
    {"role":"Chatbot", "message":"general how are you?"},
    {"role":"User", "message":"do you like pizza?"},
    {"role":"Chatbot", "message":"general do you like pizza?"},
    {"role":"User", "message":"open chrome and tell me about mahatma gandhi."},
    {"role":"Chatbot", "message":"open chrome, general tell me about mahatma gandhi"},
    {"role":"User", "message":"open chrome and firefox"},
    {"role":"Chatbot", "message":"open chrome, open firefox"},
    {"role":"User", "message":"what is today's date and by the way remaind me that i have a dancing performance on 5th august"},
    {"role":"Chatbot", "message":"general what is today's date and by the way remaind 11:00 pm 5th aug dancing performance"},
    {"role":"User", "message":"chat with me"},
    {"role":"Chatbot", "message":"general chat with me"},
]

def FirstLayerDMM(prompt: str = "test"):
    messages.append({"role":"user", "content":f"{prompt}"})

    stream = co.chat_stream(
        model="command-r-plus",
        message=prompt,
        temperature=0.7,
        chat_history=ChatHistory,
        prompt_truncation="OFF",
        connectors=[],
        preamble=preamble
    )

    response = ""

    for event in stream:
        if event.event_type == "text-generation":
            response += event.text

    response = response.replace("\n", "")
    response = response.split(",")

    response = [i.strip() for i in response]

    temp = []

    for task in response:
        for func in funcs:
            if task.startswith(func):
                temp.append(task)

    response = temp

    if "{query}" in response:
        newresponse = FirstLayerDMM(prompt=prompt)

    else:
        return response

class CustomGIFButton(ButtonBehavior, GIFImage):
    """ A custom button that uses a GIF as its image. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_press(self):
        print("GIF Button Pressed!")

    def on_release(self):
        popup = Popup(title="GIF Button Clicked!",
                      content=MDLabel(text="You clicked the GIF button!"),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

class Tab(MDFloatLayout, MDTabsBase):
    pass

class abhay(TwoLineAvatarIconListItem):
    pass

class SliverTool(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.title = "My Music"

class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.title = "Results"

class Test(MDApp):

    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    username = "Himanshu"
    scroll = "False"
    song_url = ""
    trend_song = ""
    bhojpuri_song = ""
    romantic_song = ""
    party_song = ""
    old_song = ""
    selected_message = None 

    def build(self):
        
        self.file_manager = MDFileManager(exit_manager=self.file_manager_close, select_path=self.upload_file)
        self.icon = "topbarlogo.png"
        self.title = "Ghost Comm - Silent.Stealthy.Secret"
        self.manager_open = False
        self.file = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
        self.sio = socketio.Client()
        self.sio.connect("https://7928-2401-4900-790d-e163-e00d-5972-d628-d364.ngrok-free.app")
        self.sio.on("message", self.receive_message)
        self.sio.on("file_received", self.receive_file)
        self.sio.on("upload_progress", self.update_upload_progress)
        self.sio.on("typing", self.show_typing)
        self.sio.on("stopped_typing", self.hide_typing)
        self.sio.on("play_music", self.play_received_music)
        self.sio.on("delete_message", self.handle_delete_message)
        self.sio.on("edit_message", self.handle_edit_message)
        self.process = None
        pygame.mixer.init()
        

        self.typing_timer = None
        return Builder.load_string(KV)
    
    
    def change_screen(self, screen, *args):
        if self.root.ids.screen_manager.current == 'home' or self.root.ids.screen_manager.current == "hl":
            try:
                pass
            except:
                pass
        if args:
            self.root.ids.screen_manager.transition.direction = args[0]
            if args[0] != 'right':
                self.last_screen.append(self.root.ids.screen_manager.current)
                
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
            self.last_screen.append(self.root.ids.screen_manager.current)
        self.root.ids.screen_manager.current = screen

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 13:
            if self.root.ids.screen_manager.current == 'music':
                self.show_data(self.root.ids.song_name.text)
            else:
                pass

        if keyboard == 13 and "ctrl" in modifiers:
            self.send_message()
            return True
      
        if keyboard in (1001, 27):   
            if self.manager_open:
                self.file_manager.back()
            else:
                self.back_screen()
 
        return True
    
    def ai_screen(self):
        self.change_screen("ai")

    def change(self):
        self.change_screen("chat")

    def c(self):
        self.change_screen("chat")

    def music(self):
        self.change_screen("music")

    def show_data(self, query):
       # close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)
        if query == '':
            self.dia = MDDialog(title="Invalid Name", text="Please enter a song name", size_hint=(0.7,1))
            self.dia.open()
            
        else:
            #self.trend()
          #  self.root.ids.screen_manager.transition = WipeTransition()
            self.change_screen('music_list')
            self.root.ids.cont.clear_widgets()
            
            self.root.ids.spinner.active = True
            req = UrlRequest(search_base_url+query.replace(' ','+'), self.show_list)


    def show_list(self, req, result):
        self.root.ids.song_name.text = ""
        self.search_data = json.loads(result.replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"))['songs']['data']
        
        
        for i in range(len(self.search_data)):
            print(self.search_data[i]["title"])
            
            self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
            
        
            
            lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),theme_text_color="Custom",text_color=(1,1,1,1), secondary_text=self.search_data[i]['more_info']['primary_artists'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"), secondary_theme_text_color="Custom",secondary_text_color=(220/255,86/255,219/255,0.74/1),on_press=lambda x,y=i: self.song_details(y))
            sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
            
            sl = FitImage(source=self.image_url, radius=20)
            
            sk.add_widget(sl)
            lst.add_widget(sk)
            
      
         
            self.root.ids.cont.add_widget(lst)
            
        self.root.ids.spinner.active = False

    def trend(self, *args):
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.trend_s, daemon=True).start()

    def trend_s(self):
        Clock.schedule_once(lambda dt: self.trend_so())

    def trend_so(self):
        self.root.ids.home_music.clear_widgets()
        if self.trend_song == "":

            response = requests.get(playlist_details_base_url.format("I3kvhipIy73uCJW60TJk1Q__")+"&lyrics=true")
            if response.status_code == 200:
                songs_json = response.text.encode().decode()
                songs_json = json.loads(songs_json)
                self.search_data = songs_json['list']
                self.trend_song = self.search_data

                for i in range(len(self.search_data)):
                    print(self.search_data[i]["title"])
                    
                    self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                    
                
                    
                    lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                    sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                    
                    sl = FitImage(source=self.image_url, radius=20)
                    
                    sk.add_widget(sl)
                    lst.add_widget(sk)
                    
            
                
                    self.root.ids.home_music.add_widget(lst)



        else:
            self.search_data = self.trend_song
            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""


    def bhojpuri(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.bhojpuri_s, daemon=True).start()

    def bhojpuri_s(self):
        Clock.schedule_once(lambda dt: self.bhojpuri_so())

    def bhojpuri_so(self):
        try:
            self.search_data = self.bhojpu
            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        except:

            response = requests.get(playlist_details_base_url.format("8c-UE,,iBhN8497ZNqIDKA__")+"&lyrics=true")
            if response.status_code == 200:
                songs_json = response.text.encode().decode()
                songs_json = json.loads(songs_json)
                self.search_data = songs_json['list']
                self.bhojpuri_song = self.search_data
                for i in range(len(self.search_data)):
                    print(self.search_data[i]["title"])
                    
                    self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                    
                
                    
                    lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                    sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                    
                    sl = FitImage(source=self.image_url, radius=20)
                    
                    sk.add_widget(sl)
                    lst.add_widget(sk)
                    
            
                
                    self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def romantic(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.romantic_s, daemon=True).start()

    def romantic_s(self):
        Clock.schedule_once(lambda dt: self.romantic_so())

    def romantic_so(self):
        response = requests.get(playlist_details_base_url.format("SBKnUgjNeMIwkg5tVhI3fw__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def party(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.party_s, daemon=True).start()

    def party_s(self):
        Clock.schedule_once(lambda dt: self.party_so())

    def party_so(self):
        response = requests.get(playlist_details_base_url.format("qVvfieICUY5ieSJqt9HmOQ__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def old(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.old_s, daemon=True).start()

    def old_s(self):
        Clock.schedule_once(lambda dt: self.old_so())

    def old_so(self):
        response = requests.get(playlist_details_base_url.format("qaou266p,04va8qgomsMOw__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_details(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)
        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""
        

    def song_details(self,i):
        self.song_id = self.search_data[i]['id']
        self.fetch_thread = threading.Thread(target=self.fetch_details)
        self.fetch_thread.start()

        

    def fetch_details(self):

        print('started fetching details')
        data = json.loads(requests.get(song_details_base_url+self.song_id).text.replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"))[self.song_id]
        try:
            data['media_url'] = self.decrypt_url(data['encrypted_media_url'])
            if data['320kbps'] != "true":
                data['media_url'] = data['media_url'].replace(
                    "_320.mp4", "_160.mp4")
            data['media_preview_url'] = data['media_url'].replace(
                "_320.mp4", "_96_p.mp4").replace("_160.mp4", "_96_p.mp4").replace("//aac.", "//preview.")
        except KeyError or TypeError:
            url = data['media_preview_url']
            url = url.replace("preview", "aac")
            if data['320kbps'] == "true":
                url = url.replace("_96_p.mp4", "_320.mp4")
            else:
                url = url.replace("_96_p.mp4", "_160.mp4")
            data['media_url'] = url
        print(data['media_url'])

        self.song_url = data['media_url']

        print(self.song_url)
        self.sio.emit("play_music", {"url": self.song_url,"user":self.username})
        
        
        if self.process:
            self.stop_music()  # Stop any existing process

        # Start ffplay in the background
        self.process = subprocess.Popen(
            ["ffplay", "-nodisp", "-autoexit", self.song_url],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )





    def decrypt_url(self,url):
        des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",
                        pad=None, padmode=PAD_PKCS5)
        enc_url = base64.b64decode(url.strip())
        dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
        dec_url = dec_url.replace("_96.mp4", "_320.mp4")
        return dec_url

    def on_start(self):
        Clock.schedule_once(self.trend,1)
        try:
            
            self.root.ids.profile_pic.source = "profile.jpg"
        except:
            self.root.ids.profile_pic.source = "https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_640.jpg"

    def send_message(self):
        msg = self.root.ids.message_input.text.strip()

        if msg:
            message_id = str(time.time()) 
            data = {
                "sender": self.username,
                "message_id": message_id,
                "message": msg,
                "reply_to": self.selected_message if self.selected_message else None
            }
            self.sio.emit("message", data)  # Send to server
            self.selected_message = None  # Reset after sending
            self.root.ids.message_input.text = ""  # Clear input
            self.update_reply_ui(None)

    def receive_message(self,data):
        
        reply_to = data.get("reply_to", None)
        Clock.schedule_once(lambda dt: self.add_message_to_ui(data, reply_to))

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))

    def file_manager_close(self, *args):
        self.file_manager.close()

    def upload_file(self, path):
        self.file_manager_close()
        filename = os.path.basename(path)
        file_size = os.path.getsize(path)
        chunk_size = 1024 * 10  # 10 KB per chunk
        total_chunks = (file_size + chunk_size - 1) // chunk_size

        with open(path, "rb") as f:
            for chunk_index in range(total_chunks):
                chunk_data = f.read(chunk_size)
                self.sio.emit("file_chunk", {
                    "filename": filename,
                    "chunk": chunk_data,
                    "chunk_index": chunk_index,
                    "total_chunks": total_chunks
                })
        
        # Show upload progress in UI
        Clock.schedule_once(lambda dt: self.show_upload_progress(filename))

    def show_upload_progress(self, filename):
        progress_bar = MDProgressBar(value=0, max=100)
        progress_item = OneLineAvatarIconListItem(text=f"Uploading {filename}...")
        progress_item.add_widget(progress_bar)
        self.root.ids.chat_list.add_widget(progress_item)
        setattr(self, f"upload_progress_{filename}", progress_bar)

    def back(self):
        self.change_screen("home")

    def add_file_to_ui(self, filename, file_url):
        file_item = OneLineAvatarIconListItem(text=f"{self.username+filename}")
        file_item.add_widget(IconLeftWidget(icon="download"))
        file_item.bind(on_release=lambda x: self.download_file(file_url, filename))
        self.root.ids.chat_list.add_widget(file_item)

    def update_upload_progress(self, data):
        filename = data["filename"]
        progress = data["progress"]
        
        if hasattr(self, f"upload_progress_{filename}"):
            Clock.schedule_once(lambda dt: setattr(getattr(self, f"upload_progress_{filename}"), "value", progress))
    
    def receive_file(self, data):
        filename = data["filename"]
        file_url = data["url"]
        
        Clock.schedule_once(lambda dt: self.add_file_to_ui(filename, file_url))

    def add_message_to_ui(self, data, reply_to=None):
        chat_list = self.root.ids.chat_list
        sender = data["sender"]
        message_id = data["message_id"]
        message = data["message"]
        reply_to = data.get("reply_to", None)
        long_text = f"{sender}: {message}"
        ak = break_text(long_text, 75)
        
        bubble = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            pos_hint={'center_x': 0.1,'center_y': 0.5},
            padding=[40, 11],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(210/255,212/255,217/255,1),
            id=message_id 
        )

        bub = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            
            padding=[40, 10],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(0.2, 0.6, 1, 1),
            id=message_id 
        )

        label = MDLabel(
            text=ak,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            adaptive_size=True,
        )

        delete_button = MDIconButton(
            icon="delete",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),
            pos_hint={"center_x":1, "center_y":.5},
            on_release=lambda x: self.delete_message(message_id)
        )

        edit_button = MDIconButton(
            icon="pencil",
            theme_text_color="Custom",
            text_color=(0, 0, 1, 1),
            on_release=lambda x: self.show_edit_popup(message_id, message)
        )

        bub.add_widget(label)
        bubble.add_widget(bub)
        bubble.add_widget(delete_button)
        bubble.add_widget(edit_button)

        if reply_to:
            reply_bubble = MDCard(
                size_hint_x=None,
                size_hint_y=None,
                adaptive_size=True,
                padding=[15, 5],
                radius=[10, 10, 10, 10],
                md_bg_color=(0.5, 0.5, 0.5, 1)  # Gray for reply
            )
            reply_label = MDLabel(
                text=f"Replying to: {reply_to}",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                adaptive_size=True,
            )
            reply_bubble.add_widget(reply_label)
            bubble.add_widget(reply_bubble)

        bub.bind(on_release=lambda x: self.select_message(message))
        chat_list.add_widget(bubble)

    def show_edit_popup(self, message_id, old_message):
        
        """Open a popup to edit a message."""
        content = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        text_input = MDTextField(
            text=old_message,
            hint_text="Edit your message..."
        )
        content.add_widget(text_input)

        save_button = MDRaisedButton(
            text="Save",
            on_release=lambda x: self.edit_message(message_id, text_input.text)
        )
        content.add_widget(save_button)

        self.edit_popup = Popup(
            title="Edit Message",
            content=content,
            size_hint=(None, None),
            size=("400dp", "200dp"),
            background_color=(1,1,1,1)
        )
        self.edit_popup.open()

    def edit_message(self, message_id, new_message):
        print("pressed")
        """Send an edit request to the server."""
        self.sio.emit("edit_message", {"message_id": message_id, "new_message": new_message})
        self.edit_popup.dismiss()

        #self.update_message_in(message_id, new_message)

    def handle_edit_message(self, data):
        """Handle an edited message from the server."""
        message_id = data["message_id"]
        new_message = data["new_message"]
        
        Clock.schedule_once(lambda dt: self.update_message_in(message_id, new_message))

    def update_message_in(self, message_id, new_message):
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children:
            if hasattr(widget, "id") and widget.id == message_id:
                for child in widget.children:
                    if isinstance(child, MDCard):  # 🔄 Check if message is inside an extra MDCard
                        for subchild in child.children:
                            if isinstance(subchild, MDLabel):
                                subchild.text = f"{self.username}: {new_message}"
                                return

    def delete_message(self, message_id):
        """Send delete request to the server and remove the message from UI."""
        self.sio.emit("delete_message", {"message_id": message_id})
        self.remove_message_from_ui(message_id)
        print("delete")
        
    def handle_delete_message(self, data):
        """Handle message deletion from the server."""
        message_id = data["message_id"]
        Clock.schedule_once(lambda dt: self.remove_message_from_ui(message_id))

    def remove_message_from_ui(self, message_id):
        """Find and remove the message from the UI."""
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children[:]:  
            if hasattr(widget, "id") and widget.id == message_id:
                chat_list.remove_widget(widget)
                break

    def select_message(self, message):
        """Selects a message to reply to."""
        self.selected_message = message
        self.update_reply_ui(message)

    def update_reply_ui(self, message):
        """Updates the UI to show the selected message for reply."""
        reply_label = self.root.ids.reply_label

        if message:
            reply_label.text = f"Replying to: {message}"
            reply_label.opacity = 1
        else:
            reply_label.text = ""
            reply_label.opacity = 0

    def cancel_reply(self):
        """Cancels reply mode"""
        self.selected_message = None
        self.update_reply_ui(None)
      

    # def on_start(self):
    #     Clock.schedule_interval(self.up, 2)

    # def up(self, *args):
    #     self.root.ids.scroll_view.scroll_y = 0

    def download_file(self, url, filename):
        # Show download progress in UI
        Clock.schedule_once(lambda dt: self.show_download_progress(filename))

        # Start downloading in a separate thread
        threading.Thread(target=self.download_file_thread, args=(url, filename)).start()

    def show_download_progress(self, filename):
        progress_bar = MDProgressBar(value=0, max=100)
        progress_item = OneLineAvatarIconListItem(text=f"Downloading {filename}...")
        progress_item.add_widget(progress_bar)
        self.root.ids.chat_list.add_widget(progress_item)
        setattr(self, f"download_progress_{filename}", progress_bar)

    def download_file_thread(self, url, filename):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        save_path = os.path.join(os.path.expanduser("~"), filename)

        with open(save_path, "wb") as f:
            downloaded_size = 0
            for chunk in response.iter_content(1024):
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    progress = (downloaded_size / total_size) * 100
                    Clock.schedule_once(lambda dt: self.update_download_progress(filename, progress))

        Clock.schedule_once(lambda dt: self.download_complete(filename, save_path))

    def update_download_progress(self, filename, progress):
        if hasattr(self, f"download_progress_{filename}"):
            progress_bar = getattr(self, f"download_progress_{filename}")
            progress_bar.value = progress

    def download_complete(self, filename, save_path):
        # Remove progress bar and show downloaded file
        Clock.schedule_once(lambda dt: self.replace_download_progress(filename, save_path))

    def replace_download_progress(self, filename, save_path):
        file_item = OneLineAvatarIconListItem(text=f"✅ {filename} (Downloaded)")
        file_item.add_widget(IconLeftWidget(icon="folder"))
        file_item.bind(on_release=lambda x: Clipboard.copy(save_path))
        self.root.ids.chat_list.add_widget(file_item)
        MDDialog(text=f"File saved: {save_path} (Path copied to clipboard)").open()

    def on_typing(self):
        """ Detects user typing and notifies others """
        self.sio.emit("typing", {"user": self.username})

        # Cancel any previous timer and restart it
        if self.typing_timer:
            self.typing_timer.cancel()
        self.typing_timer = Clock.schedule_once(self.user_stopped_typing, 2)


    def user_stopped_typing(self, dt):
        """ Called when user stops typing for 2 seconds """
        self.sio.emit("stopped_typing", {"user": self.username})

    def show_typing(self, data):
        """ Show 'User is typing...' only if another user is typing """
        if data["user"] != self.username:  # Avoid showing own typing status
            Clock.schedule_once(lambda dt: setattr(
                self.root.ids.typing_label, 'text', f"{data['user']} is typing..."
            ))

    def hide_typing(self, data):
        """ Hide 'User is typing...' when typing stops """
        if data["user"] != self.username:  # Ensure only other's typing is hidden
            Clock.schedule_once(lambda dt: setattr(self.root.ids.typing_label, 'text', ""))

    # def play_music(self, song_url):
    #     """ Sends song URL to all users """
    #     self.sio.emit("play_music", {"url": self.song_url})
        #os.system(f'ffplay -nodisp -autoexit "{self.song_url}"')

    def play_received_music(self, data):
        """ Plays music when received from another user """
        user = data.get("user")
         # Ensure only other's music is played
        if user == self.username:
            print("True")

        else:
            song_url = data.get("url", "")
            print(song_url)
            if self.process:
                self.stop_music()  # Stop any existing process

            # Start ffplay in the background
            self.process = subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", song_url],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )

        #os.system(f'ffplay -nodisp -autoexit "{song_url}"')

    def stop_music(self):
        """Stops the currently playing music."""
        if self.process:
            self.process.terminate()  # Kill ffplay process
            self.process = None
            print("Stopped.")

    def profile_screen(self):
        self.change_screen("profile")

    def select_pic(self):
        self.file.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        
        try:
            re = firebase.delete("chat-app-d2935-default-rtdb/user/prfile", "")
        except:
            pass
        with open(path, "rb") as image_file:
            image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_json = json.dumps(image_base64)
        data = {
            "image": image_json
        }

        ak = firebase.post("chat-app-d2935-default-rtdb/user/prfile",data)
        
        res = firebase.get("chat-app-d2935-default-rtdb/user/prfile", "")
        for i in res.keys():
            ak = res[i]["image"]

            image_data = json.loads(ak)
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
            print(image_bytes)
            self.pro()
            image.save("profile.jpg")
            self.root.ids.profile_pic.source = ""
            self.root.ids.profile_pic.source = "profile.jpg"
                

            
        print(path)

    def pro(self):
        os.remove("profile.jpg")

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file.close()

    def send_message_ai(self):
        Query = self.root.ids.ai_message.text
        chat_list = self.root.ids.ai_list
        bubble = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            pos_hint={'center_x': 0.1,'center_y': 0.5},
            padding=[40, 11],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(210/255,212/255,217/255,1)  # Light blue
        )

        bub = MDCard(
            size_hint_x=None,  # Let width be dynamically set
            size_hint_y=None,
            adaptive_size=True,
            padding=[40, 10],
            radius=[10, 10, 10, 0],  # Rounded edges
            md_bg_color=(0.2, 0.6, 1, 1)  # Light blue
        )

        label = MDLabel(
            text=f"{self.username}:{Query}",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            adaptive_size=True,
        )
        bub.add_widget(label)

        bubble.add_widget(bub)
        chat_list.add_widget(bubble)
        self.root.ids.scroll_view_ai.scroll_y = 0
        threading.Thread(target=self.a_i, daemon=True).start()

    def a_i(self):
        Clock.schedule_once(lambda dt: self.update_ui())

    def update_ui(self):
        Query = self.root.ids.ai_message.text
        TaskExecution = False
        ImageExecution = False 
        self.root.ids.ai_message.text = ""
        ImageGenerationQuery = ""
        chat_list = self.root.ids.ai_list
        if Query != "":
            Decision = FirstLayerDMM(Query)
            ak = random.choice(Decision)

            if "realtime" in ak:
                QueryFinal = ak.replace("realtime ", "")
                Answer = RealtimeSearchEngine(QueryFinal)
                long_text = "Jarvis: "+Answer
                print(long_text)
                ak = break_text(long_text, 75)
                chat_list = self.root.ids.ai_list
                bubble = MDCard(
                    size_hint_x=None,  # Let width be dynamically set
                    size_hint_y=None,
                    adaptive_size=True,
                    pos_hint={'center_x': 0.1,'center_y': 0.5},
                    padding=[40, 11],
                    radius=[10, 10, 10, 0],  # Rounded edges
                    md_bg_color=(210/255,212/255,217/255,1)  # Light blue
                )

                bub = MDCard(
                    size_hint_x=None,  # Let width be dynamically set
                    size_hint_y=None,
                    adaptive_size=True,
                    padding=[40, 10],
                    radius=[10, 10, 10, 0],  # Rounded edges
                    md_bg_color=(0.2, 0.6, 1, 1)  # Light blue
                )

                label = MDLabel(
                    text=ak,
                    size_hint_x=0.9,
                    adaptive_height=True,
                    text_size="15sp",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    size_hint_y=None,
                    adaptive_size=True,
                )
                bub.add_widget(label)

                bubble.add_widget(bub)
                chat_list.add_widget(bubble)
                return True
            
            self.root.ids.scroll_view_ai.scroll_y = 0

        else:
            pass

        G = any([i for i in Decision if i.startswith("general")])
        R = any([i for i in Decision if i.startswith("realtime")])
        Mearged_query = " and " .join(
            [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
        )
        for queries in Decision:
            if "generate " in queries:
                ImageGenerationQuery = str(queries) 
                ImageExecution = True
        for queries in Decision:
            if TaskExecution == False:
                if any(queries.startswith(func) for func in Functions):
                    tak = run(Automation(list(Decision)))
                    long_text = "Jarvis: "+str(tak)
                    ak = break_text(long_text, 75)
                    chat_list = self.root.ids.ai_list
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.1,'center_y': 0.5},
                        padding=[40, 11],
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(210/255,212/255,217/255,1)  # Light blue
                    )

                    bub = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        padding=[40, 10],
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(0.2, 0.6, 1, 1)  # Light blue
                    )

                    label = MDLabel(
                        text=ak,
                        size_hint_x=0.9,
                        adaptive_height=True,
                        text_size="15sp",
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                    )
                    bub.add_widget(label)

                    bubble.add_widget(bub)
                    chat_list.add_widget(bubble) 
                    TaskExecution = True


        if ImageExecution == True:
            long_text = "wait for a moment,I am generating this, after complete i will open it automatically"
            ak = break_text(long_text, 75)
            chat_list = self.root.ids.ai_list
            bubble = MDCard(
                size_hint_x=None,  # Let width be dynamically set
                size_hint_y=None,
                adaptive_size=True,
                pos_hint={'center_x': 0.1,'center_y': 0.5},
                padding=[40, 11],
                radius=[10, 10, 10, 0],  # Rounded edges
                md_bg_color=(210/255,212/255,217/255,1)  # Light blue
            )

            bub = MDCard(
                size_hint_x=None,  # Let width be dynamically set
                size_hint_y=None,
                adaptive_size=True,
                padding=[40, 10],
                radius=[10, 10, 10, 0],  # Rounded edges
                md_bg_color=(0.2, 0.6, 1, 1)  # Light blue
            )

            label = MDLabel(
                text=ak,
                size_hint_x=0.9,
                adaptive_height=True,
                text_size="15sp",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                adaptive_size=True,
            )
            bub.add_widget(label)

            bubble.add_widget(bub)
            chat_list.add_widget(bubble)
            self.root.ids.scroll_view_ai.scroll_y = 0
            with open(r"Frontend\Files\ImageGeneration.data", "w") as file: 
                file.write(f"{ImageGenerationQuery},True")
            try:
                p1 = subprocess.Popen(['python', r'Backend\ImageGeneration.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE, shell=False)
                
            except Exception as e:
                print(f"Error: {e}")

        if G and R or R:
            Answer = RealtimeSearchEngine(Mearged_query)
            return True
        else:
            for Queries in Decision:
                if "general" in Queries:
                    QueryFinal = Queries.replace("general ", "")
                    Answer = ChatBot(QueryFinal)
                    long_text = "Jarvis: "+Answer
                    ak = break_text(long_text, 75)
                    chat_list = self.root.ids.ai_list
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.1,'center_y': 0.5},
                        padding=[40, 11],
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(210/255,212/255,217/255,1)  # Light blue
                    )

                    bub = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        padding=[40, 10],
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(0.2, 0.6, 1, 1)  # Light blue
                    )

                    label = MDLabel(
                        text=ak,
                        size_hint_x=0.9,
                        adaptive_height=True,
                        text_size="15sp",
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                    )
                    bub.add_widget(label)

                    bubble.add_widget(bub)
                    chat_list.add_widget(bubble)
                    self.root.ids.scroll_view_ai.scroll_y = 0
                    return True
                
                    
                
                

                elif "exit" in Queries:
                    pass

        
        

def break_text(text, limit):
    return '\n'.join([text[i:i+limit] for i in range(0, len(text), limit)])

Test().run()
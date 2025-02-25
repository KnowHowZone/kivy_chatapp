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


KV = '''
BoxLayout:
    orientation: "vertical"
    MDTopAppBar:
            title: "MDToolbar"
            icon: "git"
        # mode: "free-end"
        # MDIcon:
        #     icon: "logo.png"
        #     size: "100dp", "100dp"
        #     pos_hint: {"center_x": 0.9, "center_y": 0.9}
    MDLabel:
        # text: "content"
        halign: "center"

'''


class Test(MDApp):
    def build(self):
        self.title = "Test Application"
        self.icon = "topbarlogo.png"
        return Builder.load_string(KV)
    
Test().run()
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:44:23 2021

@author: Ditiro
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:47:55 2021

@author: Ditiro
"""
# Required Imports
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import re as re
import streamlit as st


header = st.container()
body = st.container()
sidebar = st.container()

with header:
    st.title("Social Light")
    



with sidebar:
    with st.form("my_form"):
        username_string = st.text_input(label='Enter some text')
        password_string = st.text_input(label='Password')
        link_username = st.text_input(label='Enter some text')
        number_of_posts = st.text_input(label='Enter some text')
        submit = st.form_submit_button('Submit')
  
        if submit: 
            #create a browser-specific (Google Chrome) web navigation simulator:
            browser = webdriver.Chrome("C:/Users/Ditiro/Downloads/chromedriver.exe")
            #open the LinkedIn login page and login under a specified account:
            browser.get('https://www.linkedin.com/login')
            #enter the specified information to login to LinkedIn:
            elementID = browser.find_element_by_id('username')
            elementID.send_keys(username_string)
            elementID = browser.find_element_by_id('password')
            elementID.send_keys(password_string)
            elementID.submit()


with body:
    st.write("Social Light")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 02:31:14 2024

@author: bengierhart
"""

import streamlit as st
import pathlib
import season_quiz as sq

st.title("Actors Theatre of Louisville 24-25 Season Quiz")
st.divider()

with st.sidebar:
    st.subheader("Quiz Questions")
    #radio buttons V
    category = st.radio("Choose a category:",
                     ["***Start***","***World Premieres***", "***Community Partnerships***", "***Music***", "***All Ages***", "***It's Back!***"],
                     captions = ["There's something for everyone in the categories below!","We're known for producing original work no one has seen before, and we're not stopping now.", 
                                 "Why compete when you can collaborate?",
                                 "Musicals, concerts, and more.",
                                 "I want to bring my family to see this.",
                                 "We couldn't rest until we brought you these programs."])
    
from PIL import Image
col1, col2, col3 = st.columns(3)
with col2:
    #image1 = Image.open("announcement.jpg")
    st.image('announcement.jpg', width=300, caption="Announcing Actors Theatre of Louisville's 24-25 Season")
    #image1 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/announcement.jpg'))
    #st.image(image1, width=300, caption="Announcing Actors Theatre of Louisville's 24-25 Season")
st.write(sq.intro)
st.write(sq.start)

if category=="***World Premieres***":
    sq.question1()
    
elif category=="***Community Partnerships***":
    sq.question2()
    
elif category=="***Music***":
    sq.question3()

else:
    st.write("")

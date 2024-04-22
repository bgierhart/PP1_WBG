#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 02:31:14 2024

@author: bengierhart
"""

import streamlit as st
from PIL import Image
import season_quiz as sq

st.title("Actors Theatre of Louisville 24-25 Season Quiz")
st.divider()

with st.sidebar:
    st.subheader("Quiz Questions")
    #radio buttons V
    category = st.radio("Choose a category:",
                     ["***Start***","***World Premieres***", "***Community Partnerships***", "***Music***", "***All Ages***", "***Returning Shows***"],
                     captions = ["There's something for everyone in the categories below!","We're known for producing original work no one has seen before, and we're not stopping now.", 
                                 "Why compete when you can collaborate?",
                                 "Musicals, concerts, and more.",
                                 "We welcome all supporters, regardless of age, but these shows are specifically geared toward youth and families.",
                                 "We couldn't rest until we gave you another opportunity to see these programs."])
    


if category=="***Start***":
    col1, col2, col3 = st.columns(3)
    with col2:
        image1 = Image.open("announcement.jpg")
        st.image(image1, width=300, caption="Announcing Actors Theatre of Louisville's 24-25 Season")
    st.write(sq.intro)
    st.write(sq.start)

elif category=="***World Premieres***":
    sq.question1()
    
elif category=="***Community Partnerships***":
    sq.question2()
    
elif category=="***Music***":
    sq.question3()
    
elif category=="***All Ages***":
    sq.question4()
    
elif category=="***Returning Shows***":
    sq.question5()

else:
    st.write("")

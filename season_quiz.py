#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 03:48:38 2024

@author: bengierhart
"""

import streamlit as st
from PIL import Image
import pathlib

intro = "Actors Theatre's 2024–2025 Season uplifts stories and amplifies voices from myriad perspectives to connect with and learn from a diversity of people, ideas, and cultures. In its 50th anniversary year as the State Theatre, Actors Theatre will engage in meaningful community partnerships with fellow arts and service organizations around the region and will continue to share new work, revive relevant classics, and offer exciting experiences as part of the company's Storytelling (r)Evolution."
start = "Please interact with our quiz using the options to the left. It's a fun way to learn about the incredible offerings we have in store for you this season!"

world_premieres = {"A": "Starting on May 31, 2024 and continuing into Pride month, Actors Theatre of Louisville will partner with Drag Daddy Productions on the world premiere of WON'T YOU BE MY MY MAY-BOR? by Andrew Newton Schafflein and Eric Sharp, starring drag performer May O'Nays (Schafflein), and directed by Emily Tarquin, Actors Theatre's Executive Producer and Co-Director of Artistic Programming. In this production, May O'Nays portrays an escape room artist who has conquered every room but one—the elusive Mr. Rogers room. Unlike conventional escape rooms, this experience demands a shift in perspective as solving this puzzle will take patience, mindfulness, and deep listening. This interactive journey, inspired by the teachings of Mr. Rogers, will be a collective exploration of what it truly means to be a good neighbor. WON'T YOU BE MY MAY-BOR? will premiere in the Victor Jory Theater with a special sneak peek supported by the Fund for the Arts, before heading out to Owensboro, Hazard, and other communities throughout Kentucky.",
    "B": "On July 13, please join us at Alberta O. Jones Park for the world premiere of WHO KILLED ALBERTA JONES? by Larry Muhammad. In partnership with the Parks Alliance of Louisville, Actors Theatre of Louisville will present Redline Performing Arts' world-premiere production of this incredible play that tells the story of Alberta Odell Jones, the first Black woman to pass the bar in Kentucky. Jones was a prominent attorney and activist for voting rights, representing both vulnerable and prominent figures like Muhammad Ali. Jones' life was tragically cut short and her murder remains an unsolved case. Following the premiere in the park, the city's newest public green space, there will be several performances in the Victor Jory Theater in August."
}

community_partnerships = {"B": "Actors Theatre is thrilled to engage in a second partnership with Redline Performing Arts in November by presenting their production of THE COLOR PURPLE, based upon the novel by Alice Walker and the Warner Bros./Amblin Entertainment Motion Picture, with a book by Marsha Norman and music and lyrics by Brenda Russell, Allee Willis, and Stephen Bray. THE COLOR PURPLE tells the story of a young African American girl named Celie who lives in rural Georgia in the early 1900s. Deemed inferior in the United States' caste system, Celie encounters racism, sexism, abuse, and challenges to her own sexuality. She perseveres thanks to her relationships with other women, such as her sister Nettie and her lover Shug Avery. Despite the numerous attempts to ban the novel THE COLOR PURPLE, it continues to be a celebrated and powerfully resonant story that Actors Theatre will be proud to share on the stage of the Pamela Brown Auditorium.",
                          "C": "Having been friends and supporters of each other's work for so long, Actors Theatre of Louisville is excited to host Kentucky Shakespeare's winter production of THE IMPORTANCE OF BEING EARNEST, directed by Amy Attaway, current Associate Artistic Director of Kentucky Shakespeare and a former Actors Theatre staff member whom the company is delighted to welcome back to the Pamela Brown Auditorium. Kick off 2025 with Oscar Wilde's 'trivial comedy for serious people,' which explores the hypocrisy of Victorian society and is widely considered his greatest and wittiest achievement."
    }

music = {"A": "On Juneteenth, UNIVERSES will perform a concert selection of works that have been produced at Actors Theatre (Party People, Ameriville, Slanguage) to celebrate and recognize the significant contribution of the global majority and specifically Black communities in our continued societal prosperity while raising awareness of the systems and practices that continue to do harm and sustain oppression. This dynamic event brings back the award-winning ensemble whose roots trace back to theater, poetry, dance, jazz, hip hop, blues and boleros for a kinetic one-night-only performance.",
                          "C": "This December, Actors Theatre of Louisville will illuminate the darkest time of year with HERSCHEL AND THE HANUKKAH GOBLINS—a family-friendly celebration of Hanukkah, the Jewish festival of lights. Impact Producer and Co-Director of Artistic Programming Amelia Acosta Powell will direct this playful, music-filled retelling of a familiar folktale. The production's run will include a series of student matinees as well as daytime and early evening performances. Student matinees receive support from Yum! Brands and permit Actors Theatre of Louisville to subsidize these offerings and aid schools throughout the region in attending.",
                          "D": "In February, get ready to celebrate as Actors Theatre throws another MRS KRISHNAN'S PARTY, presented by New Zealand's Indian Ink Theatre Company, by Jacob Rajan and Justin Lewis. This one-of-a-kind production brought so much joy, energy, and community to the Victor Jory Theater last year that it had to return so that more audiences could experience what unfolds in this surprising and heartfelt celebration of life.",
                          "E": "Actors Theatre will continue THE AFTER SHOW SHOW, a late-night cabaret series hosted by Drag Queens Dusty Ray Bottoms and May O'Nays. Inspired by New York cabarets where Broadway performers sing something from their books after performing in another show, THE AFTER SHOW SHOW offers to keep the party going by inviting local, touring, and youth performers to share their talents and offer a selection of their choosing. Look for dates to be announced following performances at Actors Theatre or Kentucky Performing Arts to extend your night out!"
    }

def question1():
    st.header("Which world premiere do you want to see?")
    st.write("A. I want to see something unique and interactive.")
    st.write("B. I want to learn something more people should know about Louisville history.")
    selection = st.text_input("Please enter the letter corresponding to your selection:")
    upper_selection = selection.upper()
    if upper_selection == "A":
        col1, col2, col3 = st.columns(3)
        with col2:
            image2 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/May-bor.jpg'))
            st.image(image2, width=300, caption="World Premiere: Drag Daddy Productions Presents WON'T YOU BE MY MAY-BOR?")
        st.write(world_premieres[upper_selection])
        st.page_link("https://www.dragdaddy.pro/", label="Click here to learn about Drag Daddy Productions!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
    
    elif upper_selection == "B":
        col1, col2, col3 = st.columns(3)
        with col2:
            image3 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/Alberta.jpg'))
            st.image(image3, width=300, caption="World Premiere: Redline Performing Arts in Partnership with the Parks Alliance of Louisville Presents WHO KILLED ALBERTA JONES?")
        st.write(world_premieres[upper_selection])
        st.page_link("https://www.redlineperformingarts.com/", label="Click here to learn about Redline Performing Arts!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
        
    else:
        st.write("Choose A or B!")
        
def question2():
    st.header("Are you a fan of one of these other theater companies in town? See what they're doing with us at ATL this year!")
    st.write("A. Drag Daddy Productions.")
    st.write("B. Redline Performing Arts.")
    st.write("C. Kentucky Shakespeare.")
    selection = st.text_input("Please enter the letter corresponding to your selection:")
    upper_selection = selection.upper()
    if upper_selection == "A":
        col1, col2, col3 = st.columns(3)
        with col2:
            image2 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/May-bor.jpg'))
            st.image(image2, width=300, caption="World Premiere: Drag Daddy Productions Presents WON'T YOU BE MY MAY-BOR?")
        st.write(world_premieres[upper_selection])
        st.page_link("https://www.dragdaddy.pro/", label="Click here to learn about Drag Daddy Productions!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
        
    
    elif upper_selection == "B":
        option = st.selectbox(
   "Select an option:",
   ("WHO KILLED ALBERTA JONES?", "THE COLOR PURPLE"),
   index=None,
   placeholder="Select a show...",
)
        if option == "WHO KILLED ALBERTA JONES?":
            col1, col2, col3 = st.columns(3)
            with col2:
               image3 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/Alberta.jpg'))
               st.image(image3, width=300, caption="World Premiere: Redline Performing Arts in Partnership with the Parks Alliance of Louisville Presents WHO KILLED ALBERTA JONES?")
            st.write(world_premieres[upper_selection])
            st.page_link("https://www.redlineperformingarts.com/", label="Click here to learn about Redline Performing Arts!")
            st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
        elif option == "THE COLOR PURPLE":
            col1, col2, col3 = st.columns(3)
            with col2:
               image4 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/ColorPurple.jpg'))
               st.image(image4, width=300, caption="Redline Performing Arts Presents THE COLOR PURPLE")
            st.write(community_partnerships[upper_selection])
            st.page_link("https://www.redlineperformingarts.com/", label="Click here to learn about Redline Performing Arts!")
            st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
        else:
            st.write("")
        
    elif upper_selection == "C":
        col1, col2, col3 = st.columns(3)
        with col2:
            image5 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/Earnest.jpg'))
            st.image(image5, width=300, caption="Presented by Kentucky Shakespeare: THE IMPORTANCE OF BEING EARNEST")
        st.write(community_partnerships[upper_selection])
        st.page_link("https://kyshakespeare.com/", label="Click here to learn about Kentucky Shakespeare!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
        
    else:
        st.write("Choose A, B, or C!")
        
def question3():
    st.header("What kind of musical experience are you looking for?")
    st.write("A. I want to hear world-class talent perform jazz, hip hop, blues and boleros.")
    st.write("B. I'm a fan of Broadway musicals.")
    st.write("C. What about something I can bring my kids to?")
    st.write("D. Music makes me want to dance, and dancing makes me hungry...")
    st.write("E. I'm more in the mood for something campy and fun.")
    selection = st.text_input("Please enter the letter corresponding to your selection:")
    upper_selection = selection.upper()
    if upper_selection == "A":
        col1, col2, col3 = st.columns(3)
        with col2:
            image6 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/Universes.jpg'))
            st.image(image6, width=300, caption="A Juneteenth Celebration UNIVERSES in Concert")
        st.write(music[upper_selection])
        st.page_link("https://www.universesonstage.com/", label="Click here to learn about UNIVERSES!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
    
    elif upper_selection == "B":
        col1, col2, col3 = st.columns(3)
        with col2:
            image4 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/ColorPurple.jpg'))
            st.image(image4, width=300, caption="Redline Performing Arts Presents THE COLOR PURPLE")
        st.write(community_partnerships[upper_selection])
        st.page_link("https://www.redlineperformingarts.com/", label="Click here to learn about Redline Performing Arts!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
   
    elif upper_selection == "C":
        col1, col2, col3 = st.columns(3)
        with col2:
            image7 = Image.open(pathlib.Path('/Users/bengierhart/Desktop/PP1_WBG/Herschel.png'))
            st.image(image7, width=300, caption="Redline Performing Arts Presents THE COLOR PURPLE")
        st.write(community_partnerships[upper_selection])
        st.page_link("https://www.redlineperformingarts.com/", label="Click here to learn about Redline Performing Arts!")
        st.page_link("https://www.actorstheatre.org/archive/2024-2025-season-announcement/", label="Click here to learn about the rest of our season!")
    else:
        st.write("Choose A, B, C, D, or E!")

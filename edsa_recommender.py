"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#getting images from imdb database

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

#Code to ensure the app will cover the whole width of website page
#and scale dynamically.
#must always be at the start of the code
st.set_page_config(layout="wide")

## adding page background

# def add_bg_from_url():
#     st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background-image: url("https://besthqwallpapers.com/Uploads/13-12-2021/187550/4k-black-3d-shards-blue-neon-light-geometric-shapes-creative.jpg");
#                 background-size: cover
#                 background-position: centre
#                 background-repeat: no-repeat
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )

# add_bg_from_url()

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Creates a main title and subheader on your page -
# these are static across all pages
st.title("MOVIE RECOMMENDER")
st.subheader("For the best Time of Your Life")

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

    sbar = st.sidebar
    chk1 = sbar.button("Discover")
    chk2 = sbar.button("Browse")
    chk3 = sbar.button("Charts")
    chk4 = sbar.button("About the App")
    chk5 = sbar.button("Under the Hood")
    chk6 = sbar.button("The Team")
    page_options = ["Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------

    
    


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    if chk2:
        page_selection = st.radio("",page_options)
        if page_selection == "Recommender System":
            # Header contents
            st.write('# Movie Recommender Engine')
            st.write('### EXPLORE Data Science Academy Unsupervised Predict')
            st.image('resources/imgs/Image_header.png',use_column_width=True)
            st.image('resources/imgs/Image_header.png',use_column_width=True)
            # Recommender System algorithm selection
            sys = st.radio("Select an algorithm",
                            ('Content Based Filtering',
                            'Collaborative Based Filtering'))

            # User-based preferences
            st.write('### Enter Your Three Favorite Movies')
            movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
            movie_2 = st.selectbox('Second Option',title_list[25055:25255])
            movie_3 = st.selectbox('Third Option',title_list[21100:21200])
            fav_movies = [movie_1,movie_2,movie_3]

            # Perform top-10 movie recommendation generation
            if sys == 'Content Based Filtering':
                if st.button("Recommend"):
                    try:
                        with st.spinner('Crunching the numbers...'):
                            top_recommendations = content_model(movie_list=fav_movies,
                                                                top_n=10)
                        st.title("We think you'll like:")
                        for i,j in enumerate(top_recommendations):
                            st.subheader(str(i+1)+'. '+j)
                    except:
                        st.error("Oops! Looks like this algorithm does't work.\
                                    We'll need to fix it!")


            if sys == 'Collaborative Based Filtering':
                if st.button("Recommend"):
                    try:
                        with st.spinner('Crunching the numbers...'):
                            top_recommendations = collab_model(movie_list=fav_movies,
                                                                top_n=10)
                        st.title("We think you'll like:")
                        for i,j in enumerate(top_recommendations):
                            st.subheader(str(i+1)+'. '+j)
                    except:
                        st.error("Oops! Looks like this algorithm does't work.\
                                    We'll need to fix it!")
        
        if page_selection == "Solution Overview":
            page_selection = st.radio("",page_options)
            st.title("Solution Overview")
            st.write("Describe your winning approach on this page")

    #if chk3:

    #if chk4:

    #if chk5:

    if chk6:
        team_mates = ["Rogers Mugambi", "Denis Titus", "Frank Ayensu","Cosmus Mutuku","Peter Sumani","Emmanuel"]
        roles = ["Team Lead","Presentation Lead","Asst. Presentation Lead","Communication Lead","Technical Lead","Member"]
        bio = ["qwerty", "qwerty", "qwerty", "qwerty", "qwerty","qwerty"]
        image_link = ['resources/imgs/team_pics/placeHolder.png',
                        'resources/imgs/team_pics/placeHolder.png',
                        'resources/imgs/team_pics/placeHolder.png',
                        'resources/imgs/team_pics/placeHolder.png',
                        'resources/imgs/team_pics/placeHolder.png',
                        'resources/imgs/team_pics/placeHolder.png']
        theTeam = {'people':team_mates,
                    'role':roles,
                    'bio':bio,
                    'imageLink':image_link}
        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][0]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][0]} -- {theTeam['role'][0]}{chr(10)}")
            st.write(theTeam['bio'][0])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][1]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][1]} -- {theTeam['role'][1]}{chr(10)}")
            st.write(theTeam['bio'][1])
        
        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][2]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][2]} -- {theTeam['role'][2]}{chr(10)}")
            st.write(theTeam['bio'][2])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][3]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][3]} -- {theTeam['role'][3]}{chr(10)}")
            st.write(theTeam['bio'][3])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][4]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][4]} -- {theTeam['role'][4]}{chr(10)}")
            st.write(theTeam['bio'][4])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][5]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][5]} -- {theTeam['role'][5]}{chr(10)}")
            st.write(theTeam['bio'][5])
    #if chk7:

    #if chk8:

    elif chk1:
        # creating columns that will enable 
        # orderly arrangement of movie images
        col1, col2, col3, col4, col5 = st.columns(5, gap = "small")
        # assigning content to a column
        with col1:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

            #--------
            # adjusting the font
            #1. Creating a slider
            #--------
            #font_size = st.slider("Enter a font size", 1, 300, value=1)
            #html_str = f"""
            #<style>
            #p.a {{
            #font: regular 0.5px Ariel;
            #}}
            #</style>
            #<p class="a">{movie_name}</p>
            
            #st.markdown(html_str, unsafe_allow_html=True)
            #st.write(release_year)
            #st.write("Rating: ",avg_rating)
        # you can have several items in a column
        # they will be arranged vertically
        with col2:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col3:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col4:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col5:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        col6, col7, col8, col9, col10 = st.columns(5, gap = "small")
        with col6:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col7:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col8:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col9:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col10:
            link = 'resources/imgs/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")


if __name__ == '__main__':
    main()

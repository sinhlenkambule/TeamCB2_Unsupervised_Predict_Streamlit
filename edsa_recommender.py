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
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import toml
import time

from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu 
from PIL import Image

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# This command allows the app to use wide mode of the screen.
# st. set_page_config(layout="wide")


# Use local CSS to sort the styling of the contact form
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# Function to access the json files of the lottie animations
def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Visualisations", "Solution Overview", "Meet the Team", "Contact us"]
    
    logo = Image.open("images/Astro_Coders1.png")
    st.sidebar.image("images/Astro_Coders1.png", use_column_width=True)

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
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
                    # st.title("We think you'll like:")
                    st.success("##### We think you'll like:")
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


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        
        st.subheader("Our winning approach")

        st.write("""One of the main strategies used by businesses to improve the user experience for users on their platforms is the use of recommender systems.
         Major corporations like Netflix, HBO, Amazon, Youtube, and Facebook have invested millions of dollars to enhance user experience and content delivery 
         in order to increase user growth, boost customer retention, and draw more publishers to their platforms. 
         To accomplish this, each of these businesses uses a recommender system.
        """)

        st.subheader("Content Based Filtering VS Collaborative Filtering")
        st.write("There are primarily two methods for developing a recommender system. We experimented with both collaborative filtering and content-based filtering to see which approach would produce the greatest results for our system.")
        
        logo = Image.open("images/contentVScollab1.png")
        st.image("images/contentVScollab2.png")

        st.info("##### Content Based Filtering")
        st.markdown("""The available descriptive data for a certain item or product serves as the foundation for the content-based filtering strategy. 
        This approach will examine products with comparable descriptions and make recommendations based on that. 
        Finding products that match the user's historical tastes takes into account their earlier preferences. 
        For instance, if a person enjoys watching Toy Story, they will be sent suggestions for other Pixar films and other shows that are quite similar to it.
        """)

        st.info("##### Collaborative Filtering")
        st.write("""By filtering recommendations for a user based on the opinions of other users who share similar interests, 
        the Collaborative Filtering technique produces recommendations that were gathered and produced by many users rather than just one. 
        This approach makes use of a huge user base and searches for subsets of users who share a specific user's tastes. 
        It will give the user access to a greater variety of content and base recommendations on how similar their interests are.
        A fairly common technique for movie recommendation systems is collaborative filtering, which was made simple to utilize by the wealth 
        of information available on it. Due to its widespread use and comparatively simple operation, it also makes straightforward maintenance 
        and ongoing customization possible. Additionally, it performs better than the Content Based Filter because it uses less processing power.
        """)

        st.success("##### Winner: ")
        st.write("Use this section to describe our winning algorithm")
        

        st.info("##### Why we believe our Recommender System is the best in the market! ")
       



    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # if page_selection == "Visualisations":
    if page_selection == "Visualisations":
        st.title("Visualisations")
        st.write("We will use this section for graphs found during EDA process")


    # Building the "Meet the Team" page
    if page_selection == "Meet the Team":
        st.title("Meet the Team!")
        

        left_column, right_column = st.columns(2)
        with left_column:
            st.info("##### Astro Coders")
            st.write(""" 
                    An organization based in Southern Africa with a passion for problem solving through the use of our team's unique skill set.
                    Astro Coders, founded in 2020 during the outbreak of Covid19, is one of Africa's largest IT and business consulting firms.
                    We are insight-driven and outcome-driven to help accelerate returns on your IT and business investments. 
                    Through personal client relationships and the provision of industry and technological expertise to assist you in meeting the needs of your customers and citizens, it is our mission to establish confidence in all we do.
        
            """)

        with right_column:
            # Loading the animation in the "Get in touch with us!" section.
            # st.write("Get a different animation for the team section")
             contact_animation = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_zqndq8mg.json")
             st_lottie(contact_animation, height=300, key="coding")


        # Details of the team
        with st.container():
            st.info("##### Connect with us!")
            st.caption("### Chad Brache")
            st.write("""Supervisor
                    \nchad.brache@astrocoders.co.za""")
            
            st.write("---")

            left_column, right_column = st.columns(2)
            with left_column:
                st.caption("### Ozzey Padayachee")
                st.write("""Chief Executive Officer
                    \nozzey.padayachee@astrocoders.co.za""")
                        
                st.caption("### Sinhle Nkambule")
                st.write("""Web App Developer
                    \nsinhle.nkambule@astrocoders.co.za""")

                st.caption("### Nhlanhla Ngwenya")
                st.write("""Machine Learning Engineer
                    \nnhlanhla.ngwenya@astrocoders.co.za""")
        
            with right_column:
                st.caption("### Promise Lamola")
                st.write("""Data Science Manager
                    \npromise.lamola@astrocoders.co.za""")

                st.caption("### Samuel Mnisi")
                st.write("""Senior Data Analyst
                    \nsamuel.mnisi@astrocoders.co.za""")					  

                st.caption("### Sinethemba Nongqoto")
                st.write("""Data Scientist
                    \nsinethemba.nongqoto@astrocoders.co.za""")



    if page_selection == "Contact us":
        st.title("Contact us!")
        # Contact form for queries.
        with st.container():
                st.info("Send your query using the form below:")

                # Documention: https://formsubmit.co/
                contact_form =( """
                <form action="https://formsubmit.co/sinhlenkambule78@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here" required></textarea>
                    <button type="submit">Send</button>
                </form>
                """)

        left_column, right_column = st.columns(2)
        with right_column:
            # st.write("Lottie file will come in this section")
            # Loading the animation in the "Get in touch with us!" section.
            contact_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_isbiybfh.json")
            st_lottie(contact_animation, height=300, key="coding")
        
        
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)

        st.write("---")	

		
		

if __name__ == '__main__':
    main()

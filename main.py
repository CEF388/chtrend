import streamlit as st
import xml.etree.ElementTree as et
import sqlitecloud
import sqlite3
import requests
from datetime import date

from google import genai
from pydantic import BaseModel


ara=st.text_input("Haberler içinde arama yap")


conn=sqlitecloud.connect('sqlitecloud://cgi896obnk.g5.sqlite.cloud:8860/chinook.sqlite?apikey=6gaa4nSztoaj9w4PCaVOIMgos4bNzOfLQyrHkeLsuho')
c=conn.cursor()


if len(ara)>1:
    c.execute(f"SELECT * FROM haberler WHERE baslik LIKE '½{ara}½' ORDER BY trend_id DESC LIMIT 99")
    
else:
    c.execute("SELECT * FROM haberler ORDER BY trend_id DESC LIMIT 99")
    
haberler=c.fetchall()

for i in range(0,len(haberler),3):
    col1,col2,col3=st.columns(3)

    with col1:
        st.image(haberler[i][3])
        st.write(haberler[i][1])
        st.link_button("Habere Git",haberler[i][2])
    with col2:
        if i+1 < len(haberler):
            st.image(haberler[i+1][3])
            st.write(haberler[i+1][1])
            st.link_button("Habere Git", haberler[i+1][2])
        else:
            pass
    with col3:
        if i+2 < len(haberler):
            st.image(haberler[i+2][3])
            st.write(haberler[i+2][1])
            st.link_button("Habere Git", haberler[i+2][2])
        else:
            pass

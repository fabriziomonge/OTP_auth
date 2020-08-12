#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st

# number = input("inserire il proprio numero di cellulare per autenticazione") #jupytercode

number = st.text_input("inserire il proprio numero di cellulare per autenticazione", "4") #streamlit code

number = "0039"+number

if number != "00394":
    

    # generate random integer values
    from random import seed
    from random import randint
    # seed random number generator
    
    # generate some integers

    value = randint(1000, 9999)
    value = str(value)

    from textmagic.rest import TextmagicRestClient
  
    username = "fabriziomonge"
    token = "FXYszXlUIdZKW3xVC8da90mTm30RME"
    client = TextmagicRestClient(username, token)
    # weYT0IOJ1c api password
  
    message = client.messages.create(phones=number, text=value)

PSW = st.text_input("Inserire il codice ricevuto tramite sms") #streamlit code
# PSW = input("Inserire il codice ricevuto tramite sms") #jupytercode

if PSW == value:
#     print("Autenticazione riuscita") #jupytercode
    
    st.write("""
    # Autenticazione effettuata.
    """) #streamlit code
    
    autorizzazione = "OK"
    
else:
#     print("Autenticazione fallita!") #jupytercode

    st.write("""
    # Autenticazione fallita.
    """) #streamlit code
    
    autorizzazione = "NO"

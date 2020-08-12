#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from textmagic.rest import TextmagicRestClient
from random import seed
from random import randint
username = "fabriziomonge"
token = "FXYszXlUIdZKW3xVC8da90mTm30RME"
client = TextmagicRestClient(username, token)

# number = input("inserire il proprio numero di cellulare per autenticazione") #jupytercode

number = st.text_input("inserire il proprio numero di cellulare per autenticazione", "4") #streamlit code

number = "0039"+number

if number != "00394":
    
  
    try:
        if generator == "OFF":
            value = value
            st.write("generator è uguale a off")
            
        else:

            value = randint(1000, 9999)
            value = str(value)
            message = client.messages.create(phones=number, text=value)
            PSW = st.text_input("Inserire il codice ricevuto tramite sms", "in attesa") #streamlit code
            generator = "OFF"
            st.write("generator è diverso da off")            
            
    except:
            value = randint(1000, 9999)
            value = str(value)
            message = client.messages.create(phones=number, text=value)
            PSW = st.text_input("Inserire il codice ricevuto tramite sms", "in attesa") #streamlit code
            st.write("ti trovi nella eccezione del try")
            generator = "OFF"
            
else:
    
    value = "2"


if value != "2":
    
    # PSW = input("Inserire il codice ricevuto tramite sms") #jupytercode
    
    if PSW == "in attesa":
        st.write("""
        # In attesa del codice
        """) #streamlit code
        
    else:
                
        if PSW == value:
#       print("Autenticazione riuscita") #jupytercode
    
            st.write("""
            # Autenticazione effettuata.
            """) #streamlit code
    
            autorizzazione = "OK"
            generator = "OFF"
    
        else:
#       print("Autenticazione fallita!") #jupytercode

            st.write("""
            # Autenticazione fallita.
            """) #streamlit code
    
            autorizzazione = "NO"
            generator = "OFF"

            
try:
    st.write(generator)
    st.write(PSW)
    st.write(value)
    st.write(type(PSW))
    st.write(type(value))
    st.write(number)
except:
    st.write("dati incompleti")


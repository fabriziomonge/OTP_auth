import streamlit as st
from textmagic.rest import TextmagicRestClient
from random import seed
from random import randint
username = "fabriziomonge"
token = "FXYszXlUIdZKW3xVC8da90mTm30RME"
client = TextmagicRestClient(username, token)

inizio = 1000

fine = 9999


# number = input("inserire il proprio numero di cellulare per autenticazione") #jupytercode

number = st.text_input("inserire il proprio numero di cellulare per autenticazione", "4") #streamlit code

number = "0039"+number

@st.cache
def generator(inizio,fine,number):
    
    value = randint(inizio, fine)
    value = str(value)
    message = client.messages.create(phones=number, text=value)
    
    return value, message

value=generator(inizio,fine,number)[0]

if number != "00394":
    
    PSW = st.text_input("Inserire il codice ricevuto tramite sms", "in attesa")
    
    if PSW == "in attesa":
        st.write("In attesa del codice di conferma")
    else:
        if PSW == value:
            
            st.write("Convalidato")
        else:
            
            st.write("Accesso negato")
    

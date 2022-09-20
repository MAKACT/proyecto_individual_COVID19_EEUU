'''IMPORTANTE: para lograr visualizar esto de forma correcta en el local solo abre tu terminal y ejecuta los siguiente,
streamlit run main_page.py si alguna de las librerias que contine se remarca bastara con colocarte sobre ella y
 seleccionar la opcion que te permite instalarla o tambien ir  a la terminal y colocar pip install nombrelibreria '''
# importamos las librerias

import streamlit as st


header = st.container()
dataset = st.container()
with header:
    st.title('Actividad Hospitalaria en Estados Unidos de América durante la pandemia por COVID-19 ')
    st.write('Periodo 01-01-2020 a 01-08-2022')















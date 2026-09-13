import streamlit as st

st.title("Una Pregunta Para Ti:")

respuesta = st.text_input ("Quires Ser Mi Novia?(SI/NO)").strip().upper()

if respuesta == "SI":
    st.balloons()
    st.success("Gracias Por Hacerme Parte de Tu Vida. Te amo!!")
    st.write("Dare todo lo mejor de mi")
elif respuesta == "NO":
    st.error("Okey No Hay Problema")

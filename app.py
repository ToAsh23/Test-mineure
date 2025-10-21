import streamlit as st

st.title("Bonjour à tous !")

st.write('Mineure numérique')

nombre = [1,2,3,4]
carre = [1**1,2**2,3**3,4**4]

d = {"nombre :" nombre, "carré:" carre}

data = pd.DataFrame (d)

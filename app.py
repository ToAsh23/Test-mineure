import streamlit as st
import pandas as pd
st.title("Bonjour à tous !")

st.write('Mineure numérique')

nombre = [1,2,3,4]
carre = [1**1,2**2,3**3,4**4]

d = {"nombre" : nombre, "carré": carre}

data = pd.DataFrame (d)
st.header("Premier exemple")
st.write("Voici un DataFrame de nombre et leur carré par elle même :")
st.dataframe(data)

# Créer un exemple de DataFrame
df = pd.DataFrame({
    'colonne 1': [1, 2, 3, 4],
    'colonne 2': [10, 20, 30, 40]
})

st.header("Affichage de Données")
st.write("Voici un DataFrame :")
st.dataframe(df) # Affiche une table interactive

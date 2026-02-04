import streamlit as s
import math as m

#Titel
s.title("Mijn Eerste Streamlit App")

#Tekst
s.write("Welkom, bereken hier je getal in een kwadraat")

#Slider
x = s.slider("Kies een getal", 0, 100)

#Output
s.write(f"Het kwadraat van de variabele {x} is {x**2}")
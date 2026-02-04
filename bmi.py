import streamlit as s
import math as m

#Titel
s.title("Mijn Eerste Streamlit App")

#Tekst
s.write("Welkom, bereken hier je bmi")

#Slider
x = s.slider("Kies een getal", 0, 100)
g = s.slider("Hoeveel weeg je (in kg)? ", 0, 120)
l = s.slider("Hoe groot ben je (in cm)? ", 0, 220)


#Output
bmi = g / (l**2)
s.write(f"De BMI van {g} KG en een grootte van {h} cm is {bmi}")
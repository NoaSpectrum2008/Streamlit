import streamlit as s
import math as m

# Titel
s.title("Mijn Eerste Streamlit App")

# Tekst
s.write("Welkom, bereken hier je BMI")

# Sliders
g = s.slider("Hoeveel weeg je (in kg)?", 1, 120)
l_cm = s.slider("Hoe groot ben je (in cm)?", 50, 220)

# Omrekenen naar meters
l = l_cm / 100

# Berekening
bmi = g / (l ** 2)

# Output
s.write(f"De BMI bij {g} kg en een lengte van {l_cm} cm is **{bmi:.2f}**")

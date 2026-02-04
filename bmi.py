import streamlit as s
import math as m

s.title("BMI calculator")

g = s.slider("Gewicht (kg)", 1, 120)
l = s.slider("Lengte (m)", 0.5, 2.5)

bmi = g / (l ** 2)
bmi = round(bmi, 1)
s.write(bmi)


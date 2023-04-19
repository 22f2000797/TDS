# -*- coding: utf-8 -*-
import streamlit as st

st.write("# Largest Number")
st.write("This app finds the largest among the 3 given numbers")

numA = st.number_input("Insert the first number **A**")
numB = st.number_input("Insert the second number **B**")
numC = st.number_input("Insert the third number **C**")

largest = max(numA, numB, numC)

st.write("The largest of the three numbers is")
st.write(f"#${largest}")

import streamlit as st
import time

st.header("Hello")

st.sidebar.title("Configuraion")
with st.sidebar:
    shape = st.selectbox("Choose Shape", ["Circle", "Rectangle"])

print(shape)
area = 0.0
perimeter = 0.0
if shape == "Circle":
    radius = st.number_input("Radius", min_value=0.0, max_value=100.0, step=0.1)
    area = radius * radius * 3.14
    perimeter =  2 * radius * 3.14
elif shape == "Rectangle":
    length = st.number_input("Length", min_value=0.0, max_value=100.0, step = 0.1)
    width = st.number_input("Width", min_value=0.0, max_value=100.0, step = 0.1)
    area = length * width
    perimeter =  2 * (length + width)

compute_btn = st.button("Compute Area and Perimeter")
if compute_btn:
    with st.spinner("Computing..."):
        time.sleep(1)
        st.write("Area: ", area)
        st.write("Perimeter", perimeter)
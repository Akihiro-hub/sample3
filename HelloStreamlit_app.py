import streamlit as st
st.title("Análisis del punto de equilibrio")
a = st.number_input("Precio unitario para la venta")
b = st.number_input("Costo variable unitario")
c = st.number_input("Todos los costos fijos al mes")
d = st.number_input("Meta de ganancia al mes")

st.title("Venta necesaria para la meta")
st.text((c+d)/((a-b)/a))

st.title("Venta al punto de equilibrio")
st.text(c/((a-b)/a))
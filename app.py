import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
fig = px.histogram(car_data, x="odometer") 
fig.show()

car_data = pd.read_csv('vehicles_us.csv')
fig = px.scatter(car_data, x="odometer", y="price") 
fig.show()

st.header('Graficos para anuncios de venta de coches')

hist_button = st.button('Construir histograma')
        
if hist_button: 
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            fig = px.histogram(car_data, x="odometer")     
            st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de disperción')

if scatter_button:
        st.write('Creacion de un gráfico de disperción para el conjunto de datos de anucios de venta de coches')
        fig = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig,use_container_width=True)

        

import pandas as pd
import streamlit as st
import plotly.express as px
st.header('Anuncios de ventas de coches')

        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
    if hist_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
        # crear un histograma
        fig = px.histogram(car_data, x="odometer", color='condition') 
        
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
    
    # crear una casilla de verificación
build_scatter = st.checkbox('Construir el gráfico de disperción')

    if build_scatter: # si la casilla de verificación está seleccionada
        #Escribir un mensaje
        st.write('Construir un grafico de disperción utilizando la columna odómetro y precio')
        
        #Crear un gráfico de disperción
        fig1 = px.scatter(car_data, x="odometer", y="price", color='model_year') # crear un gráfico de dispersión

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig1, use_container_width=True)

import pandas as pd
import streamlit as st
from utils.data_processing import clean_data
from utils.visualization import plot_fuel_type_count, plot_price_distribution

#Cargar achivo desde fuente
df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')

#Limpiar los datos
df = clean_data(df)

#Título y descripción de la app
st.title('Análisis descriptivo de vehículos')
st.write(
    'Esta aplicación permite explorar un dataset de vehículos, proporcionando estadísticas y visualizaciones intercativas.'
)

#Mostrar el resumen estadístico
tabla_resumen = df.describe()
st.write('## Resumen Estadístico de los Datos')
st.dataframe(tabla_resumen)

#Generar y mostrar gráficos
fig1 = plot_price_distribution(df)
st.pyplot(fig1)

fig2 = plot_fuel_type_count(df)
st.pyplot(fig2)

#Input para seleccionar una marca de vehículo
selected_brand = st.selectbox('Selecciona una marca de vehículo para filtrar los datos:',
                              df['brand'].unique())
df_filtered = df[df['brand'] == selected_brand]

if df_filtered.empty:
    st.write('Ingrese un valor adecuado')
else:
    st.write(f'### Datos filtrados para la marca {selected_brand}')
    st.dataframe(df_filtered.describe())
    fig_filtered = plot_fuel_type_count(df_filtered)
    st.pyplot(fig_filtered)
        

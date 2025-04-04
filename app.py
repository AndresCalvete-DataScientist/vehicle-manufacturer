import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de vehículos usados')
st.subheader('Usa el botón para construir un histograma y selecciona en las casillas que otros graficos de apoyo deseas construir.')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# crear un botón para construir un histograma
build_plots = st.button('Construir diagramas')  # crear un botón

st.write('Selecciona los gráficos de apoyo que deseas construir')

# crear casillas de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión.')
build_boxplot = st.checkbox('Construir un diagrama de caja.')


if build_plots:  # al hacer clic en el botón

    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')

    # Histograma de distribución del kilometraje.
    fig = px.histogram(car_data, x="odometer")  # crear un histograma

    # Dando forma al gráfico.
    fig.update_layout(
        title={
            'text': 'Distribución del kilometraje',
            'x': 0.5,  # Centrar el título
            'xanchor': 'center'
        },
        xaxis_title='Kilometraje (Millas)',
        yaxis_title='Número de vehiculos',
        xaxis=dict(range=[0, 500000]),  # Establecer el rango del eje x
        yaxis=dict(range=[0, 700])  # Establecer el rango del eje y
    )

    # mostrar histograma Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    if build_scatter:  # si la casilla de verificación está seleccionada
        st.write(
            'Diagrama de dispersiión para el conjunto de datos de anuncios de venta de coches')

        # Dispersión entre precio y kilometraje.
        # crear un gráfico de dispersión
        fig = px.scatter(car_data, x="odometer", y="price")

        # Dando forma al gráfico.
        fig.update_layout(
            title={
                'text': 'Relación entre precio y kilometraje',
                'x': 0.5,  # Centrar el título
                'xanchor': 'center'
            },
            xaxis_title='Kilometraje (Millas)',
            yaxis_title='Precio (USD)',
            # Establecer el rango del eje x
            xaxis=dict(range=[-10000, 1000000]),
            yaxis=dict(range=[0, 200000])  # Establecer el rango del eje y
        )

        st.plotly_chart(fig, use_container_width=True)

    if build_boxplot:  # si la casilla de verificación está seleccionada
        st.write(
            'Diagrama de caja para el conjunto de datos de anuncios de venta de coches')

        # Definir el orden de las categorías
        category_order = ['new', 'like new',
                          'excellent', 'good', 'fair', 'salvage']

        # Convertir la columna a tipo categórico con el orden especificado
        car_data['condition'] = pd.Categorical(
            car_data['condition'], categories=category_order, ordered=True)

        # Realizion entre precio y kilometraje.
        fig = px.box(car_data, x="price", y="condition", color="condition",
                     category_orders={"condition": category_order})

        # Dando forma al gráfico.
        fig.update_layout(
            title={
                'text': 'Distribución de precios por condición del vehiculo',
                'x': 0.5,  # Centrar el título
                'xanchor': 'center'
            },
            xaxis_title='Precio (USD)',
            yaxis_title='Condición del vehiculo',
            xaxis=dict(range=[-1000, 200000])  # Establecer el rango del eje y
        )

        st.plotly_chart(fig, use_container_width=True)

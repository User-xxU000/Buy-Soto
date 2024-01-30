import streamlit as st
st.set_page_config(page_title="Serial Codes Secrets of the Obscure Buy Now")


st.title("""Secrets of the Obscure - Standard Edition - Serial Codes""")
#layouts

col1,col2,col3 = st.columns(3)
with col3:
    st.subheader("""Secrets of the Obscure -Serial Codes""",)

st.markdown(
    "<style> img { border-radius: 10px; transition: transform 0.3s; } img:hover { transform: translateY(-5px); } </style>", 
    unsafe_allow_html=True
)

with col1:
    image = st.image("Photogame.jpg", width=440)



with col3:
    st.markdown("""

                Details Of This Product: 

                Launch date : 22/06/2023
                
                Product Type : Game Membership
                
                Price : 13.99""")


# Definir el estilo CSS para el botón redondo
css = """
<style>
.boton-redondo {
  display: inline-block;
  padding: 10px 20px;
  background-color: #2e518b;
  color: #ffffff;
  text-decoration: none;
  text-transform: uppercase;
  font-family: 'Helvetica', sans-serif;
  border-radius: 25px; /* Bordes redondos para crear un aspecto moderno */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra para un efecto tridimensional */
  transition: all 0.3s ease; /* Transición suave al interactuar con el botón */
}

.boton-redondo:hover {
  transform: translateY(-2px); /* Efecto de elevación al pasar el cursor sobre el botón */
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2); /* Sombra más pronunciada al interactuar con el botón */
}
</style>
"""

# Agregar el estilo CSS al documento
st.markdown(css, unsafe_allow_html=True)
with col3:
    st.write('<a href="https://making-a-purchase-order.onrender.com" class="boton-redondo">Buy Now</a>', unsafe_allow_html=True)
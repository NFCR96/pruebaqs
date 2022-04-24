import streamlit as st
option = st.selectbox(
     'Presentas alguno de estos sintomas?',
     ('Llagas', 'Hinchazon', 'Berrugas', 'Irritacion o Enrojecimiento'))
if 'Llagas' in option:
     st.write('Las Llagas son uno de los sintomas carcaterisiticos de la sifilis; La Silifis es una infeccion bacteriana causada por Treponema pallidum, la principal causa de trasnmision es por Contacto Sexual con alguna persona infectada, pero tambien y de fomra menos comun ,es mediente el contacto con una lesion activa como las que se podrian presentar en la boca y al darse un beso se transmitiria, tambien existe la probabilidad de trasnmision de madre a hijo durante el embarazo o parto,todo esto mediente el contacto de las llagas con la piel o membranas mucosas. Aunque es de condsideracion señalar que no es probable que se contagie mendiente el uso de tasas de baño, ropa, piciinas, jacuzzis por mencionar algunos ejemplos. Los sintomas mas comunes es la aparicion de Llagas indoloras en boca, recto o genitales . ¿El tratamiento? es simple existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiotico recomendado por tu medico, en este caso en caso de presentar algun sintoma acude inmenditamente con tu medico, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a organos como el corazon o cerebro incluso algunos otros. ¡POR FAVOR, CHECATE!')
   

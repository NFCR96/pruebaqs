import streamlit as st
option = st.selectbox(
     'Presentas alguno de estos sintomas?',
     ('Enrojecimiento', 'Picazon', 'Dolor'))
if 'Picazon' in option:
     st.write('bebe panda')
   

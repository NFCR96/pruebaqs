import streamlit as st
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
if 'Email' in option:
     st.write('cual es tu email')
   

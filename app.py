import streamlit as st


st.title('Bienvenido a Sexuapp')
if 'num' not in st.session_state:
    st.session_state.num = 0

choices1 = ['Cisgénero', 'Crossdresser', 'Drag king', 'Drag queen', 'Disforia de género', 'Fluidez de género', 'género no binario', 'Genderqueer ', 'Intersexual', 'Transgénero', 'Hombre transgénero', 'Mujer transgénero ', 'Gay', 'Inconformidad de género', 'Lesbiana', 'Intersexual', 'Poliamoroso', 'Femenino', 'Masculino', 'Chico', 'Chica', 'Tomboy', 'Hombre joven', 'Mujer joven', 'Hombre transexual', 'Mujer transexual',
 'Bigénero', 'Intersexual', 'Sin género', 'No estoy seguro', 'Prefiero no decir', 'Otro']



qs1 = [('Cual es tu genero?', choices1),
    ('sexo biologico', choices1),
    ('sexo biologico', choices1)]



def main():
    for _ in zip(qs1): 
        placeholder = st.empty()
        num = st.session_state.num
        with placeholder.form(key=str(num)):
            st.radio(qs1[num][0], key=num+1, options=qs1[num][1])

                      
            if st.form_submit_button():
                st.session_state.num += 1
                if st.session_state.num >= 3:
                    st.session_state.num = 0 
                placeholder.empty()
            else:
                st.stop()


main()


   

import streamlit as st


#Seccion 1: Presentación
my_page = st.sidebar.radio("Página de navegación", ["Historia", "Hombres", "Mujeres", "Referencias bibliográficas"])

if my_page == "Historia":
    st.title("Sexuapp")
    st.write("")
    st.write("")
    st.write("")

    st.header("¡Hola! Bienvenido (a) Sexuapp")

    st.write("")
    st.write("")
    st.subheader("Historia")
    st.write("")
    st.write("")
    st.subheader("Esta guía fue desarrollada por dos estudiantes de posgrado de la Universidad Autónoma de Chihuahua con el fin de ayudar en la orientación de algunas enfermedades de transmisión sexual a través de la descripción de síntomas comúnmente presentados.")
    st.write("")
    st.write("")
    st.write("Podrás aprender acerca de las posibles causas de tus síntomas")
    st.write("")
    st.write("")
    st.write("")


if my_page == "Hombres":
st.title("Hombres")
st.write("")
st.write("")
option = st.selectbox(
'¿Presentas alguno de estos síntomas?',
('Llagas', 'Hinchazón', 'Verrugas', 'Irritación, enrojecimiento o ardor'))
if 'Llagas' in option:
        st.write('Las llagas son uno de los síntomas característicos de la sífilis, la cual, es una infección bacteriana causada por Treponema pallidum.')
        st.subheader('Causas de transmisión')
        st.write('Puedes contagiarte por contacto sexual vaginal, anal u oral con alguna persona infectada; pero también y de forma menos común es mediante el contacto con una lesión activa como las que se podrían presentar en la boca y al darse un beso se transmitiría.')
        st.write('También existe la probabilidad de transmisión de madre a hijo durante el embarazo o parto mediante el contacto de las llagas con la piel o membranas mucosas.')
        st.warning('Debes saber que no es probable que se contagie mendiante el uso de inodoros, ropa, piscinas, jacuzzis; por mencionar algunos ejemplos.')
        st.write('Los síntomas más comunes es la aparición de llagas indoloras en boca, recto o genitales.')
        st.write('')
        st.write('')
        st.subheader('¿Cuál es el tratamiento adecuado para mí?')
        st.write('Es simple. Existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiótico recomendado por tu médico, por lo que en caso de presentar algun sÍntoma, es necesario que acude inmediatamente con tu médico, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a tus órganos como el corazón o cerebro incluso algunos otros.')
        st.write('')
        st.write('')
        st.info('POR FAVOR, ¡CHÉCATE!')
if 'Hinchazón' in option:
        st.write('La hinchazón en pene o testículos puede considerarse como uno de los síntomas caraterísticos de la Blenorragia o Gonorrea, esta infección de trasmisión sexual que afecta tanto hombres y mujeres causada por la bacteria Neisseria gonorrhoeae y puedes adquirirla por sexo vaginal, anal u oral; así como también puede trasnmitirse por la mamá al bebé durante del parto.')
        st.write('Aunque esta infección puede expresarse en varias partes del cuerpo como el recto, ojos, garganta y articulaciones; generalmente se expresa más en los genitales, donde se puede presentar secresión en la punta del pene similar al pus, dolor al orinar o hinchazón en los testículos.')
        st.write('')
        st.write('')
        st.warning('Entre sus complicaciones puedes presentar infertilidad y afectación en las articulaciones, así como también aumenta la posibilidad de contraer VIH/SIDA.')
        st.write('')
        st.write('')
        st.subheader('¿Cuál es el tratamiento adecuado para mí?')
        st.write('Deberás acudir con tu médico ante síntomas o sospechas de gonorrea y este te asignará un tratamiento adecuado tanto para ti como tu pareja.')
        st.write('')
        st.write('')
        st.info('POR FAVOR, ¡CHÉCATE!')
if 'Verrugas' in option:
        st.write('Cuando presentas verrugas en los genitales existe una causa probable de que estés contagiado con el Virus del Papiloma Humano (VPH).')
        st.write('Se dice que todas las personas sexualmente activas adquirirán el virus en algún momento de sus vidas.')
        st.write('Existen causas probables de transmisión como la práctica de sexo vaginal, sexo anal u oral; aunque también se trasnmite por medio de cortaduras, abrasiones y desgarros; además las personas son portadoras del VIH o con alguna alteración en el sistema inmune.')
        st.write('La verrugas ocasionadas por este virus se presentan principalmente en los tejidos húmedos de las zonas genitales como el escroto, punta o cuerpo del pene o ano, aunque también se podrían presentar en la boca o garganta de la persona infectada dependiendo del modo de contagio; además que en muchas ocasiones las verrugas son tan pequeñas que no logran ser visibles.')
        st.write('Presentan un color carne y apariencia similar a una coliflor.')
        st.write('También puedes presentar hinchazón, comezón o malestar en el área e incluso sangrado al momento de mantener relaciones sexuales.')
        st.write('')
        st.write('')      
        st.warning('Las complicaciones a largo plazo es que aumentan la posibilidad de presentar cáncer en pene, boca, ano y garganta,')
        st.write('')
        st.write('')
        st.subheader('¿Cuál es el tratamiento adecuado para mí?')
        st.write('Tu médico te recomendará las instrucciones a seguir una vez diagnosticado')
        st.info('POR FAVOR, ¡CHECATE!')
if 'Irritación, enrojecimiento o ardor' in option:
        st.write('Este síntoma se puede debe a varias causas entre las cuales existe la presencia de alguna infección o la portación de microrganismos como el causante de la Trichomoniasis por el parásito Tricomonas vaginallis o la infección por balanianitis causada por contacto con el hongo Candida albicans; ambas presentan enrojecimiento, picazón y sensación de ardor en el pene al orinar o mantener relaciones sexuales.')
        st.write('En ambos casos es ocasionado por el contacto sexual vaginal con parejas portadoras de los microoganismos señalados que presentan Candidiasis y Trichomoniasis.')
        st.write('')
        st.write('')
        st.subheader('¿Tratamiento?')
        st.write('En ambos casos necesitarás visitar a tu médico que aplicará el tratamiento correspondiente dependiendo del patógeno.')
        st.info('POR FAVOR, CHÉCATE!')

if my_page == "Mujeres":
st.title("Mujeres")
st.write("")
st.write("")
option = st.selectbox('¿Presentas alguno de estos síntomas?',('Llagas', 'Aumento del flujo vaginal', 'Verrugas', 'Irritación, enrojecimiento o ardor', 'Secreción vaginal', 'Olor fétido'))
if 'Llagas' in option:
st.write('Las llagas son uno de los síntomas característicos de la sífilis.')
st.write('La Sílifis es una infección bacteriana causada por Treponema pallidum. La principal causa de transmisión es por contacto sexual con alguna persona infectada, ya sea vaginal, anal u oral, pero también y de forma menos comun es mediante el contacto con una lesión activa en la boca, ya que al darse un beso se podría transmitir.')
st.write('También existe la probabilidad de transmisión de madre a hijo durante el embarazo o parto. Esto puede ocurrir por medio del contacto de las llagas con la piel o membranas mucosas.')
st.warning('Es importante que sepas que no es probable que te contagies mediante el uso de inodoros, compartir ropa, pisciinas, jacuzzis; por mencionar algunos ejemplos.')
st. write('')
st. write('')
st.write('Además de la aparición de llagas en los genitales, también se pueden presesentar llagas indoloras en boca y recto.')
st.subheader('¿Cuál es el tratamiento?')
st.write('Es simple. Existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiótico recomendado por tu médico.')
st. write('')
st. write('')
st.warning('En caso de que presentes algun sintoma acude inmenditamente con tu medico a realizar el diagnostico correspondiente, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a órganos como el corazón o cerebro, incluso algunos otros.')
st. write('')
st. write('')
st.info('POR FAVOR, ¡CHÉCATE!')
  if 'Aumento del flujo vaginal' in option:
st.write('El aumento del flujo vaginal puede considerarse como uno de los síntomas caraterísticos de la Blenorragia o también conocida como Gonorrea.')
st.write('Esta infección de trasmisión sexual afecta tanto hombres y mujeres y es causada por la bacteria Neisseria gonorrhoeae. Puede ser adquirida tanto por relaciones sexuales vaginales, anales u orales.')
st.write('Aunque también puede ser transmitida durante el parto por la madre al bebé.')
st.write('Aunque esta infección puede expresarse en varias partes del cuerpo como el recto, ojos, garganta y articulaciones; esta infección se expresa generalmente en los genitales, donde además puedes presentar dolor al orinar, sangrado vaginal después de mantener relaciones sexuales vaginales, dolor abdominal o pélvico.')
st. write('')
st. write('')
st.warning('Entre sus complicaciones existe la posibilidad de infertilidad, presentar afectaciones en las articulaciones, y aumenta la posibilidad de contraer VIH/SIDA.')
st. write('')
st. write('')
st.subheader('¿Cuál es el tratamiento?')
st.write('Deberás acudir con tu médico ante síntomas o sospechas de gonorrea y este te asignará el tratamiento adecuado tanto para ti como tu pareja.')
st. write('')
st. write('')
st.info('¡POR FAVOR, CHECATE!')
if 'Verrugas' in option:
st.write('Cuando se presentan verrugas en los genitales existe una causa probable de que se deba al Virus del Papiloma Humano (VPH).')
st.write('Se dice que todas las personas sexualmente activas adquirirán el virus en algún momento de sus vidas. Existen causas probables de transmisión como la práctica de relaciones sexuales vaginales, anales u orales.')
st.write('Aunque también se puede transmitir por medio de cortaduras, abrasiones y desgarros.')
st. write('')
st. write('')
st. warning('Es importante que sepas que las personas que son portadoras del VIH o con alguna alteración en el sistema inmune son aun mas propensas.')
st. write('')
st. write('')
st.write('La verrugas ocasionadas por este virus se presentan principalmente en los tejidos húmedos de las zonas genitales o ano aunque también se pueden presentar en la boca o garganta de la persona infectada dependiendo del modo de contagio, presentan un color carne y apariencia similar a una coliflor.')
st.write('También se puede presentar hinchazón, comezón o malestar en el área; así como sangrado al momento de mantener relaciones sexuales, ademas en muchas ocasiones las verrugas son tan pequeñas que no logran ser visibles.')
st. write('')
st. write('')
st.warning('Las complicaciones a largo plazo es que aumenta la posibilidad de presentar cancer de cuello uterino, boca, ano y garganta.')
st. write('')
st. write('')
st.subheader('¿Cuál es el tratamiento?')
st.write('Tu médico te recomendará las instrucciones a seguir una vez que hayas sigo correctamente diagnosticada.')
st. write('')
st. write('')
st.info('POR FAVOR, ¡CHÉCATE!')
if 'Irritación, enrojecimiento, picazón y ardor' in option:
st.write('Este síntoma puede deberse a varias causas como Trichomoniasis ocasionada por el parásito patógeno Tricomonas vaginallis o candidiasis causada por contacto con hongos vaginales como Candida albicans.')
st.write('Ambas enfermedades ocasionan síntomas como enrojecimiento, picazón y sensación de ardor en los genitales al orinar o mantener relaciones sexuales. En ambos casos este es ocasionado por el contacto sexual vaginal con parejas portadoras de estos microorganismos.')
st.subheader('¿Cuál es el tratamiento?')
st.write('En ambos casos necesitarás visitar a tu médico el cual aplicará las pruebas de diagnóstico adecuadas y en caso de confirmar, se necesitará aplicar el tratamiento correspondiente dependiendo de la infección.')
st.info('POR FAVOR, ¡CHÉCATE!')
if 'Secreción vaginal' in option:
st.write('Existen fluidos vaginales que no son comunes tener y que pueden estar relacionados con alguna enfermedad de transmisión sexual.  Estos pueden ser fluidos de colores como gris, amarillo o verde y es caracteristico de la tricomoniasis o vaginitis bacteriana')
st.write('También puede ser una secreción espesa, blanca e inolora parecida al queso cotagge que es parte de los síntomas relacionados con la candidiasis.'
st.write('Estas infecciones son ocasionadas por distintos microrganismos patógenos y en la mayoría de los casos estas son ocasionados por el contacto sexual vaginal con parejas portadoras de los agentes causantes de las mismas.')
st. write('')
st. write('')
st.subheader('¿Cuál es el tratamiento?')
st.write('En estos casos necesitarás visitar a tu médico el cual aplicará las pruebas de diagnóstico correctas y en caso de confirmar se aplicará el tratamiento correspondiente dependiendo de la enfermedad.')
st.info('POR FAVOR, ¡CHÉCATE!')
if 'Olor fétido' in option:
st.write('El olor fétido a "pescado", es uno de los síntomas mas comunes de las vaginitis bacteriana.')
st.write('Estas infecciones son ocasionadas principalmente por un desequilibrio en la población bacteriana de la vagina.')
st.write('Además de este síntoma, también es posible que presentes comezón, ardor o secreción de color gris, blanca o verde en tu zona íntima.')
st. write('')
st. write('')
st.warning('Si no es tratada correctamente la vaginitis bacteriana puede ocasionar complicaciones durante el embarazo, enfermedad inflamatoria pélvica o aumentar la posibilidad de contraer otras enfermedades de transmisión sexual.')
st. write('')
st. write('')
st.subheader('¿Cuál es el tratamiento?')
st. write('Deberás acudir al médico a que te aplique las herramientas de diagnóstico adecuadas y él te indicará al tratamiento correcto para ti.')
st. write('')
st. write('')
st.info('POR FAVOR, ¡CHÉCATE!')
   

if my_page == "Referencias bibliográficas":
    st.title("Referencias bibliográficas")
    st.write("")
    st.write("")
[theme]
primaryColor="#purple"
backgroundColor="#white"
secondaryBackgroundColor="#blue"
textColor="#black"
font="sans serif"
         import streamlit as st
option = st.selectbox(
     'Presentas alguno de estos sintomas?',
     ('Llagas', 'Hinchazon', 'Verrugas', 'Irritacion, Enrojecimiento o Ardor'))
if 'Llagas' in option:
     st.write('Las Llagas son uno de los sintomas carcaterisiticos de la sifilis; La Silifis es una infeccion bacteriana causada por Treponema pallidum, la principal causa de trasnmision es por Contacto Sexual con alguna persona infectada,ya sea vaginal, anal u oral, pero tambien y de fomra menos comun ,es mediente el contacto con una lesion activa como las que se podrian presentar en la boca y al darse un beso se transmitiria, tambien existe la probabilidad de trasnmision de madre a hijo durante el embarazo o parto,todo esto mediente el contacto de las llagas con la piel o membranas mucosas. Aunque es de condsideracion señalar que no es probable que se contagie mendiente el uso de tasas de baño, ropa, piciinas, jacuzzis por mencionar algunos ejemplos. Los sintomas mas comunes es la aparicion de Llagas indoloras en boca, recto o genitales . ¿El tratamiento? es simple existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiotico recomendado por tu medico, en este caso en caso de presentar algun sintoma acude inmenditamente con tu medico, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a organos como el corazon o cerebro incluso algunos otros. ¡POR FAVOR, CHECATE!')
if 'Hinchazon' in option:
     st.write('La hinchazon en pene o testiculos puede considerarse como uno de los sintomas carateristicos de la Blenorragia o Gonorrea, esta infeccion de trasmision sexual que afecta tanto hombres y mujeres causada por la bacteria Neisseria gonorrhoeae y puede ser adquirida tanto por sexo vaginal, anal u oral y  tambien puede ser trasnmitida por la mama al bebe al momento del parto. Aunque esta infeccion puede expresarse en varias partes del cuerpo como el recto, ojos, garganta y articulaciones aunque generalmente se expresa mas en los genitales, donde se puede presentar secresion en la punta del pene similar al pus, dolor al orinar o hinchazon en los testiculos. Ademas entre sus comlicaciones se puede presentar infertilidad, puedes presentar afectacion en las articulaciones y aumentan la posibilidad de contraer VIH/SIDA. ¿Tratamiento? deberas acudir con tu medico ante sintomas o sospechas de gonorrea y  este te asiganra el tratamiento adecuado tanto para ti como tu pareja. ¡POR FAVOR, CHECATE!')
if 'Verrugas' in option:
     st.write('Cuando se presentan verrugas en los genitales existe una causa probable; El Virus del Papiloma Humano (VPH). Se dice que todas las personas sexualmente activas adquiriran el virus en aqlgun momento de sus vidas. Existen causad probables de transmision como la practica de sexo vaginal, sexo anal u oral , aunque tambien se trasnmite por medios de cortes, abrasiones y  desgarros, ademas las personas son pportadoras del VIH o con alguna alteracion en el sistema inmune. La verrugas ocasionadas por este virus se presentan principalmente en los tejidos humedos de las zonas genitales como el escroto, punta o cuerpo del pene o  ano, aunque tambien se podrian presenta en la boca o garganta de la persona infectada dependiendo del modo de contagio, ademas que en muchas ocasiones las verrugas son tan pequeñas que no logran ser visibles. Presentan un color carne y apariencia a una coliflor, acoplado a esto se puede presentar hinchazon, comezon o malestar en el area e incluso sangrado al momento de mantener relaciones sexuales. dentro de las complicaciones a largo plazo aumenta la posibilidad de presentar cancer tanto pene, boca, ano y garganta ¿Tratamiento? tu medico te recomendara las instrucciones a seguir una vez diagnosticado, ¡POR FAVOR, CHECATE!')  
if 'Irritacion, Enrojecimiento o Ardor' in option:
     st.write('Este sintoma puede debe a varias causas entre las cuales la presencia de alguna infeccion o la portacion de microrganismos como el causante de la Trichomoniasis por el parasito Tricomonas vaginallis o la infeccion por balanianitis causada por contacto con el hongo Candida albicans, ambas presentan enrojecimiento, picazón y sensacion de ardor en el pene como al orinar o mantener relaciones sexuales. En ambos casos este es ocasionado por el contacto sexual vaginal con parejas portadoras de los microoganismos señalados que presentan Candidiasis y Trichomoniasis. ¿Tratamiento? en ambos casos necesitaras visitar a tu medico se aplicara el tratamiento correspondiente dependiendo de la naturaleza del patogeno. ¡POR FAVOR, CHECATE!')

     #Seccion de Mujeres
     
     import streamlit as st
     
option = st.selectbox(
     'Presentas alguno de estos sintomas?',
     ('Llagas', 'Aumento del flujo vaginal', 'Verrugas', 'Irritacion, Enrojecimiento o Ardor', 'Secrecion Vaginal', 'Olor fetido'))
if 'Llagas' in option:
     st.write('Las Llagas son uno de los sintomas carcaterisiticos de la sifilis; La Silifis es una infeccion bacteriana causada por Treponema pallidum, la principal causa de trasnmision es por Contacto Sexual con alguna persona infectada, ya sea vaginal, anal u oral, pero tambien y de forma menos comun es mediente el contacto con una lesion activa como las que se podrian presentar en la boca y al darse un beso esta se transmitiria, tambien existe la probabilidad de trasnmision de madre a hijo durante el embarazo o parto, todo esto mediente el contacto de las llagas con la piel o membranas mucosas. Aunque es de condsideracion señalarte que no es probable que te contagies mediante el uso de tasas de baño, ropa, piciinas, jacuzzis por mencionar algunos ejemplos. Ademas de aparicion en genitales tambien se puede presesentar llagas indoloras en boca y recto- ¿El tratamiento? es simple existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiotico recomendado por tu medico, en caso de que presentes algun sintoma acude inmenditamente con tu medico a realizar el diagnostico correspondiente, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a organos como el corazon o cerebro incluso algunos otros. ¡POR FAVOR, CHECATE!')
if 'Aumento del flujo vaginal' in option:
     st.write('El aumento del flujo vaginal puede considerarse como uno de los sintomas carateristicos de la Blenorragia o Gonorrea, esta infeccion de trasmision sexual que afecta tanto hombres y mujeres causada por la bacteria Neisseria gonorrhoeae y puede ser adquirida tanto por sexo vaginal, anal u oral y tambien puede ser trasnmitida en el momento del parto de la madre al bebe. Aunque esta infeccion puede expresarse en varias partes del cuerpo como el recto, ojos, garganta y articulaciones esta se expresa generalmente en los genitales, donde ademas puedes presentar dolor al orinar, sangrado vaginal como despues de tener relaciones sexuales vaginales, ademas de dolor abdominal o pelvico. Ademas entre sus complicaciones existe la posibilidad infertilidad,presentar afectaciones en las articulaciones y aumenta la posibilidad de contraer VIH/SIDA. ¿Tratamiento? deberas acudir con tu medico ante sintomas o sospechas de gonorrea y  este te asiganra el tratamiento adecuado tanto para ti como tu pareja. ¡POR FAVOR, CHECATE!')
if 'Verrugas' in option:
     st.write('Cuando se presentan verrugas en los genitales existe una causa probable; El Virus del Papiloma Humano (VPH). Se dice que todas las personas sexualmente activas adquiriran el virus en algun momento de sus vidas. Existen causas probables de transmision como la practica de sexo vaginal, anal u oral, aunque tambien se transmite por medios de cortes, abrasiones y desgarros. Ademas las personas que son portadoras del VIH o con alguna alteracion en el sistema inmune son aun mas propensas. La verrugas ocasionadas por este virus se presentan principalmente en los tejidos húmedos de las zonas genitales o ano aunque tambien se podrian presentar en la boca o garganta de la persona infectada dependiendo del modo de contagio, presentan un color carne y apariencia a una coliflor, adicional a esto se puede presentar hinchazon, comezón o malestar en el area e incluso sangrado al momento de mantener relaciones sexuales, ademas en muchas ocasiones las verrugas son tan pequeñas que no logran ser visibles. Dentro de las complicaciones a largo plazo aumenta la posibilidad de presentar cancer de cuello uterino boca, ano y garganta ¿Tratamiento? tu medico te recomendara las instrucciones a seguir una vez diagnosticado correctamente y en caso de presentar la infeccion, ¡POR FAVOR, CHECATE!')  
if 'Irritacion, Enrojecimiento, Picazón y Ardor' in option:
     st.write('Este sintoma puede deberse a varias causas como Trichomoniasis ocasionada por el parasito patogeno Tricomonas vaginallis o candidiasis causada por contacto con el hongos vagianles como Candida albicans, ambas presentan enrojecimiento, picazón y sensacion de ardor en los genitales al orinar o mantener relaciones sexuales. En ambos casos este es ocasionado por el contacto sexual vaginal con parejas portadoras de los microoganismos señalados causanttes de las mismas. ¿Tratamiento? en ambos casos necesitaras visitar a tu medico el cual aplicara las prubeas de diagnostico correcto y  en caso de confirmar se aplicara el tratamiento correspondiente dependiendo de la naturaleza del patogeno. ¡POR FAVOR, CHECATE!')
if 'Secrecion Vaginal' in option:
     st.write('Existen fluidos vaginales inusuales que pueden estar relacionados con alguna enfermedad de transmision sexual como por ejemplo fluido de colores como gris, amarillo o verde es caracteristico de la tricomoniasis y tambien puede tener caracteristicas propias de una vaginitis bacteriana, o bien secrecion espesa, blanca e inoloro parecida al queso cotagge que es parte de los sintomas relacionados con la candidiasis, estas infecciones son ocasionadas por distintos microrganismos patogenos y en la mayoria de los casos estas son ocasionados por el contacto sexual vaginal con parejas portadoras de los agentes causantes de las mismas. ¿Tratamiento? En estoscasos necesitaras visitar a tu medico el cual aplicara las pruebas de diagnostico correcto y  en caso de confirmar se aplicara el tratamiento correspondiente dependiendo de la naturaleza del patogeno. ¡POR FAVOR, CHECATE!')
if 'Olor fetido' in option:
     st.write('El olor fetido a "pescado", es uno  de los sintomas mas comunes de las vaginitis bacterianas, estas son ocasionadas principalmente por un desequilibrio en la poblacion bacteriana de la vagina. Ademas de este sintoma tambien es caracteristico de las vaginitis bacteriana comezón vaginal, ardor vaginal o secrecion vaginal de color gris, blanca o verde,  estas ademas de  no ser tratadas correctamente las vaginitis bacterianas traen consigo complicaciones durente el embarazo, enferemedad inflamatorio pelvica o el aumento posibilidad de contraer otras enfermedades de transmision sexual ¿Tratamiento? Primero deberas acudir al medico a que te aplique las herramientas de diagnostico correcto y posterior a eso el te indeicara al tratamiento adecuado para ti')
     
[theme]
primaryColor="#purple"
backgroundColor="#white"
secondaryBackgroundColor="#blue"
textColor="#black"
font="sans serif"


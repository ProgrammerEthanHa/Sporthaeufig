import streamlit as st
import pandas as pd
import altair as alt

st.header("Sportliche Aktivität von Jungen im Alter von 11-13 Jahren")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [34, 36.7, 23.1, 6.2],
        'Häufigkeit': ['Fast täglich', '3-5 Mal pro Woche', '1-2 Mal pro Woche', 'Seltener']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Häufigkeit:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Deutschland; 11-13 Jahre; Jungen
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista Research Department")
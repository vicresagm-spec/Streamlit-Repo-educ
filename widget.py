import streamlit as st

st.header("this is a sample one ",divider ='rainbow')

#st.button allows the display of a button widget
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 

#create teh header text fro the app
st.header('st.button',divider='gray')

# conditional astatement for alternate msgs

if st.button('Say Hello'):
    st.write('Why Hello there ')
else:
    st.write('Goodbye')


st.header('st.write')

st.write('Hello ,*world!*  :sunglasses:')

st.write(1234)


df = pd.DataFrame({
    'First Coloumn':[1,2,3,4],
    'Second Coloumn':[10,20,30,40]
})
st.write(df)

st.write('Below is a Dataframe',df,'Avbove is adataframe ')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
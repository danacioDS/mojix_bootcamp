import streamlit as st
import pandas as pd
import sqlalchemy

st.title('Fundamentals comparison')

engine = sqlalchemy.create_engine('sqlite:///Fundamentals.db')
df = pd.read_sql('Fundamentalstable',engine, index_col=['symbol'])

dropdown_1 = st.selectbox('Choose your sector',
df.sector.unique())

dropdown_2 = st.selectbox('Choose your metric',
df.columns[df.columns !='sector'])

values = df[df.sector==dropdown_1][[dropdown_2]]

st.bar_chart(values)

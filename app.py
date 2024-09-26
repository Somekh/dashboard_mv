import streamlit as st
import pandas as pd
from scipy import stats

st.title("Анализ продаж")

# Загрузка данных
df = pd.read_csv("stats.csv", encoding='cp1251')

df = df.set_axis(['work_days', 'age', 'gender'], axis=1)
df['gender'] = df['gender'].replace({'М': 1, 'Ж': 0})
df.to_parquet('ttr.parquet')
# Визуализация данных
st.header('рабочие дни', divider='gray')
st.line_chart(df["work_days"])

# # Фильтрация данных
# date_filter = st.slider("Выберите период", min_value=df["age"].min(), max_value=df["age"].max())
# filtered_df = df[df["age"] <= date_filter]
# st.line_chart(filtered_df["work_days"])


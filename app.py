import streamlit as st
import pandas as pd
from scipy import stats
import seaborn as sns

st.title("Проверка гипотез")

# Загрузка данных
df = pd.read_csv("stats.csv", encoding='cp1251')

df = df.set_axis(['work_days', 'age', 'gender'], axis=1)
df['gender'] = df['gender'].replace({'М': 1, 'Ж': 0})
df.to_parquet('ttr.parquet')
# Визуализация данных
age = st.number_input("Укажите уровень стат. значимости:", min_value=0.01, max_value=0.2, value=0.05)
st.header('рабочие дни', divider='gray')
st.line_chart(df["work_days"])

# # Фильтрация данных
# date_filter = st.slider("Выберите период", min_value=df["age"].min(), max_value=df["age"].max())
# filtered_df = df[df["age"] <= date_filter]
# st.line_chart(filtered_df["work_days"])

# age = st.number_input("Введите ваш возраст:", min_value=0, max_value=120, value=30)
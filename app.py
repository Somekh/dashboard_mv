import streamlit as st
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

alpha = st.number_input("Укажите уровень стат. значимости:", min_value=0.01, max_value=0.2, value=0.05)
days = st.number_input("Укажите значение порога количества дней (work_days):", min_value=1, max_value=6, value=2)

#Загрузка файла
uploaded_file = st.file_uploader("Загрузите CSV файл:", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='cp1251')
else:
    df = pd.read_csv("stats.csv", encoding='cp1251')

df = df.set_axis(['work_days', 'age', 'gender'], axis=1)
df['gender'] = df['gender'].replace({'М': 1, 'Ж': 0})
df.to_parquet('ttr.parquet')

#Пол
men = df[(df['gender'] == 1) & (df['work_days'] > days)]
women = df[(df['gender'] == 0) & (df['work_days'] > days)]
t_statistic, p_value = stats.ttest_ind(men['work_days'], women['work_days'], equal_var=False)

st.title("Проверка гипотез")
st.write(f"Для проверки гипотез будем применять критерий Стьюдента (t-test).")
st.header('Пол', divider='gray')
st.write(f"p_value = {round(p_value, 4)}. Статистика = {round(t_statistic, 4)}.")
if p_value > alpha:
    st.write(f"Можно говорить о том, что нет статистически значимой разницы между двумя выборками. Отвергаем гипотезу о значимости пола сотрудника")
else:
    st.write(f"Можно говорить о том, что есть статистически значимая разница между двумя выборками. Данные не противоречат гипотезе.")

# Построение графика
fig, ax = plt.subplots(figsize=(10, 5))
sns.kdeplot(men['work_days'], label='Мужчины', fill=True, ax=ax)
sns.kdeplot(women['work_days'], label='Женщины', fill=True, ax=ax)
ax.set_title(f"Графики плотности вероятности пропущенных рабочих дней")
ax.set_xlabel('Кол-во пропущенных рабочих дней')
ax.set_ylabel("Плотность")
ax.legend()
st.pyplot(fig)

#Возраст
st.header('Возраст', divider='gray')
age = st.number_input("Укажите значение порога возраста (age):", min_value=23, max_value=40, value=35)

older = df[(df['age'] > age) & (df['work_days'] > days)]
younger = df[(df['age'] <= age) & (df['work_days'] > days)]
t_statistic_age, p_value = stats.ttest_ind(older['work_days'], younger['work_days'], equal_var=False)

st.write(f"p_value = {round(p_value, 4)}. Статистика = {round(t_statistic_age, 4)}.")
if p_value > alpha:
    st.write(f"Можно говорить о том, что нет статистически значимой разницы между двумя выборками. Отвергаем гипотезу о значимости возраста сотрудника.")
else:
    st.write(f"Можно говорить о том, что есть статистически значимая разница между двумя выборками. Данные не противоречат гипотезе.")

# Построение графика
fig, ax = plt.subplots(figsize=(10, 5))
sns.kdeplot(older['work_days'], label='старые', fill=True, ax=ax)
sns.kdeplot(younger['work_days'], label='молодые', fill=True, ax=ax)
ax.set_title(f"Графики плотности вероятности пропущенных рабочих дней")
ax.set_xlabel('Кол-во пропущенных рабочих дней')
ax.set_ylabel("Плотность")
ax.legend()
st.pyplot(fig)
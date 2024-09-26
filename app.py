import streamlit as st
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Проверка гипотез")
alpha = st.number_input("Укажите уровень стат. значимости:", min_value=0.01, max_value=0.2, value=0.05)
days = st.number_input("Укажите порог количества дней:", min_value=1, max_value=50, value=2)

df = pd.read_csv("stats.csv", encoding='cp1251')
df = df.set_axis(['work_days', 'age', 'gender'], axis=1)
df['gender'] = df['gender'].replace({'М': 1, 'Ж': 0})
df.to_parquet('ttr.parquet')

men = df[(df['gender'] == 1) & (df['work_days'] > days)]
women = df[(df['gender'] == 0) & (df['work_days'] > days)]
t_statistic, p_value = stats.ttest_ind(men['work_days'], women['work_days'], equal_var=False)
if p_value > alpha:
    st.write("Можно говорить о том что нет стат значимой разницы между выборками")
else:
    st.write('Можно говориь о том, что есть статистически значимая разница между двумя выборками')

plt.figure(figsize=(10, 5))

sns.kdeplot(men['work_days'], label='Мужчины', fill=True)
sns.kdeplot(women['work_days'], label='Женщины', fill=True)

plt.title(f"Графики плотности вероятности пропущенных рабочих дней")
plt.xlabel('Кол-во пропущенных рабочих дней')
plt.ylabel("Плотность")
plt.legend()

st.show()












st.header('рабочие дни', divider='gray')
st.line_chart(df["work_days"])

# # Фильтрация данных
# date_filter = st.slider("Выберите период", min_value=df["age"].min(), max_value=df["age"].max())
# filtered_df = df[df["age"] <= date_filter]
# st.line_chart(filtered_df["work_days"])

# age = st.number_input("Введите ваш возраст:", min_value=0, max_value=120, value=30)
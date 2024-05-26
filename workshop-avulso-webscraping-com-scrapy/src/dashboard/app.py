import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

# Fechar a conexão com o banco de dados SQLite
conn.close()

# Streamlit - Inserindo o título da aplicação
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

# Streamlit - Melhorar o layout com colunas para KPI (Key Performance Indicator | Indicadores de perfomance chave)
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

# Streamlit - KPI #1: Número total de itens
total_items = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_items)

# Streamlit - KPI #2: Número de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

# Streamlit - KPI #3: Preço médio novo (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

# Streamlit - Quais são as marcas mais encontradas até a página 10
st.subheader('Marcas mais encontradas até a página 10')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Streamlit - Qual o preço médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Streamlit - Qual a satisfação por marca
st.subheader('Nível de satisfação por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)

# Streamlit - Tabela completa
st.subheader('Tabela completa')
st.write(df)
import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Dasboard de Visualisation des Données de Vente - AdventureWorks")

# Charger la table de calendrier

calendar = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Calendar Lookup.csv")

# Créer les colonnes années, trimestres et nom du mois en français
calendar['Year'] = pd.to_datetime(calendar['Date']).dt.year
calendar['Quarter'] = pd.to_datetime(calendar['Date']).dt.quarter
calendar['Month Name'] = pd.to_datetime(calendar['Date']).dt.month_name(locale='fr_FR')
st.write("Table de calendrier avec les colonnes années, trimestres et nom du mois en français :")
st.dataframe(calendar.head())

# Charger les tables de ventes

sales_2020 = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Sales Data 2020.csv")
sales_2021 = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Sales Data 2021.csv")
sales_2022 = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Sales Data 2022.csv")

# Combiner les tables de ventes en une seule table
sales = pd.concat([sales_2020, sales_2021, sales_2022], ignore_index=True)
st.write("Table combinée des ventes pour les années 2020, 2021 et 2022 :")
st.dataframe(sales.head())

# Charger la table de produits, catégories et sous-catégories
products = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Product Lookup.csv")
categories = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Product Categories Lookup.csv")
subcategories = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Product Subcategories Lookup.csv")

# Fusionner les tables de produits, catégories et sous-catégories
products = products.merge(subcategories, on='ProductSubcategoryKey', how='left')
products = products.merge(categories, on='ProductCategoryKey', how='left')
st.write("Table des produits avec les catégories et sous-catégories :")
st.dataframe(products.head())

# Charger la table territoires
territories = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Territory Lookup.csv")
st.write("Table des territoires :")
st.dataframe(territories.head())

# Charger la table retours
returns = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Returns Data.csv")
st.write("Table des retours :")
st.dataframe(returns.head())

# Charger la table clients
customers = pd.read_csv("C:\\Users\\HP\\Desktop\\Davis\\Streamlit\\training_data_model\\data\\AdventureWorks Customer Lookup.csv")
st.write("Table des clients :")
st.dataframe(customers.head())

# VISUALISATION DES DONNÉES

# Histogramme des ventes par year
sales_by_year = sales.groupby('OrderDate')['OrderQuantity'].sum().reset_index()
sales_by_year['OrderDate'] = pd.to_datetime(sales_by_year['OrderDate'])
sales_by_year['Year'] = sales_by_year['OrderDate'].dt.year
st.write("Histogramme des ventes par année :")
st.bar_chart(sales_by_year.groupby('Year')['OrderQuantity'].sum())

# Ajouter un widget de sélection pour les années
years = sales['OrderDate'].str[:4].unique()
selected_year = st.selectbox("Sélectionnez une année :", years)

# Filtrer les données l'histogramme en fonction de l'année sélectionnée
filtered_sales = sales[sales['OrderDate'].str.startswith(selected_year)]
sales_by_month = filtered_sales.groupby(filtered_sales['OrderDate'].str[5:7])['OrderQuantity'].sum().reset_index()
sales_by_month['OrderDate'] = pd.to_datetime(sales_by_month['OrderDate'], format='%m')
sales_by_month['Month Name'] = sales_by_month['OrderDate'].dt.month_name(locale='fr_FR')
st.write(f"Histogramme des ventes pour l'année {selected_year} :")
st.bar_chart(sales_by_month.groupby('Month Name')['OrderQuantity'].sum())


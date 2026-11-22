import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload file", type=["CSV"])

if file is None:
    st.info("Please upload a CSV file to get started.")
    st.stop()

df = load_data(file)
n_rows = max_value=len(df)
df_columns = df.columns.to_list()

rows_to_show = st.slider('Choose number of rows', min_value=1, max_value=n_rows, step = 1, value = n_rows//2)
columns_to_show = st.multiselect("Choose Columns to show", df_columns, default=df_columns)


st.write(df[:n_rows][columns_to_show])

numerical_df = df.select_dtypes(include=['number'])
numerical_columns = numerical_df.columns.to_list()

tab1, tab2 = st.tabs(["Scatter", "Histogram"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        color = st.selectbox("select the column to be color", df_columns)
    with col2:
        xAxis_scatter = st.selectbox("select the column for x-axis", numerical_columns)
    with col3:
        yAxis_scatter = st.selectbox("select the column for y-axis", numerical_columns)
    fig_scatter = px.scatter(df, x = xAxis_scatter, y = yAxis_scatter, color=color)
    st.plotly_chart(fig_scatter)
with tab2:
    column_for_histogram = st.selectbox("select column to see its histogram", numerical_columns)
    fig_hist = px.histogram(df, x=column_for_histogram)
    st.plotly_chart(fig_hist)

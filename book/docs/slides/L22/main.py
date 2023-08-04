import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

st.title("Heart Failure Prediction Dataset")
st.text("This is a web app to allow exploration of Heart failure Data")


def show_about_page():
    st.header("Dataset")
    st.markdown(
        """
    This dataset is taken from
    https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

    At Kaggle, several authors publish their own code where they
    have analyzed the different datasets.

    For example, the following review https://www.kaggle.com/code/durgancegaur/a-guide-to-any-classification-problem/notebook
    is a pretty good one.
    """,
    )


df = pd.read_csv("heart.csv")


def show_data_summary_page(df):
    st.header("Statistics of Dataframe")
    st.write(df.describe())


def show_data_header_page(df):
    st.header("Header of Dataframe")
    st.write(df.head())


def plot_mpl(df):
    st.header("Plot of Data")

    fig, ax = plt.subplots()
    ax.scatter(x=df["Age"], y=df["MaxHR"])
    ax.grid()
    ax.set_xlabel("Age")
    ax.set_ylabel("MaxHR")

    st.pyplot(fig)


def plot_pairplot(df):
    st.header("Pair plot")

    column = st.selectbox(
        "Select column",
        options=df.columns,
    )

    grid = sns.pairplot(df, hue=column)
    st.pyplot(grid.fig)


def histogram(df):
    st.header("Histogram")

    column = st.selectbox("Select column", options=df.columns)
    plot = px.histogram(df, x=column)
    st.plotly_chart(plot, use_container_width=True)


def two_columns(df):
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox("Select the X-axis", options=df.columns)
    y_axis_val = col2.selectbox("Select the Y-axis", options=df.columns)

    plot_type = st.selectbox("Select plot type", options=["scatter", "box"])

    if plot_type == "scatter":
        plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    elif plot_type == "box":
        plot = px.box(df, x=x_axis_val, y=y_axis_val)

    st.plotly_chart(plot, use_container_width=True)


st.sidebar.title("Navigation")
options = st.sidebar.radio(
    "Select what you want to display:",
    [
        "About",
        "Data Summary",
        "Data Header",
        "Scatter Plot",
        "Histogram",
        "Two columns",
        "Pairplot",
    ],
)

if options == "About":
    show_about_page()
elif options == "Data Summary":
    show_data_summary_page(df)
elif options == "Data Header":
    show_data_header_page(df)
elif options == "Scatter Plot":
    plot_mpl(df)
elif options == "Histogram":
    histogram(df)
elif options == "Two columns":
    two_columns(df)
elif options == "Pairplot":
    plot_pairplot(df)

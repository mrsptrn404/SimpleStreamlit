import streamlit as st
import pandas as pd
import joblib
from.sklearn.model_selection import train_test_split
from.sklearn.matrics import classification_report, accuracy_score

st.set_page_config(page_title="Predictions", page_icon="🔍")
st.tittle("Predictions")
st.header("Predictions")

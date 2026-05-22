import streamlit as st 
import requests as req


@st.cache_data
def api_calling():
    url="https://fakestoreapi.com/products"

    res=req.get(url)

    res_data=res.json()

    return res_data


st.write(api_calling())


import streamlit as st
import requests
import base64
import pandas as pd
from io import StringIO
import json

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    b64data = base64.b64encode(bytes_data).decode('utf-8')
    response = requests.post("http://api-service/vec", json={"code": 0, "base64": b64data})
    payload = response.content.decode("utf-8")
    payload = json.loads(payload)
    dataframe = pd.DataFrame(payload["results"])
    st.write(dataframe)


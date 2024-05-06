# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import streamlit as st
import plotly.express as px
import pandas as pd
import os

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Global Superstore  👋")

    st.sidebar.success("Select a demo above.")

 


if __name__ == "__main__":
    run()
    
# Sample data
df = pd.read_csv("Processed_GlobalSuperstore.csv")




import matplotlib.pyplot as plt



# Create the bar chart using Matplotlib
fig, ax = plt.subplots()
ax.bar(Region, Quantity, color='skyblue')

# Add labels and title
ax.set_xlabel('Region')
ax.set_ylabel('Quantity')
ax.set_title('Quantity by Region')

# Display the chart using Streamlit's pyplot function
st.pyplot(fig)

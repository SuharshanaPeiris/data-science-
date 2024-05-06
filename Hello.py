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

# Load the dataset
uploaded_file = st.file_uploader("Processed_GlobalSuperstore.csv", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Check the first few rows of the dataframe
    st.write(df.head())

    # Count the occurrences of each order priority
    order_priority_counts = df['Order Priority'].value_counts()

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(order_priority_counts, labels=order_priority_counts.index, autopct='%1.1f%%')

    # Add a title
    ax.set_title('Order Priority Distribution')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Show the chart
    st.pyplot(fig)
# Load the dataset
# Upload CSV file
uploaded_file = st.file_uploader("Processed_GlobalSuperstore.csv", type=["csv"])

# If file is uploaded
if uploaded_file is not None:
    # Read data from CSV file
    df = pd.read_csv(uploaded_file)

    # Group data by 'Country' and calculate total shipping cost
    country_shipping_cost = df.groupby('Country')['Shipping Cost'].sum().reset_index()

    # Plot bar chart
    fig, ax = plt.subplots()
    ax.bar(country_shipping_cost['Country'], country_shipping_cost['Shipping Cost'])

    # Add labels and title
    ax.set_xlabel('Country')
    ax.set_ylabel('Total Shipping Cost')
    ax.set_title('Total Shipping Cost by Country')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Show plot
    st.pyplot(fig)

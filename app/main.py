"""
Streamlit Dashboard for Solar Data Analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add parent directory to path for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from app.utils import load_country_data, calculate_summary_stats, filter_by_date_range

# Page configuration
st.set_page_config(
    page_title="Solar Data Discovery Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("☀️ Solar Data Discovery Dashboard")
st.markdown("### Cross-Country Solar Farm Analysis: Benin, Sierra Leone, and Togo")

# Sidebar
st.sidebar.header("Dashboard Controls")

# Country selection
countries = ["Benin", "Sierra Leone", "Togo"]
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries
)

# Metric selection
metrics = ["GHI", "DNI", "DHI", "Tamb", "RH", "WS"]
selected_metric = st.sidebar.selectbox(
    "Select Metric",
    metrics,
    index=0
)

# Date range filter (if data is loaded)
date_filter_enabled = st.sidebar.checkbox("Enable Date Range Filter", value=False)

# Main content
if not selected_countries:
    st.warning("Please select at least one country from the sidebar.")
else:
    # Load data for selected countries
    country_data = {}
    for country in selected_countries:
        try:
            country_lower = country.lower().replace(" ", "_")
            df = load_country_data(country_lower)
            country_data[country] = df
        except FileNotFoundError:
            st.error(f"Data file not found for {country}. Please ensure cleaned data files are in the data/ directory.")
    
    if country_data:
        # Tabs for different visualizations
        tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Time Series", "Comparison", "Statistics"])
        
        with tab1:
            st.header("Overview")
            st.markdown("### Summary Statistics")
            
            # Summary table
            summary_data = []
            for country, df in country_data.items():
                stats = calculate_summary_stats(df, selected_metric)
                summary_data.append({
                    'Country': country,
                    'Mean': f"{stats['mean']:.2f}",
                    'Median': f"{stats['median']:.2f}",
                    'Std Dev': f"{stats['std']:.2f}",
                    'Min': f"{stats['min']:.2f}",
                    'Max': f"{stats['max']:.2f}"
                })
            
            summary_df = pd.DataFrame(summary_data)
            st.dataframe(summary_df, use_container_width=True)
        
        with tab2:
            st.header("Time Series Analysis")
            
            fig, ax = plt.subplots(figsize=(12, 6))
            for country, df in country_data.items():
                if 'Timestamp' in df.columns and selected_metric in df.columns:
                    df_sorted = df.sort_values('Timestamp')
                    ax.plot(df_sorted['Timestamp'], df_sorted[selected_metric], 
                           label=country, alpha=0.7)
            
            ax.set_xlabel('Timestamp')
            ax.set_ylabel(selected_metric)
            ax.set_title(f'{selected_metric} Over Time')
            ax.legend()
            ax.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        with tab3:
            st.header("Cross-Country Comparison")
            
            # Boxplot comparison
            fig, ax = plt.subplots(figsize=(10, 6))
            data_for_plot = []
            labels = []
            for country, df in country_data.items():
                if selected_metric in df.columns:
                    data_for_plot.append(df[selected_metric].dropna())
                    labels.append(country)
            
            if data_for_plot:
                ax.boxplot(data_for_plot, labels=labels)
                ax.set_ylabel(selected_metric)
                ax.set_title(f'{selected_metric} Comparison Across Countries')
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
        
        with tab4:
            st.header("Detailed Statistics")
            
            for country, df in country_data.items():
                st.subheader(country)
                st.dataframe(df.describe(), use_container_width=True)
    
    else:
        st.info("No data available. Please ensure cleaned data files are placed in the data/ directory.")

# Footer
st.markdown("---")
st.markdown("**MoonLight Energy Solutions** - Solar Data Discovery Week 0 Challenge")
st.markdown("10 Academy: Artificial Intelligence Mastery")


"""
Utility functions for the Streamlit dashboard.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_country_data(country_name: str) -> pd.DataFrame:
    """
    Load cleaned data for a specific country.
    
    Args:
        country_name: Name of the country (benin, sierra_leone, or togo)
    
    Returns:
        DataFrame with country data
    """
    # Try multiple paths to find the data directory
    possible_paths = [
        f"data/{country_name}_clean.csv",
        f"../data/{country_name}_clean.csv",
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", f"{country_name}_clean.csv")
    ]
    
    for file_path in possible_paths:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if 'Timestamp' in df.columns:
                df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            return df
    
    raise FileNotFoundError(f"Data file not found for {country_name}. Tried paths: {possible_paths}")


def calculate_summary_stats(df: pd.DataFrame, metric: str) -> dict:
    """
    Calculate summary statistics for a given metric.
    
    Args:
        df: DataFrame with data
        metric: Name of the metric column
    
    Returns:
        Dictionary with summary statistics
    """
    return {
        'mean': df[metric].mean(),
        'median': df[metric].median(),
        'std': df[metric].std(),
        'min': df[metric].min(),
        'max': df[metric].max()
    }


def filter_by_date_range(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filter DataFrame by date range.
    
    Args:
        df: DataFrame with Timestamp column
        start_date: Start date string
        end_date: End date string
    
    Returns:
        Filtered DataFrame
    """
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    mask = (df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)
    return df.loc[mask]


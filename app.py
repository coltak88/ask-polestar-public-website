import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Ask Polestar - Digital Command Center",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.metric-card {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Header
    st.markdown('<h1 class="main-header">Ask Polestar Digital Command Center</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("Navigation")
        page = st.selectbox(
            "Select Page",
            ["Dashboard", "Analytics", "Data Visualization", "Settings"]
        )
    
    # Main content based on selected page
    if page == "Dashboard":
        show_dashboard()
    elif page == "Analytics":
        show_analytics()
    elif page == "Data Visualization":
        show_data_visualization()
    elif page == "Settings":
        show_settings()

def show_dashboard():
    """Display main dashboard"""
    st.header("Dashboard Overview")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Active Users",
            value="1,234",
            delta="12%"
        )
    
    with col2:
        st.metric(
            label="Data Points",
            value="45.6K",
            delta="8%"
        )
    
    with col3:
        st.metric(
            label="Processing Speed",
            value="98.5%",
            delta="2.1%"
        )
    
    with col4:
        st.metric(
            label="System Health",
            value="Optimal",
            delta="Stable"
        )
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Activity Timeline")
        # Generate sample data
        dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
        activity_data = pd.DataFrame({
            'Date': dates,
            'Activity': np.random.randint(50, 200, len(dates))
        })
        
        fig = px.line(activity_data, x='Date', y='Activity', title="Daily Activity")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Performance Metrics")
        # Generate sample data
        metrics_data = pd.DataFrame({
            'Metric': ['CPU Usage', 'Memory', 'Network', 'Storage'],
            'Value': [65, 78, 45, 82]
        })
        
        fig = px.bar(metrics_data, x='Metric', y='Value', title="System Performance")
        st.plotly_chart(fig, use_container_width=True)

def show_analytics():
    """Display analytics page"""
    st.header("Advanced Analytics")
    
    # Sample analytics content
    st.info("Analytics dashboard coming soon...")
    
    # Placeholder for analytics charts
    sample_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': np.random.randint(10, 100, 5)
    })
    
    fig = px.pie(sample_data, values='Values', names='Category', title="Category Distribution")
    st.plotly_chart(fig, use_container_width=True)

def show_data_visualization():
    """Display data visualization page"""
    st.header("Data Visualization")
    
    # Interactive data visualization
    st.subheader("Interactive Charts")
    
    # Generate sample time series data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Value1': np.cumsum(np.random.randn(len(dates))) + 100,
        'Value2': np.cumsum(np.random.randn(len(dates))) + 50,
        'Value3': np.cumsum(np.random.randn(len(dates))) + 75
    })
    
    # Multi-line chart
    fig = px.line(data, x='Date', y=['Value1', 'Value2', 'Value3'], 
                  title="Multi-Series Time Series")
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation heatmap
    correlation_data = data[['Value1', 'Value2', 'Value3']].corr()
    fig_heatmap = px.imshow(correlation_data, 
                           title="Correlation Matrix",
                           color_continuous_scale='RdBu')
    st.plotly_chart(fig_heatmap, use_container_width=True)

def show_settings():
    """Display settings page"""
    st.header("Settings")
    
    # Settings form
    with st.form("settings_form"):
        st.subheader("Application Settings")
        
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
        refresh_rate = st.slider("Refresh Rate (seconds)", 1, 60, 5)
        enable_notifications = st.checkbox("Enable Notifications", value=True)
        
        submitted = st.form_submit_button("Save Settings")
        
        if submitted:
            st.success("Settings saved successfully!")

if __name__ == "__main__":
    main()
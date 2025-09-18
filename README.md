# Ask Polestar Public Website

A Streamlit-based frontend for the Ask Polestar public website featuring advanced data visualization and real-time analytics.

## Overview

This repository contains the public-facing website component of the Ask Polestar ecosystem, separated from the influence system for better modularity and security.

## Features

- **Interactive Dashboard**: Streamlit-based user interface
- **Data Visualization**: Advanced charts and graphs using Plotly
- **Real-time Analytics**: Live data processing and display
- **Responsive Design**: Modern UI/UX optimized for all devices

## Technology Stack

- **Frontend Framework**: Streamlit
- **Data Visualization**: Plotly, Streamlit components
- **Data Processing**: Pandas, NumPy
- **Styling**: Custom CSS and Streamlit theming

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/coltak88/ask-polestar-public-website.git
   cd ask-polestar-public-website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
ask-polestar-public-website/
├── app.py                    # Main Streamlit application
├── components/               # Reusable UI components
├── pages/                    # Multi-page application structure
├── assets/                   # Static assets (images, CSS)
├── utils/                    # Utility functions
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Contributing

Please read the contributing guidelines and ensure all tests pass before submitting pull requests.

## License

This project is part of the Rasa-X-Machina ecosystem.
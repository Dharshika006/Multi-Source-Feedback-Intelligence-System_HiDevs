# Feedback Intelligence System

# Multi-Source Feedback Intelligence System

## Overview
This system collects and analyzes feedback from multiple sources such as Google Play Store reviews and CSV datasets. It performs sentiment analysis, trend detection, and generates actionable insights for product teams.

## Features
- Play Store review ingestion
- CSV feedback ingestion
- Sentiment analysis
- Trend detection
- Issue prioritization
- Automated PDF reports
- Interactive dashboard

## Architecture
Cyber-Physical feedback intelligence pipeline.

Data Sources → Ingestion → Processing → Intelligence → Visualization

## Technologies
Python
FastAPI
Streamlit
NLTK / TextBlob
Matplotlib
ReportLab

## Running the System

Start API:

Open API docs:

Run dashboard:streamlit run feedback_intelligence/src/dashboard/streamlit_app.py

## Output
- Sentiment chart
- Feedback intelligence report
- Dashboard visualization

## Future Improvements
- Multi-language sentiment detection
- Real-time monitoring
- Automated alerting

run commands :uvicorn feedback_intelligence.main:app --reload
streamlit run feedback_intelligence/src/dashboard/streamlit_app.py


## Demo Video

Watch the project demonstration here: https://youtu.be/bTeMAxmAFnk?feature=shared

### screenshot of dashboard 

## Dashboard Screenshots

### Dashboard View 1
![Dashboard 1](dashboard1.png)

### Dashboard View 2
![Dashboard 2](dashboard2.png)

### Dashboard View 3
![Dashboard 3](dashboard3.png)

### Dashboard View 4
![Dashboard 4](dashboard4.png)

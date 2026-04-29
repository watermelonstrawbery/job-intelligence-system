### Job Intelligence System

An automated data pipeline that fetches, processes, and ranks job listings based on relevance to AI, Data, and Python roles.

The system collects job data from an external API, applies data cleaning and feature engineering, and ranks the most relevant jobs using a custom scoring system. The final output is a Top 10 list exported to a CSV file.

The pipeline runs automatically using Windows Task Scheduler every day at 9 AM. 

# How It Works

## 1. Data Collection
Job listings are fetched from a public REST API.

## 2. Data Cleaning
Raw data is processed and the following fields are extracted:

title
company
description
location

All text is standardized to lowercase for consistency.


## 3. Feature Engineering
Binary features are created to detect relevant keywords:

has_ai
has_python
has_data

## 4. Scoring System
Jobs are ranked using a rule-based scoring model:

AI: +2

Python: +2

Data: +1

## 5. Ranking
Jobs are sorted by total score and the Top 10 most relevant jobs are selected.

## 6. Output
Results are saved as:

outputs/top_jobs_YYYY-MM-DD.csv

## Project Structure
src/
    fetch.py         Fetch jobs from API
    clean.py         Clean and structure data
    features.py      Create features
    scoring.py       Rank jobs
main.py              Main pipeline
requirements.txt     dependencies
outputs/             Generated CSV files

# How to run

## Install dependencies
pip install -r requirements.txt

## Run the project
python main.py

## View results
outputs/top_jobs_YYYY-MM-DD.csv

## Optional: Automation
The script can be scheduled to run automatically using Windows Task Scheduler, generating updated job results daily.

# API
This project uses a public jobs REST API to fetch job listings in real time.

- Data includes: title, company, location, and description
- Data is retrieved in JSON format using HTTP requests

This project uses environment variables to securely store sensitive information such as API credentials.
Instead of hardcoding keys in the source code, the system retrieves them from the operating system using os.getenv().

## Setup Instructions

To run the project locally:

## Set environment variables (Windows)
   
setx API_KEY "your_api_key_here"

setx APP_ID "your_app_id_here"

After setting them, restart your terminal or IDE and run the program

# Tech Stack

- Python
- Pandas
- Requests
- REST API
- Windows Task Scheduler

# Project Goal
To build an automated end-to-end data pipeline that collects job data, processes it, and ranks relevant opportunities for tech roles.

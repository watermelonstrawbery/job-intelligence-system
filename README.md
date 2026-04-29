### Job Intelligence System

An automated system that fetches, processes, and ranks job listings based on relevance to tech roles within AI, Data and Python.

This project collects job data from an API, cleans and processes it, and ranks the most relevant jobs using a custom scoring 
system. The system runs automatically and outputs the top 10 most relevant jobs into a CSV file. The automation is executed 
using Windows Task Scheduler every day at 9 am.  

## How It Works

## 1. Data Collection
Fetches job listings using an API

## 2. Data Cleaning
Extracts relevant fields:
title
company
description
location
Standardizes text (lowercase)


## 3. Feature Engineering

Creates binary features:

has_ai
has_python
has_data

## 4. Scoring System

Jobs are ranked using a rule-based scoring model:

AI: +2
Python: +2
Data: +1

## 5. Ranking

Jobs are sorted based on total score and the Top 10 are selected.

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
requirements-txt     required libraries
outputs/             Generated CSV files

## How to run

# Install dependencies

pip install -r requirements.txt

# Run the project

python main.py

# View results

outputs/top_jobs_YYYY-MM-DD.csv

# Optional: Automation

The script can be scheduled to run automatically using Windows Task Scheduler, generating updated job results daily.

## API

This project uses a public jobs REST API to fetch job listings in real time.

- Data includes: title, company, location, and description
- Data is retrieved in JSON format using HTTP requests

This project uses environment variables to securely store sensitive information such as API credentials.
Instead of hardcoding keys in the source code, the system retrieves them from the operating system using os.getenv().

# Setup Instructions

To run the project locally:

# 1. Set environment variables (Windows)
   
setx API_KEY "your_api_key_here"
setx APP_ID "your_app_id_here"

After setting them, restart your terminal or IDE and run the program

# IRCC-CRS-points-prediction
I became a permanent resident of Canada this year. In the past, I noticed that many people—including myself—constantly checked the IRCC invitation website to monitor the cutoff scores. We wanted to understand how far we were from the required score and what steps we could take to improve our chances.
Inspired by this experience, I am starting to build a program that analyzes historical IRCC invitation data and predicts future cutoff scores across different immigration categories.

# IRCC CRS Dashboard

An **interactive dashboard** that visualizes Canada Express Entry Invitation trends over time, by category (e.g., CEC, PNP, FSW). Built using **Python**, **Dash**, **Plotly**, and **Pandas**.

---

## Features

- Interactive line charts showing **minimum CRS score trends**.
- Displays **invitations issued** for each draw when hovering.
- Filter by **invitation category** (CEC, PNP, FSW, etc.).
- Fully interactive zooming, panning, and tooltips.
- Ready to be deployed online (e.g., Render, Streamlit, Heroku).

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Mac/Linux
# Windows: venv\Scripts\activate

3. Install dependencies: pip install -r requirements.txt


Usage

1. Make sure ircc_analyzer_data.csv is in the data/ folder.

2. Run the dashboard: python dashboard.py

3. Open the browser at:

http://127.0.0.1:8050/
Select a category to view CRS trends. Hover over points to see detailed information.


##Technologies:

Python 3

Pandas

Dash

Plotly


##Project Structure:
IRCC_Project/
│
├─ dashboard.py
├─ requirements.txt
├─ data/
│   └─ ircc_analyzer_data.csv
└─ src/
    ├─ data_loader.py
    ├─ analyzer.py
    └─ visualizer.py



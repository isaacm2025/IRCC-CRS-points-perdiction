# ircc_crs_analyzer/dashboard.py
import dash  

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

from src.data_loader import load_data

# Load data
df = load_data("data/ircc_analyzer_data.csv")

# Create Dash app
app = Dash(__name__)
app.title = "IRCC CRS Dashboard"

# Layout
app.layout = html.Div([
    html.H1("IRCC CRS Score Dashboard", style={'textAlign': 'center'}),
    
    html.Label("Select Round Type:"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': c, 'value': c} for c in df['round_type'].unique()],
        value=df['round_type'].unique()[0],  # default first category
        clearable=False
    ),
    
    dcc.Graph(id='crs-graph')
])

# Callback to update graph based on selected category
@app.callback(
    dash.dependencies.Output('crs-graph', 'figure'),
    [dash.dependencies.Input('category-dropdown', 'value')]
)
def update_graph(selected_category):
    filtered_df = df[df['round_type'] == selected_category].sort_values('date')
    fig = px.line(
        filtered_df,
        x='date',
        y='min_crs_score',
        markers=True,
        hover_data={
            'date': True,
            'min_crs_score': True,
            'invitations_issued': True
        },
        title=f"CRS Score Trend - {selected_category}"
    )
    fig.update_layout(yaxis_title="Minimum CRS Score", xaxis_title="Date")
    return fig

# Run server
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(debug=True, host="0.0.0.0", port=port)

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq
import plotly.express as px
import pandas as pd
import numpy as np

# --- 1. Load Data ---
try:
    df = pd.read_csv("sensor_data.csv")
except FileNotFoundError:
    print("Error: 'sensor_data.csv' not found. Run 'python generate_data.py' first.")
    exit()

df["timestamp"] = pd.to_datetime(df["timestamp"])
component_options = df["component_id"].unique()

# --- 2. Initialize the App ---
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# --- 3. Helper Functions & Components ---

# A helper function to create styled KPI cards
def create_kpi_card(title, value, color):
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-title text-muted"),
            html.H3(value, className="card-text"),
        ]),
        color=color,
        inverse=True,
        className="mb-3"
    )

# --- 4. Define the App Layout ---
app.layout = dbc.Container([
    # --- Header Row ---
    dbc.Row([
        dbc.Col(
            html.H1("☢️ Nuclear Plant Predictive Maintenance Dashboard"),
            width=10, className="my-3"
        ),
        dbc.Col(
            html.Img(src="https://i.imgur.com/n14rE2X.png", height="60px"),
            width=2, className="my-3 text-end"
        )
    ]),

    # --- KPI Row ---
    dbc.Row([
        dbc.Col(create_kpi_card("Plant Power Output", "980 MW", "success")),
        dbc.Col(create_kpi_card("Overall Status", "Nominal", "success")),
        dbc.Col(create_kpi_card("Active Alerts", "0", "secondary")),
        dbc.Col(create_kpi_card("Inspections Due", "2", "warning")),
    ]),

    # --- Main Content Row ---
    dbc.Row([
        # --- Left Column (Controls & Gauges) ---
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Component Selector", className="card-title"),
                    dcc.Dropdown(
                        id="component-dropdown",
                        options=[{"label": c, "value": c} for c in component_options],
                        value=component_options[0],
                        clearable=False,
                    ),
                    html.Hr(),
                    html.H4("Real-time Status", className="card-title"),
                    # Gauges for Temperature and Pressure
                    dash_daq.Gauge(
                        id="temp-gauge",
                        label="Temperature (°C)",
                        min=0, max=600,
                        color={"gradient":True,"ranges":{"green":[0,300],"yellow":[300,450],"red":[450,600]}},
                        value=80
                    ),
                    dash_daq.Gauge(
                        id="pressure-gauge",
                        label="Pressure (kPa)",
                        min=1000, max=2000,
                        color={"gradient":True,"ranges":{"green":[1000,1600],"yellow":[1600,1800],"red":[1800,2000]}},
                        value=1500
                    ),
                ])
            ], className="mb-3"),
            
            # AI Prediction Card
            dbc.Card([
                dbc.CardBody([
                    html.H4("AI Prediction", className="card-title"),
                    html.P("AI-driven forecast based on component data:"),
                    html.H3(id="rul-text", className="text-warning"), # Will be updated
                    html.P("Remaining Useful Life (Hours)", className="text-muted")
                ])
            ])

        ], md=4), # This column takes 4 of 12 grid spaces

        # --- Right Column (Historical Graphs) ---
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Historical Sensor Data", className="card-title"),
                    html.P("Vibration (mm/s) over time"),
                    dcc.Graph(id="vibration-graph"),
                    html.P("Pressure (kPa) over time"),
                    dcc.Graph(id="pressure-graph"),
                ])
            ])
        ], md=8), # This column takes 8 of 12 grid spaces
    ])

], fluid=True)

# --- 5. Define Callbacks (Interactivity) ---
@app.callback(
    [Output("temp-gauge", "value"),
     Output("pressure-gauge", "value"),
     Output("rul-text", "children"),
     Output("vibration-graph", "figure"),
     Output("pressure-graph", "figure")],
    [Input("component-dropdown", "value")]
)
def update_component_data(selected_component):
    # Filter data to the selected component
    df_filtered = df[df["component_id"] == selected_component]
    
    # Get the *most recent* sensor readings for the gauges
    latest_temp = df_filtered["temperature_C"].iloc[-1]
    latest_pressure = df_filtered["pressure_kPa"].iloc[-1]
    
    # Simulate a "Remaining Useful Life" prediction
    # (In a real app, this would come from an AI model)
    rul_prediction = "1,200 Hours"
    if selected_component == "PUMP-A01":
        # Because we added degradation to this pump, we'll show a lower RUL
        rul_prediction = "450 Hours" 
    elif selected_component == "TURBINE-G01":
        rul_prediction = "8,900 Hours"
        
    # Create the historical graphs
    vib_fig = px.line(df_filtered, x="timestamp", y="vibration_mm_s", 
                      title=f"Vibration for {selected_component}")
    vib_fig.update_layout(template="plotly_dark")
    
    pressure_fig = px.line(df_filtered, x="timestamp", y="pressure_kPa", 
                           title=f"Pressure for {selected_component}")
    pressure_fig.update_layout(template="plotly_dark")
    
    # Return all the new values
    return latest_temp, latest_pressure, rul_prediction, vib_fig, pressure_fig

# --- 6. Run the App ---
if __name__ == "__main__":
    app.run(debug=True)

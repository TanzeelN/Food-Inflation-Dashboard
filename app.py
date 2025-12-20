from dash import Dash, html, dcc, callback, Output, Input, Patch, clientside_callback, State
from dash_svg import Svg, Path
import vizro
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from components.ui_components import color_mode_switch
from components.graph_components import continent_Line_Graph, continent_time_series, countries_Bar_Chart
from callbacks.ui_callbacks import colour_mode_callback
from utils.Meal_Icon_Path import Meal_Icon_Path

# region Underlying Data

# Cleaned Data
data = pd.read_csv("Data/Inflation_Data_Cleaned.csv", index_col=False)

#Continent List
continent_Names = data["CONTINENT"].unique()

#Total Year Range
min_year = int(data['YEAR'].min())
max_year = int(data['YEAR'].max())

# endregion



app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO,dbc.icons.FONT_AWESOME])

app.layout = dbc.Container(
        [
            dbc.Row(
                [   
                    dbc.Col(
                        [   
                            #Light or Dark theme switch (add Icon)
                            html.Div(
                                color_mode_switch(),
                                style = {
                                    "marginBottom": "1rem"
                                }
                                ),
                            #Title & Icon
                            html.H1(
                                "Global Food Inflation: A 20-Year Overview (2005–2025)",
                                style={
                                    "font-weight": "bold",
                                    "font-size": "33px",
                                    "text-align": "left",
                                    "line-height": "1.2",
                                    "margin-bottom": "20px" 
                                }
                            ),
                            html.Div(
                                Svg(
                                    #Current Color matches dark/light mode
                                    children=[Path(d=Meal_Icon_Path, fill="currentcolor")],
                                    width="150px",
                                    height="150px"
                                ),
                                style={
                                    "display": "flex",            
                                    "justify-content": "center",  
                                    "align-items": "center",      
                                    "width": "100%",              
                                    "flex-shrink": 0,
                                    "margin-left": "10px"              
                                },
                                id = "icon-color"
                            
                            ),
                            
                            #Filter Components
                            html.Div(
                                [   
                                    #Continent Selection
                                    html.H2(
                                        "Continent Selection",
                                        style = {
                                            "text-align":"center",
                                            "font-size": "20px",
                                            "font-weight": "bold",
                                            "margin-top": "-100px"
                                        }
                                    ),
                                    
                                    dcc.Dropdown(
                                        options=continent_Names,
                                        value="Europe",
                                        clearable=False,
                                        id="continents-and-dropdown-item",
                                        className="blue-dropdown"
                                    ),
                                    
                                    #Year Selection
                                    html.H2(
                                        "Year Range",
                                        style = {
                                            "text-align":"center",
                                            "font-size": "20px",
                                            "font-weight": "bold",
                                            "margin-top": "40px"
                                        }
                                    ),
                                    html.Div(
                                        dcc.RangeSlider(
                                            min = min_year,
                                            max = max_year,
                                            value = [min_year,max_year],
                                            step = 1,
                                            marks = None,
                                            id = "year-slider",
                                            tooltip = {"placement": "bottom","always_visible": True}),
                                        style = {
                                            "margin-bottom":"30px"
                                        }
                                    ),
                                    
                                    #Button to compute result after selecting filters
                                    dbc.Button(
                                        children = "Display",
                                        id = "compute-button",
                                        size = "sm",
                                        className = "blue-button"
                                        
                                    )
                                ],
                                style = {
                                    "display": "flex",
                                    "flexDirection": "column",
                                    "justifyContent": "center",
                                    "flex": 1
                                }
                            ),
                            
                            html.Div(id="color-mode-switch-output", style={"display": "none"})
                        ],
                        width = 3,
                        style = {
                            "display": "flex",
                            "flexDirection": "column",
                            "min-height": "100vh",
                            "padding-left": "40px",
                            "border-right": "1px solid #d3d3d3",
                            "overflow": "visible",
                        }
                    ),
                    #Graph Section of the dashboard
                    dbc.Col(
                        [
                            #Line Graph at the top half
                            dbc.Row(
                                dcc.Graph(id = "continent-line-graph",
                                          config={
                                              "displayModeBar":False}, ),
                            ),
                            #Second half of the dashboard
                            dbc.Row(
                                [
                                    #Time Series Graph
                                    dbc.Col(
                                        dcc.Graph(id = "time-series-map",
                                                  config={
                                                      "displayModeBar":False}),
                                        width = 6
                                    ),
                                    dbc.Col(
                                        dcc.Graph(id = "bar-chart-countries",
                                                  config={
                                                      "displayModeBar":False}),
                                        width = 6
                                    ),
                                    
                                ],
                                className="g-0"
                            ),
                        ],
                        width = 9,
                        
                        
                    )
                ]
            )
        ],
        #Container Style
        style=
        {
            "margin": 0,  # remove row margins
            "padding": 0,  # remove row padding
            "width": "100%"# ensure row spans entire container width
        },
        fluid=True
    )





colour_mode_callback(app)
    

@callback(
    Output("continent-line-graph", "figure"),
    Output("time-series-map", "figure"),
    Output("bar-chart-countries", "figure"),
    Input("compute-button", "n_clicks"),
    State("continents-and-dropdown-item", "value"),
    State("year-slider", "value")
)
def update_all_graphs(n_clicks, continent, year_range):

    fig_line = continent_Line_Graph(
        Continent=continent,
        Year_Range=year_range,
        data=data
    )

    fig_map = continent_time_series(
        Continent=continent,
        Year_Range=year_range,
        data=data
    )

    fig_bar = countries_Bar_Chart(
        Continent=continent,
        Year_Range=year_range,
        data=data
    )

    return fig_line, fig_map, fig_bar




if __name__ == "__main__":
    app.run(debug=True)

import pandas as pd
import plotly.express as px


def continent_Line_Graph(Continent, Year_Range, data):
    if Continent == "World":
        current_Continent = ["World"]
    else:
        current_Continent = [Continent, "World"]
    
    start_Year,end_Year = Year_Range
    
    data_Subset = data[
        data["CONTINENT"].isin(current_Continent)
    ]
        
    average_Continents = data_Subset.groupby(["CONTINENT", "YEAR"])["CPI_PERC"].mean().round(2).reset_index()
    
    average_Continents_Filtered = average_Continents[
        (average_Continents["YEAR"] >= start_Year) & (average_Continents["YEAR"] <= end_Year)
        ]
    
    Line_Graph = px.line(
        average_Continents_Filtered,
        x = "YEAR",
        y = "CPI_PERC",
        color = "CONTINENT"
    )
    
    return Line_Graph


def continent_time_series(Continent, Year_Range, data):
    start_Year,end_Year = Year_Range
    
    data_Subset = data[
        data["CONTINENT"].isin([Continent])
    ]
    
    data_Subset = data_Subset[
        (data_Subset["YEAR"] >= start_Year) & (data_Subset["YEAR"] <= end_Year)
    ]
    
    Time_Series_Map = px.choropleth(
        data_frame = data_Subset,
        locations = "REF_AREA",
        locationmode = "ISO-3",
        animation_frame = "YEAR",
        color="CPI_PERC"
    )
    
    Time_Series_Map.update_geos(
        scope = Continent.lower(),
        projection_type = "natural earth"
    )
        
    
    return Time_Series_Map

def countries_Bar_Chart(Continent, Year_Range, data):
    start_Year,end_Year = Year_Range
    
    data_Subset = data[
        data["CONTINENT"].isin([Continent])
    ]
    
    data_Subset = data_Subset[
        (data_Subset["YEAR"] >= start_Year) & (data_Subset["YEAR"] <= end_Year)
    ]
    
    n_Largest = 10
    
    Current_Continent_Top = data_Subset.groupby(["REF_AREA_LABEL"])["CPI_PERC"].agg(["min","max"]).reset_index()
    Current_Continent_Top["GROWTH_PERC"] = (Current_Continent_Top["max"] - Current_Continent_Top["min"]).round(2)
    Countries_Top_N = Current_Continent_Top.nlargest(n_Largest, "GROWTH_PERC", "all")
    
    Countries_Top_N_Melted = Countries_Top_N.melt(
        id_vars = "REF_AREA_LABEL",
        value_vars = ["max"],
        value_name = "CPI_PERC",
        var_name = "CPI_LEVEL"
    )
    
    Countries_Bar_Chart = px.bar(
        Countries_Top_N_Melted,
        x = "REF_AREA_LABEL",
        y = "CPI_PERC"
    )
    
    return Countries_Bar_Chart
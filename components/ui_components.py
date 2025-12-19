from dash import html
import dash_bootstrap_components as dbc


def color_mode_switch():
    return html.Span(
        [
            dbc.Label(className="fa fa-moon", html_for="color-mode-switch"),
            dbc.Switch( id="color-mode-switch", value=False, className="d-inline-block ms-1", persistence=True),
            dbc.Label(className="fa fa-sun", html_for="color-mode-switch"),
            
        ]
    )
    
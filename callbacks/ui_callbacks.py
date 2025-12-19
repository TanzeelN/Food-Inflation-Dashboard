from dash import Input, Output

def colour_mode_callback(app):
    app.clientside_callback(
        """
        function(switchOn) {
            document.documentElement.setAttribute('data-bs-theme', switchOn ? 'light' : 'dark');
            return null;
        }
        """,
        Output("color-mode-switch-output", "children"),
        Input("color-mode-switch", "value")
    )

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from apps.home import create_home_page
from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = dbc.Container(
    [
        html.H5(
                    "Digital Filter Designer",
                    className="text-center bg-dark text-white p-2",
                ),
        create_home_page(),dcc.Store(id='store_num_real'),dcc.Store(id='store_den_real'),dcc.Store(id='store_num_imag'),dcc.Store(id='store_den_imag'),
        dcc.Store(id='store_zeros'), dcc.Store(id='store_poles'), dcc.Store(id='store_corrected_zeros'), dcc.Store('store_corrected_poles')
    ],
    className="p-0",
    
    fluid=True,
                      )


if __name__ == '__main__':
    app.run_server(debug=True)
    
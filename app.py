import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import fetch
import plotly.express as px

external_stylesheets = [dbc.themes.BOOTSTRAP]

colors = {
    'background': 'black',
    'text': 'white'
}

# Initialise the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# fetch data
SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD = fetch.get_lw_data()

fig_SP500   = px.line(SP500[1:], title="SP500", x=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday'], y = 'Adj Close')
fig_DJIA    = px.line(DJIA[1:], title="DJIA", x=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday'], y = 'Adj Close')
fig_NASDAQ  = px.line(NASDAQ[1:], title="NASDAQ", x=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday'], y = 'Adj Close')
fig_EURUSD  = px.line(EURUSD[1:], title="EURUSD", x=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday'], y = 'Adj Close')
fig_OIL     = px.line(OIL[1:], title="OIL", x=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday'], y = 'Adj Close')
fig_GOLD    = px.line(GOLD[1:], title="GOLD", x=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday'], y = 'Adj Close')

fig_SP500.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig_DJIA.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig_NASDAQ.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig_EURUSD.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig_OIL.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig_GOLD.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


navbar1 = html.Div(
    [
        dbc.Row(dbc.Col(html.H1("LOGO WILL BE HERE", style = {'color':colors['text'], 'marginTop':50}))),
        dbc.Row([dbc.Col(dbc.Button('Dashboard', block = True), style = {'marginLeft':10}), dbc.Col(dbc.Button('Methodology', block = True)), dbc.Col(dbc.Button('Gamma Market Technologies', block = True), style = {'marginRight':10})]),
    ], style={'textAlign':'center', 'marginTop': 50, 'backgroundColor':colors['background']}
)

# Define the app
app.layout = html.Div(style = {'backgroundColor': colors['background'], 'marginTop': -50},



children=[

  navbar1, 

  dcc.Graph(
    id = 'SP500',
    figure = fig_SP500
  ),

  dcc.Graph(
    id = 'DJIA',
    figure = fig_DJIA
  ),

  dcc.Graph(
    id = 'NASDAQ',
    figure = fig_NASDAQ
  ),

  dcc.Graph(
    id = 'EURUSD',
    figure = fig_EURUSD
  ),

  dcc.Graph(
    id = 'OIL',
    figure = fig_OIL
  ),

  dcc.Graph(
    id = 'GOLD',
    figure = fig_GOLD
  )

  ]
  )


  

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import fetch
import plotly.express as px

import components.styles as styles
import components.charts as chrt
import components.headlines as headlines
import components.headline_field as hf

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# fetch data
mssmw_date, lw_enddate, SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD = fetch.get_MSSMW()

mssmw_date = str(mssmw_date.iloc[0])[:10]
lw_enddate = str(lw_enddate)[:10]

fig_SP500   = chrt.comparative_main(SP500, "Standard and Poor's 500", draw_label = True)
fig_DJIA    = chrt.comparative_main(DJIA, "Dow Jones Industrial Average")
fig_NASDAQ  = chrt.comparative_main(NASDAQ, "NASDAQ Composite Index")
fig_EURUSD  = chrt.comparative_main(EURUSD, "EUR/USD")
fig_OIL     = chrt.comparative_main(OIL, "Crude Oil Spot Price")
fig_GOLD    = chrt.comparative_main(GOLD, "Gold Spot Price")

#fetch headlines
hist_headline_base = headlines.get_headlines(mssmw_date)

# Define the app
app.layout = html.Div(style = {'backgroundColor': styles.colors['background'], 'marginTop': -50},

children=[

  html.Div([dbc.Row([dbc.Col([html.Img(src=app.get_asset_url('mssmw.png'), height=150, style = {'margin':20})]),
    dbc.Col(),
    dbc.Col(html.P('dashboard', style = styles.navbar_sections)),
    dbc.Col(html.P('methodology', style = styles.navbar_sections)),
    dbc.Col(html.P('about gmt', style = styles.navbar_sections)),
    dbc.Col(),
    dbc.Col()])],
    style = {'marginTop':50, 'backgroundColor':styles.colors['navbar']}),

  dbc.Row([dbc.Col([html.P('The week ended '+ lw_enddate +' is most similar to the week ended '+ mssmw_date + '.', style = styles.similarity_text)])], style = styles.headliner_center), # this row specifies which week was the last one most similar to

  dbc.Row([ # this will be the main row with headline columns and graph column
    
    dbc.Col([hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base),
              hf.headline_field(hist_headline_base)], style = styles.content_field_left), #historical headlines?
    
    dbc.Col([dcc.Graph(
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
  )], style= styles.content_field_center, width=6), #graphs
    dbc.Col(html.P('modern headlines will be here!', style={'text-align':'center'}), style = styles.content_field_right)  #modern headlines
  ]), 

  
  ]
  )


  

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import numpy as np
import time
from datetime import datetime

import fetch
from components import styles
from components import charts as chrt
from components import headlines
from components import headline_field as hf


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# fetch data
MSSMW_DATE, LW_ENDDATE, SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD = fetch.get_MSSMW()

MSSMW_DATE = str(MSSMW_DATE.iloc[0])[:10]
LW_ENDDATE = str(LW_ENDDATE)[:10]

fig_SP500   = chrt.comparative_main(SP500, "Standard and Poor's 500", draw_label = True)
fig_DJIA    = chrt.comparative_main(DJIA, "Dow Jones Industrial Average")
fig_NASDAQ  = chrt.comparative_main(NASDAQ, "NASDAQ Composite Index")
fig_EURUSD  = chrt.comparative_main(EURUSD, "EUR/USD")
fig_OIL     = chrt.comparative_main(OIL, "Crude Oil Spot Price")
fig_GOLD    = chrt.comparative_main(GOLD, "Gold Spot Price")

#fetch headlines and create used/unused databases
hist_headline_base = headlines.get_headlines(MSSMW_DATE)


# Define the app
app.layout = html.Div(style = {'backgroundColor': styles.colors['background'], 'marginTop': -50},

children=[

  html.Div([
      dbc.Row([
        dbc.Col([html.Img(src=app.get_asset_url('mssmw.png'), height=150, style = {'margin':20})]),
        dbc.Col(),
        dbc.Col(html.P('dashboard', style = styles.navbar_sections)),
        dbc.Col(html.P('methodology', style = styles.navbar_sections)),
        dbc.Col(html.P('about gmt', style = styles.navbar_sections)),
        dbc.Col(),
        dbc.Col()])],
      style = {'marginTop':50, 'backgroundColor':styles.colors['navbar']}),

  dbc.Row([
      dbc.Col([
        html.P('The week ended ' +
              LW_ENDDATE +
              ' is most similar to the week ended '+
              MSSMW_DATE + '.', style = styles.similarity_text)
              ])
              ], style = styles.headliner_center),
  dbc.Row([ # this will be the main row with headline columns and graph column

    dbc.Col([hf.headline_field(hist_headline_base, 'headline_1', 'fader_1'), 
             hf.headline_field(hist_headline_base, 'headline_2', 'fader_2'),
             hf.headline_field(hist_headline_base, 'headline_3', 'fader_3'), 
             hf.headline_field(hist_headline_base, 'headline_4', 'fader_4'), 
             hf.headline_field(hist_headline_base, 'headline_5', 'fader_5'), 
             hf.headline_field(hist_headline_base, 'headline_6', 'fader_6'),
             hf.headline_field(hist_headline_base, 'headline_7', 'fader_7'),
             hf.headline_field(hist_headline_base, 'headline_8', 'fader_8'), 
             hf.headline_field(hist_headline_base, 'headline_9', 'fader_9'),                      
              dcc.Interval(id = 'interval-component-1',
                           interval=0.5*1000,
                           n_intervals=0)], style = styles.content_field_left),
              
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
    dbc.Col(html.P('modern'), style = styles.content_field_right)
  ]),
  ]
  )



#headline animation and replacement for hist_headline_1
@app.callback(
    Output("fader_1", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_1", "is_in"))
def toggle_fade(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value']
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_1", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_1", "is_in"),
    State("headline_1", "children"))
def change_text(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_1', 'fader_1', headline_only=True)
      return output


#headline animation and replacement for hist_headline_2
@app.callback(
    Output("fader_2", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_2", "is_in"))
def toggle_fade2(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 1
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_2", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_2", "is_in"),
    State("headline_2", "children"))
def change_text2(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_2', 'fader_2', headline_only=True)
      return output

#headline animation and replacement for hist_headline_3
@app.callback(
    Output("fader_3", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_3", "is_in"))
def toggle_fade3(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 2
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_3", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_3", "is_in"),
    State("headline_3", "children"))
def change_text3(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_3', 'fader_3', headline_only=True)
      return output

#headline animation and replacement for hist_headline_4
@app.callback(
    Output("fader_4", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_4", "is_in"))
def toggle_fade4(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 3
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_4", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_4", "is_in"),
    State("headline_4", "children"))
def change_text4(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_4', 'fader_4', headline_only=True)
      return output

#headline animation and replacement for hist_headline_5
@app.callback(
    Output("fader_5", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_5", "is_in"))
def toggle_fade5(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 4
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_5", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_5", "is_in"),
    State("headline_5", "children"))
def change_text5(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_5', 'fader_5', headline_only=True)
      return output

#headline animation and replacement for hist_headline_6
@app.callback(
    Output("fader_6", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_6", "is_in"))
def toggle_fade6(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 5
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_6", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_6", "is_in"),
    State("headline_6", "children"))
def change_text6(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_6', 'fader_6', headline_only=True)
      return output


#headline animation and replacement for hist_headline_7
@app.callback(
    Output("fader_7", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_7", "is_in"))
def toggle_fade7(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 6
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_7", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_7", "is_in"),
    State("headline_7", "children"))
def change_text7(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_7', 'fader_7', headline_only=True)
      return output


#headline animation and replacement for hist_headline_8
@app.callback(
    Output("fader_8", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_8", "is_in"))
def toggle_fade8(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 7
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_8", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_8", "is_in"),
    State("headline_8", "children"))
def change_text8(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_8', 'fader_8', headline_only=True)
      return output


#headline animation and replacement for hist_headline_9
@app.callback(
    Output("fader_9", "is_in"),
    Input("interval-component-1", "n_intervals"),
    State("fader_9", "is_in"))
def toggle_fade9(n_int, is_in):
    ctx = dash.callback_context
    val = ctx.triggered[0]['value'] - 8
    if is_in == False:
      return True
    elif val is None:
      return True
    elif int(val) % 10 == 0:
      return False
    else:
      return True

@app.callback(
    Output("headline_9", "children"),
    Input("interval-component-1", "n_intervals"),
    State("fader_9", "is_in"),
    State("headline_9", "children"))
def change_text9(n_int, is_in, hist_children):
    if is_in:
      return hist_children
    else:
      output = hf.headline_field(hist_headline_base, 'headline_9', 'fader_9', headline_only=True)
      return output

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
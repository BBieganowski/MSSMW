import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import numpy as np
import time
from datetime import datetime
from memory_profiler import profile

import fetch
from components import styles
from components import charts as chrt
from components import headlines
from components import headline_field as hf


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, update_title=None)
server = app.server
app.title = 'MSSMW'

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
modern_headline_base = headlines.get_modern_headlines()


# Define the app
app.layout = html.Div(style = {'backgroundColor': styles.colors['background'], 'marginTop': -50},

children=[

  dbc.Row([dbc.Col(), html.Img(src=app.get_asset_url('logo1.png'), style = {'height':300, 'justify':'center', 'marginTop':30}), dbc.Col()], style = styles.navbar),

  dbc.Row([dbc.Col([html.P('Historical Headlines', style = styles.similarity_text)], style = styles.content_field_left),
           dbc.Col([html.P('The week ended ' + LW_ENDDATE + ' is the most similar to the week ended '+ MSSMW_DATE + '.', style = styles.similarity_text)], style = styles.content_field_center, width = 6),
           dbc.Col([html.P('Modern Headlines', style = styles.similarity_text)],style = styles.content_field_right)]),
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
             hf.headline_field(hist_headline_base, 'headline_10', 'fader_10'), 
             hf.headline_field(hist_headline_base, 'headline_11', 'fader_11'), 
             hf.headline_field(hist_headline_base, 'headline_12', 'fader_12'),                    
             dcc.Interval(id = 'interval-component-1',
                           interval=4*1000,
                           n_intervals=0),
             dcc.Interval(id = 'interval-component-2',
                           interval=2*1000,
                           n_intervals=0)], style = styles.content_field_left),
              
    dbc.Col([dcc.Graph(
    id = 'SP500',
    figure = fig_SP500,
    config= {
    'displayModeBar': False,
    'displaylogo': False,                                       
  }
  ),

  dcc.Graph(
    id = 'DJIA',
    figure = fig_DJIA,
    config= {
    'displayModeBar': False,
    'displaylogo': False,                                       
  }
  ),

  dcc.Graph(
    id = 'NASDAQ',
    figure = fig_NASDAQ,
    config= {
    'displayModeBar': False,
    'displaylogo': False, 
  }
  ),

  dcc.Graph(
    id = 'EURUSD',
    figure = fig_EURUSD,
    config= {
    'displayModeBar': False,
    'displaylogo': False,                                       
  }
  ),

  dcc.Graph(
    id = 'OIL',
    figure = fig_OIL,
    config= {
    'displayModeBar': False,
    'displaylogo': False,                                       
  }
  ),

  dcc.Graph(
    id = 'GOLD',
    figure = fig_GOLD,
    config= {
    'displayModeBar': False,
    'displaylogo': False,                                       
  }
  )], style= styles.content_field_center, width=6), #graphs
    
    dbc.Col([hf.modern_headline_field(modern_headline_base,'modern-headline-1', 'modern-fader-1'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-2', 'modern-fader-2'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-3', 'modern-fader-3'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-4', 'modern-fader-4'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-5', 'modern-fader-5'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-6', 'modern-fader-6'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-7', 'modern-fader-7'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-8', 'modern-fader-8'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-9', 'modern-fader-9'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-10', 'modern-fader-10'),
             hf.modern_headline_field(modern_headline_base,'modern-headline-11', 'modern-fader-11')], style = styles.content_field_right)


  ]),
  ]
  )

@app.callback(
  Output('modern-fader-1', 'children'),
  Output('modern-fader-1', 'is_in'),
  Output('modern-fader-2', 'children'),
  Output('modern-fader-2', 'is_in'),
  Output('modern-fader-3', 'children'),
  Output('modern-fader-3', 'is_in'),
  Output('modern-fader-4', 'children'),
  Output('modern-fader-4', 'is_in'),
  Output('modern-fader-5', 'children'),
  Output('modern-fader-5', 'is_in'),
  Output('modern-fader-6', 'children'),
  Output('modern-fader-6', 'is_in'),
  Output('modern-fader-7', 'children'),
  Output('modern-fader-7', 'is_in'),
  Output('modern-fader-8', 'children'),
  Output('modern-fader-8', 'is_in'),
  Output('modern-fader-9', 'children'),
  Output('modern-fader-9', 'is_in'),
  Output('modern-fader-10', 'children'),
  Output('modern-fader-10', 'is_in'),
  Output('modern-fader-11', 'children'),
  Output('modern-fader-11', 'is_in'),
  Input('interval-component-1', 'n_intervals'),
  Input('interval-component-2', 'n_intervals'),
  State('modern-fader-1', 'children'),
  State('modern-fader-1', 'is_in'),
  State('modern-fader-2', 'children'),
  State('modern-fader-2', 'is_in'),
  State('modern-fader-3', 'children'),
  State('modern-fader-3', 'is_in'),
  State('modern-fader-4', 'children'),
  State('modern-fader-4', 'is_in'),
  State('modern-fader-5', 'children'),
  State('modern-fader-5', 'is_in'),
  State('modern-fader-6', 'children'),
  State('modern-fader-6', 'is_in'),
  State('modern-fader-7', 'children'),
  State('modern-fader-7', 'is_in'),
  State('modern-fader-8', 'children'),
  State('modern-fader-8', 'is_in'),
  State('modern-fader-9', 'children'),
  State('modern-fader-9', 'is_in'),
  State('modern-fader-10', 'children'),
  State('modern-fader-10', 'is_in'),
  State('modern-fader-11', 'children'),
  State('modern-fader-11', 'is_in'),
)
def updater(n_intervals, n_intervals_2, children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11):
  ctx = dash.callback_context.triggered
  if ctx[0]['prop_id'] == 'interval-component-1.n_intervals':
    parameter_list = [children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11]
    chosen_index = int(np.random.randint(0, 11))*2+1
    parameter_list[chosen_index] = False
    return parameter_list[0], parameter_list[1], parameter_list[2], parameter_list[3], parameter_list[4], parameter_list[5], parameter_list[6], parameter_list[7], parameter_list[8], parameter_list[9], parameter_list[10], parameter_list[11], parameter_list[12], parameter_list[13], parameter_list[14], parameter_list[15], parameter_list[16], parameter_list[17], parameter_list[18], parameter_list[19], parameter_list[20], parameter_list[21]
  else:
    parameter_list = [children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11]
    try:
      chosen_index = parameter_list.index(False)
      parameter_list[chosen_index] = True
      name_id = int(chosen_index+1)/2
      parameter_list[chosen_index-1] = hf.modern_headline_field(modern_headline_base,'modern-headline-'+str(name_id), 'modern-fader-'+str(name_id))
      return parameter_list[0], parameter_list[1], parameter_list[2], parameter_list[3], parameter_list[4], parameter_list[5], parameter_list[6], parameter_list[7], parameter_list[8], parameter_list[9], parameter_list[10], parameter_list[11], parameter_list[12], parameter_list[13], parameter_list[14], parameter_list[15], parameter_list[16], parameter_list[17], parameter_list[18], parameter_list[19], parameter_list[20], parameter_list[21]
    except ValueError:
      return children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11


@app.callback(
  Output('fader_1', 'children'),
  Output('fader_1', 'is_in'),
  Output('fader_2', 'children'),
  Output('fader_2', 'is_in'),
  Output('fader_3', 'children'),
  Output('fader_3', 'is_in'),
  Output('fader_4', 'children'),
  Output('fader_4', 'is_in'),
  Output('fader_5', 'children'),
  Output('fader_5', 'is_in'),
  Output('fader_6', 'children'),
  Output('fader_6', 'is_in'),
  Output('fader_7', 'children'),
  Output('fader_7', 'is_in'),
  Output('fader_8', 'children'),
  Output('fader_8', 'is_in'),
  Output('fader_9', 'children'),
  Output('fader_9', 'is_in'),
  Output('fader_10', 'children'),
  Output('fader_10', 'is_in'),
  Output('fader_11', 'children'),
  Output('fader_11', 'is_in'),
  Input('interval-component-1', 'n_intervals'),
  Input('interval-component-2', 'n_intervals'),
  State('fader_1', 'children'),
  State('fader_1', 'is_in'),
  State('fader_2', 'children'),
  State('fader_2', 'is_in'),
  State('fader_3', 'children'),
  State('fader_3', 'is_in'),
  State('fader_4', 'children'),
  State('fader_4', 'is_in'),
  State('fader_5', 'children'),
  State('fader_5', 'is_in'),
  State('fader_6', 'children'),
  State('fader_6', 'is_in'),
  State('fader_7', 'children'),
  State('fader_7', 'is_in'),
  State('fader_8', 'children'),
  State('fader_8', 'is_in'),
  State('fader_9', 'children'),
  State('fader_9', 'is_in'),
  State('fader_10', 'children'),
  State('fader_10', 'is_in'),
  State('fader_11', 'children'),
  State('fader_11', 'is_in'),
)
def updater2(n_intervals, n_intervals_2, children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11):
  ctx = dash.callback_context.triggered
  if ctx[0]['prop_id'] == 'interval-component-1.n_intervals':
    parameter_list = [children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11]
    chosen_index = int(np.random.randint(0, 11))*2+1
    parameter_list[chosen_index] = False
    return parameter_list[0], parameter_list[1], parameter_list[2], parameter_list[3], parameter_list[4], parameter_list[5], parameter_list[6], parameter_list[7], parameter_list[8], parameter_list[9], parameter_list[10], parameter_list[11], parameter_list[12], parameter_list[13], parameter_list[14], parameter_list[15], parameter_list[16], parameter_list[17], parameter_list[18], parameter_list[19], parameter_list[20], parameter_list[21]
  else:
    parameter_list = [children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11]
    try:
      chosen_index = parameter_list.index(False)
      parameter_list[chosen_index] = True
      name_id = int(chosen_index+1)/2
      parameter_list[chosen_index-1] = hf.headline_field(hist_headline_base,'headline_'+str(name_id), 'fader_'+str(name_id))
      return parameter_list[0], parameter_list[1], parameter_list[2], parameter_list[3], parameter_list[4], parameter_list[5], parameter_list[6], parameter_list[7], parameter_list[8], parameter_list[9], parameter_list[10], parameter_list[11], parameter_list[12], parameter_list[13], parameter_list[14], parameter_list[15], parameter_list[16], parameter_list[17], parameter_list[18], parameter_list[19], parameter_list[20], parameter_list[21]
    except ValueError:
      return children_1, is_in_1, children_2, is_in_2, children_3, is_in_3, children_4, is_in_4, children_5, is_in_5, children_6, is_in_6, children_7, is_in_7, children_8, is_in_8, children_9, is_in_9, children_10, is_in_10, children_11, is_in_11




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import components.styles as styles
import components.headlines as headlines

base1 = headlines.get_headlines('2016-03-12')

def headline_field(base):
    base = base[base['words_in_headline'] > 7]
    sample = base.sample(1)

    headline_text = sample['headline'].iloc[0].replace('’S', '’s')

    field = dbc.Row([html.P(headline_text, style = styles.headline),
                     html.P("New York Times - " + str(sample['date'].iloc[0])[:10], style = styles.headline_subscript)])
    return field

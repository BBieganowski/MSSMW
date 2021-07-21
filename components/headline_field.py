import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import components.styles as styles
import components.headlines as headlines

def headline_field(base, headline_id = '', fader_id = '', headline_only = False):
    base = base[base['words_in_headline'] > 7]
    sample = base.sample(1)

    headline_text = sample['headline'].iloc[0].replace('’S', '’s').replace('\'S', '\'s')
    headline_obj = html.P(headline_text, style = styles.headline)
    field = dbc.Row([headline_obj,
                     html.P("New York Times - " + str(sample['date'].iloc[0])[:10], style = styles.headline_subscript)], id=headline_id, style=styles.headline_content_field)

    fade = dbc.Fade(field, id = fader_id, is_in=True, appear = False, style=styles.transition, timeout=250)
    if headline_only:
        return field.children
    else:
        return fade



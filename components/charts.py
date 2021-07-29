import plotly.express as px
import components.styles as styles

def comparative_main(asset_object, title, draw_label = False):
    x = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday']
    figure = px.line(asset_object, title=title, x=x, y = ['Last Week','Historical Week'], line_shape = 'spline')
    figure.layout.yaxis.tickformat = ',.2%'
    amplitude = (asset_object.max().max() - asset_object.min().min())


    figure.update_traces(line=dict(width=4))
    figure.update_yaxes(dtick = amplitude/5)
    figure.update_xaxes(showgrid=False, zeroline=False)
    figure.update_yaxes(showgrid=True, gridwidth=2, gridcolor='grey')
    figure.update_yaxes(title = "")
    figure.update_xaxes(title = "")

    if draw_label:
        figure.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
            ), legend_title = "")
    else:
        figure.update_layout(showlegend = False)

    figure.update_layout(
    plot_bgcolor=styles.content_field_center['background'],
    paper_bgcolor=styles.content_field_center['background'],
    font_color=styles.colors['text'],    
    font_family = 'ubuntu',
    font_size = 16
    )

    return figure
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import config
import requests
from markdown import md

colors = {'background': 'lightcyan'}

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = "Sentiment Analyser"

sentiment_analysis_layout = html.Div(
    [
        html.H1("Sentiment Analyser", style={'padding-top':'20px','margin-bottom':'30px'}),
        dcc.Textarea(id="text", placeholder="Write something here...", style={'width': '50%', 'height': 200}),
        dbc.Progress(id="bar", value=50, style={'width': '50%', 'margin-left': '25%', 'margin-right': '25%'}),
        html.Div(id="result", children="Sentiment Result", style={'margin': '10px', 'height': '1em'}),
        dcc.Markdown(md, id="markdown", style={'margin-top': '80px'})
    ], style={'textAlign':'center', 'backgroundColor': colors['background']})

app.layout = sentiment_analysis_layout

@app.callback([Output('result', 'children'), Output('bar','value'), Output('bar','color')],
              [Input('text','value')],
              prevent_initial_call=True)
def update_result(text):
    if text.strip() != '':
        json_data = {'text': text, 'pred_type': 'soft'}
        response = requests.post(config.API_URL, json=json_data)
        if response.status_code == 200:
            response_json_data = response.json()
            pred_val = response_json_data['pred']
            pred_val = float(pred_val)
            if pred_val < 0.4:
                pred = 'Negative'
                bar_color = 'danger'
            elif pred_val > 0.6:
                pred = 'Positive'
                bar_color = 'success'
            else:
                pred = 'Neutral'
                bar_color = 'info'
            return [pred, pred_val*100, bar_color]
        else:
            print(f"Error response from API. Code: {response.status_code}")
            return ['', 50, 'info']
    else:
        return ['', 50, 'info']

server = app.server
if __name__ == '__main__':
    app.run_server(debug=config.DEBUG, host=config.HOST)
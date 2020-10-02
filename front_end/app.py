import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import config
import requests

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = "Sentiment Analyser"

sentiment_analysis_layout = html.Div(
    [
        html.H1("Sentiment Analyser"),
        dcc.Textarea(id="text", placeholder="Write something here...", style={'width': '50%', 'height': 200}),
        dbc.Progress(id="bar", value=50),
        html.Div(id="result", children="Result displayed here.")
    ])

app.layout = sentiment_analysis_layout

@app.callback([Output('result', 'children'), Output('bar','value')],
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
            pred = "Positive" if pred_val > 0.5  else "Negative"
            return [pred, pred_val*100]
        else:
            print(f"Error response from API. Code: {response.status_code}")
            return ['', 50]
    else:
        return ['', 50]

server = app.server
if __name__ == '__main__':
    app.run_server(debug=config.DEBUG, host=config.HOST)
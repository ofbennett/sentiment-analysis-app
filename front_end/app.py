import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import config
import requests
from markdown import md1, md2

colors = {'background': 'lightcyan'}

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = "Sentiment Analyser"

sentiment_analysis_layout = html.Div(
    [
        html.H1("Sentiment Analyzer", style={'padding-top':'20px','margin-bottom':'30px', 'text-decoration': 'underline'}),
        # html.Div(children="Oscar Bennett, October 2020", style={'textAlign':'right', 'margin-right':'20px'}),
        html.Div(id="text-area", children=[
            dcc.Textarea(id="text", placeholder="Write something here...", style={'width': '100%', 'height': 180}),
            dbc.Progress(id="bar", value=50, color='info')
        ]),
        html.Div(id="result", children="Sentiment Prediction", style={'margin': '10px', 'height': '1em'}),
        html.Div(id="markdown-area", children=[dcc.Markdown(md1, id="markdown1"),
                                               html.Img(src="assets/system_diagram.png",style = {"width": "75%", 
                                                                                                    "display": "block",
                                                                                                    "margin-left": "auto",
                                                                                                    "margin-right": "auto"}),
                                               dcc.Markdown(md2, id="markdown2"),])
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
            if pred_val < 0.2:
                pred = 'Negative'
                bar_color = 'danger'
            elif 0.2 <= pred_val < 0.4:
                pred = 'Lean Negative'
                bar_color = 'info'
            elif 0.4 <= pred_val < 0.6:
                pred = 'Neutral'
                bar_color = 'info'
            elif 0.6 <= pred_val < 0.8:
                pred = 'Lean Positive'
                bar_color = 'info'
            else:
                pred = 'Positive'
                bar_color = 'success'
            return [pred, pred_val*100, bar_color]
        else:
            print(f"Error response from API. Code: {response.status_code}")
            return ['Sentiment Prediction', 50, 'info']
    else:
        return ['Sentiment Prediction', 50, 'info']

server = app.server
if __name__ == '__main__':
    app.run_server(debug=config.DEBUG, host=config.HOST)
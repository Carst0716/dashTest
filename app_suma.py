import dash
from dash import html, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Suma de Dos Números"),
    html.Label("Número 1:"),
    dcc.Input(id='num1', type='number', value=0, style={'margin': '10px'}),
    html.Label("Número 2:"),
    dcc.Input(id='num2', type='number', value=0, style={'margin': '10px'}),
    html.Br(),
    html.Div(id='resultado', style={'marginTop': '20px', 'fontSize': '20px'})
])

@app.callback(
    Output('resultado', 'children'),
    [Input('num1', 'value'), Input('num2', 'value')]
)
def update_resultado(num1, num2):
    if num1 is None or num2 is None:
        return "Por favor, introduce ambos números."
    try:
        suma = float(num1) + float(num2)
        return f"El resultado de la suma es: {suma}"
    except ValueError:
        return "Por favor, introduce números válidos."

if __name__ == '__main__':
    app.run(debug=True)
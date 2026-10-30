from dash import Dash, html


app = Dash(__name__)

app.layout = html.Main(
    [
        html.H1("Analyse de données — La Vie en Rose"),
        html.P("Notre tableau de bord de vente et d'analyse financière."),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)

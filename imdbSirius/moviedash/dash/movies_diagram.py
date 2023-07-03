from dash import html, dcc
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from movies.models import Movie, Director, Type, OriginalName, Duration
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from django.db.models import Count

app = DjangoDash('MovieDiagram')
app.layout = html.Div(
    [html.H1("Диаграмма режисёров"),
    dcc.Graph(id='movies_diagram'),
    dbc.Button(id='update_diagram', children='Обнови диаграмму', n_clicks=0)]
)


@app.callback(
    Output('movies_diagram', 'figure'),
    Input('update_diagram', 'n_clicks')
)
def update_movie_diagram(n):
    directors_movies_count = Director.objects.all().values('name').annotate(movies_count=Count('movie'))
    data = go.Pie(
        values=[director['movies_count'] for director in directors_movies_count],
        labels=[director['name'] for director in directors_movies_count]
    )
    layout = {
        'showlegend':True
    }

    return go.Figure(data=data, layout=layout)
import pandas as pd

# Made a df with the team name color, and url
df = pd.DataFrame(
    {
        "team": ["chelsea", "juan", "diego"],
        "color": ["Blue", "#00FF00", "#0000FF"],
        "url": ["https://www.google.com", "https://www.google.com", "https://www.google.com"]
    })


def global_data():
    prem = pd.read_html("https://fbref.com/es/comps/9/Estadisticas-de-Premier-League")
    prem = pd.DataFrame(prem[0])
    prem = prem.drop(
        ['Pts/PJ', 'xG', 'xGA', 'xGD', 'xGD/90', 'Asistencia', 'Máximo Goleador del Equipo', 'Portero', 'Notas'],
        axis=1)
    return prem


def get_global_stats(team):
    # Get the color and url from the df
    color = df[df["team"] == team]["color"].values[0]
    url = df[df["team"] == team]["url"].values[0]
    return team, color, url


def get_table_data():
    return 0

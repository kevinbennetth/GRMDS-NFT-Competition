import pandas as pd
import plotly.express as px
from dash import dcc, html

def get_layout(assets):    
    assets_sale_count = assets['Last Sale Payment Token Symbol'].value_counts()
    assets_sale_count_df = pd.DataFrame({'token': assets_sale_count.index, 'count': assets_sale_count.values})
    assets_sale_count_df.loc[2:,'token'] = "Others (GALA, MANA, ASH, USDC, DAI, SAND, REVV)"
    assets_sale_count_df = assets_sale_count_df.groupby('token')['count'].sum()
    assets_sale_count_df = pd.DataFrame({'token': assets_sale_count_df.index, 'count': assets_sale_count_df.values}).sort_values('count', ascending=False)
    fig = px.pie(assets_sale_count_df, values="count", names="token", hole=.5)
    fig.update_layout(
        legend = {
            'font' : {
                'family':"Arial", 
                'size':16, 
                'color':"black"
            }, 
            "orientation":"h", 
            "yanchor":"bottom",
            "y":-0.3,
            "xanchor":"center",
            "x":0.5
        }
    )
    return html.Div(
        children=[
            html.H1("Fee Basis Points & Total Transactions vs. Total Price"),
            html.Div(
                dcc.Graph(id="pie_plt", figure=fig)
            )
        ]
    )
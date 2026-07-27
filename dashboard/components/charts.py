import plotly.express as px

DEFAULT_HEIGHT = 450
DEFUALT_TEMPLATE = "plotly_white"

def _style_chart(fig):
    """Apply a consistent style to all dashboard charts."""

    fig.update_layout(
        template=DEFUALT_TEMPLATE,
        height=DEFAULT_HEIGHT,
        margin=dict(l=20, r=20, t=60, b=20),
        title_x=0.02,
        legend_title_text="",
    )

    return fig

def plot_bar_chart(df, x, y, title):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
    )

    return _style_chart(fig)

def plot_horizontal_bar_chart(df, x, y, title):
    fig = px.bar(
        df,
        x=x,
        y=y,
        orientation="h",
        title=title,
    )

def plot_line_chart(df, x, y, title):
    fig = px.line(
        df,
        x=x,
        y=y,
        title=title,
        markers=True,
    )

def plot_pie_chart(df, names, values, title):
    fig = px.pie(
        df,
        names=names,
        values=values,
        title=title,
    )

    return _style_chart(fig)
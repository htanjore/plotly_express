def _swatches(module_names, module_contents):
    from .. import _px
    import plotly.graph_objs as go

    sequences = [
        (k, v)
        for k, v in module_contents.items()
        if not (k.startswith("_") or k == "swatches")
    ]

    return _px.FigurePx(
        data=[
            go.Bar(
                orientation="h",
                y=[name] * len(colors),
                x=[1] * len(colors),
                customdata=list(range(len(colors))),
                marker=dict(color=colors),
                hovertemplate="%{y}[%{customdata}] = %{marker.color}<extra></extra>",
            )
            for name, colors in reversed(sequences)
        ],
        layout=dict(
            title=module_names,
            barmode="stack",
            barnorm="fraction",
            template="plotly",
            bargap=0.5,
            showlegend=False,
            xaxis=dict(range=[-0.02, 1.02], showticklabels=False, showgrid=False),
            height=max(600, 40 * len(sequences)),
        ),
    )
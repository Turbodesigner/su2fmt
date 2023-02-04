from typing import Dict, List
import numpy as np
import colorsys
import random

def generate_color_legend_html(title: str, color_labels: Dict[str, List[int]]):
    title = f"<h2>{title}</h2>"
    legend = '<table>'
    for label, color in color_labels.items():
        assert len(color) == 3, "Color must be a list of 3 integers"
        legend += f'<tr><td style="background-color: {to_rgb_str(color)}" width="20"></td><td>{label}</td></tr>'
    legend += '</table>'
    return f'<div style="float: left; padding-right: 50px">{title+legend}</div>'


def generate_rgb_values(n_colors, is_grayscale=False):
    colors=[]
    for i in np.arange(0., 360., 360. / n_colors):
        hue = i/360.
        lightness = (50 + np.random.rand() * 10)/100.
        saturation = (90 + np.random.rand() * 10)/100.
        if is_grayscale:
            val = random.uniform(0.5, 1)
            rgb_values = [val,val,val]
        else:
            rgb_values = list(colorsys.hls_to_rgb(hue, lightness, saturation))

        colors.append(rgb_values)


    return colors

def to_rgb_str(color: List[int]):
    return f"rgb({int(color[0]*255)},{int(color[1]*255)},{int(color[2]*255)})"


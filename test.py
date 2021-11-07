# helloworld.py
#import the library
import streamlit as st
import altair as alt
import pandas as pd
import streamlit.components.v1 as components
import datetime
from datetime import date
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Category10
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool
import numpy as np

import streamlit as stl
# add title
st.set_page_config(page_title="CΕΙ 523 Εργασία 2021", page_icon="🧊", layout='wide', initial_sidebar_state='auto')
st.info('Ελένη Γιακουμή, Ανδρέας Όθωνος, Ανδριανή Πέτρου')

page = PAGES[selection]
page.app()

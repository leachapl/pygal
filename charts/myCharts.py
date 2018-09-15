import functools
import pygal
from datetime import date
from pygal.style import DefaultStyle
from pygal import Config


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('myCharts', __name__, url_prefix='/charts')

@bp.route('/')
def charts():
  try:
    dateline = pygal.Line()

    config = Config()
    config.box_mode = True

    dateline = pygal.Line(config)
    dateline.title = 'Remaining Stories/Bugs'
    dateline.x_labels = ['21 May 2018','28 May 2018','4 June 2018','11 June 2018','18 June 2018','25 June 2018','2 July 2018','9 July 2018','16 July 2018','23 July 2018','30 July 2018','6 August 2018','13 August 2018','20 August 2018','27 August 2018','3 September 2018','10 September 2018']

    dateline.add('Glacier',       [None, None, None, None, None, 0, 7, 1, 1, 16, 17, 15, 16, 14, 15, 16])
    dateline.add('APS',           [None, None, None, None, None, None, None, 0, 60, 128, 128, 117, 120, 121, 116, 118])
    dateline.add('AWS Migration', [9, 9, 9, 7, 9, 13, 9, 27, 81, 97, 96, 93, 85, 94, 86, 90, 79])
    dateline.add('DBP Builder App', [None, None, None, None, None, None, None, 0, 4, 14, 16, 16, 26, 41, 46, 46, 30])
    dateline.add('Workspace',      [None, None, None, None, None, None, None, None, 0, 69, 62, 62, 61, 61, 55, 60, 64])
    
    graph_data = dateline.render_data_uri()

    return render_template("dateline.html",graph_data=graph_data)
  except Exception as e:
    return (str(e))


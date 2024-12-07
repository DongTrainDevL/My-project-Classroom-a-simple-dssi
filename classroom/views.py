from django.shortcuts import render, redirect
from classroom.models import *
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, show
import pandas as pd

# Create your views here.
def Home(req):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    course = Course.objects.all()
    student_count = Student.objects.all().count()
    teacher_count = Teacher.objects.all().count()
    
    db = ['Students', 'Teachers']
    counts = [student_count, teacher_count]
    colors = Spectral4[:2]  
    source = ColumnDataSource(data=dict(db=db, counts=counts, color=colors))
    p = figure(x_range=db, y_range=(0, max(counts) + 2), height=350, title="Counts",
               toolbar_location=None, tools="")
    p.vbar(x='db', top='counts', width=0.9, color='color', legend_field="db", source=source)
    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    df = pd.DataFrame({'Count': [student_count, teacher_count]}, index=['Students', 'Teachers'])
    df.columns.name = 'Student and Teacher'
    
    context = {
        "student" : student,
        "teacher" : teacher,
        "course" : course,
        'graph_script': show(p, include_plotlyjs=False, output_type='div'),
        'dataframe': df.to_html(classes='table'),
    }
    return render(req, "pages/home.html", context)

def Graph(req):
    student = Student.objects.all().count()
    teacher = Teacher.objects.all().count()
    db = ['Students', 'Teachers']
    counts = [student, teacher]
    colors = Spectral4[:2]  
    source = ColumnDataSource(data=dict(db=db, counts=counts, color=colors))
    p = figure(x_range=db, y_range=(0, max(counts) + 2), height=350, title="Counts",
               toolbar_location=None, tools="")
    p.vbar(x='db', top='counts', width=0.9, color='color', legend_field="db", source=source)
    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    df = pd.DataFrame({'Count': [student, teacher]}, index=['Students', 'Teachers'])
    df.columns.name = 'Student and Teacher'
    context = {
        'graph_script': show(p, include_plotlyjs=False, output_type='div'),
        'dataframe': df.to_html(classes='table'),
    }
    return render(req, 'pages/dashboard/graph.html', context)


# -*- coding: cp1252 -*-
from datetime import date
import datetime
import os
sn = 0
days = datetime.datetime.today().day
months = datetime.datetime.today().month
years = datetime.datetime.today() .year
f = open('%s%slab.html'%(days,months), 'w')
f.write('<!DOCTYPE html>')
f.write('\n<html>')
f.write('\n<head>')
f.write('\n<style>')
f.write('\ntable, th, td {')
f.write('\n    border: 2px solid black;')
f.write('\n}')
f.write('\n</style>')
f.write('\n<body>')
f.write('\n<h5>Dear Priya,</h5>')
f.write('\n<h3>La Brioche Quality Check for Products Send on %s/%s/%s</h3>'%(days,months,years))
f.write('\n<p>During checking of the products of La Brioche outlets for today’s delivery the products were good with some minor issues and instructed  them for replacement and proper checking - pictures of products send are below for your verification. </p>')
f.write('\n<h5>Summary of Products</h5>')
f.write('\n<table>')
f.write('\n<tr>Raw Material<tr>')
f.write('\n<tr>')
f.write('\n<th>S.No</th>')
f.write('\n<th>Name of Product</th>')
f.write('\n<th>Picture of Product</th>')
f.write('\n<th>Quality of Product</th>')
f.write('\n</tr>')
for root, subdirs, files in os.walk('C:\Users\LEON\Desktop\labraw2108'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
             flet = os.path.join(root, file)
             sn = sn+1
             f.write('\n<tr>')
             f.write('\n<td>''</td>')
             f.write('\n<td>Fresh</td>')
             f.write('\n<td><img src="file:///%s" alt="" style="width:200px; height:auto;"></td>'%flet)
             f.write('\n<td>Good</td>')
             f.write('\n</tr>')
f.write('\n</table>')
f.write('\n<table>')
f.write('\n<tr>Sanitized Products<tr>')
f.write('\n<tr>')
f.write('\n<th>S.No</th>')
f.write('\n<th>Name of Product</th>')
f.write('\n<th>Picture of Product</th>')
f.write('\n<th>Quality of Product</th>')
f.write('\n</tr>')
sn = 0
for root, subdirs, files in os.walk('C:\Users\LEON\Desktop\labveg2108'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
             flet = os.path.join(root, file)
             sn = sn+1
             f.write('\n<tr>')
             f.write('\n<td>%s</td>'%sn)
             f.write('\n<td>Sanitized</td>')
             f.write('\n<td><img src="file:///%s" alt="" style="width:200px; height:auto;"></td>'%flet)
             f.write('\n<td>Good</td>')
             f.write('\n</tr>')
f.write('\n</table>')
f.write('\n</table>')
f.write('\n<table>')
f.write('\n<tr>Salads<tr>')
f.write('\n<tr>')
f.write('\n<th>S.No</th>')
f.write('\n<th>Name of Product</th>')
f.write('\n<th>Picture of Product</th>')
f.write('\n<th>Quality of Product</th>')
f.write('\n</tr>')
sn = 0
for root, subdirs, files in os.walk('C:\Users\LEON\Desktop\labsal2108'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
             flet = os.path.join(root, file)
             sn = sn+1
             f.write('\n<tr>')
             f.write('\n<td>%s</td>'%sn)
             f.write('\n<td>''</td>')
             f.write('\n<td><img src="file:///%s" alt="" style="width:200px; height:auto;"></td>'%flet)
             f.write('\n<td>Good</td>')
             f.write('\n</tr>')
f.write('\n</table>')
f.write('\n</table>')
f.write('\n<table>')
f.write('\n<tr>Fruits<tr>')
f.write('\n<tr>')
f.write('\n<th>S.No</th>')
f.write('\n<th>Name of Product</th>')
f.write('\n<th>Picture of Product</th>')
f.write('\n<th>Quality of Product</th>')
f.write('\n</tr>')
sn = 0
for root, subdirs, files in os.walk('C:\Users\LEON\Desktop\labfj2108'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
             flet = os.path.join(root, file)
             sn = sn+1
             f.write('\n<tr>')
             f.write('\n<td>%s</td>'%sn)
             f.write('\n<td>''</td>')
             f.write('\n<td><img src="file:///%s" alt="" style="width:200px; height:auto;"></td>'%flet)
             f.write('\n<td>Good</td>')
             f.write('\n</tr>')
f.write('\n</table>')
by = date(2015, 11, 28)
since = date(years,months,days)
res = since - by
datecode = res.days
datecode = datecode - 1
f.write('\n<footer>')
f.write('\n<p>%s</p>'%datecode)
f.write('\n</footer>')
f.write('\n</body>')
f.write('\n</head>')
f.write('\n</html>')
f.closed

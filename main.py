import os
import jinja2
from docxtpl import DocxTemplate


def gendoc(n, context(n)):
    doc = DocxTemplate('in/template.docx')
    doc.render(context[n])
    doc.save('out/invitation_%s.docx' %context[n]['Name'].replace(' ','_'))

for i in range(1,24):
    gendoc(i)

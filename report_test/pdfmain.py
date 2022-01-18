from reportlab.pdfgen  import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from body import gen_bodyTable
from footer import gen_footerTable
from header import gen_headerTable

pdf = canvas.Canvas('report.pdf', pagesize =A4 )
pdf.setTitle('LakyPos Receipt')

width, height = A4 # tuple
each_row_height =[
    height* 0.2, #20% of the height
    height * 0.77 ,
    height * 0.03

]

#hold text
table_main= Table([
    # to divide a table with one col  and 3 rows to make header, body, footer
    #each table will then have another table

    [gen_headerTable(width, each_row_height[0] )],
    [gen_bodyTable(width, each_row_height[1] )],
    [gen_footerTable(width, each_row_height[2] )],
],
    # if one value it applies to all row
    #if list it applies to each row
colWidths=width,
rowHeights= each_row_height
)

table_main.setStyle([
    #(styleproperty, stat cell(x,y), end cell , value
    #  indexing    X= 0 OR -1
    # Y=0 OR -3     0,0
    # Y=1 OR -2     1,0
    # Y=2 OR -1     2,0

    # ('GRID', (0,0) , (-1, -1), 1, 'red'),
    ('LEFTPADDING', (0,0), (-1, 2), 0),
    ('BOTTOMPADDING', (0,0), (-1, -2), 0)
])



table_main.wrapOn(pdf, 0, 0)
table_main.drawOn(pdf, 0,0)


pdf.showPage()
pdf.save()

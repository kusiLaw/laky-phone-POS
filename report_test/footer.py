
from reportlab.pdfgen  import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.lib import colors

def gen_footerTable( width, height):
   tb = Table([
       ['Root 66 , 8453 dubai - Tif. : *47824 85475 00 - Email: polinagyamuaah@gmail.com - www.palmhotel.com']
   ],
       width, height)

   tb.setStyle([
       # ('GRID', (0,0), (-1,-1), 2, 'blue'),
       ('LEFTPADDING', (0, 0), (-1, -1), 0),
       ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#003363')),
       ("TEXTCOLOR", (0, 0), (-1, -1), 'white' ),

       ("ALIGN", (0, 0), (-1, -1), 'CENTER' ), # horizontal algn
       ("VALIGN", (0, 0), (-1, -1), 'MIDDLE'), #vertical align
   ])

   return tb

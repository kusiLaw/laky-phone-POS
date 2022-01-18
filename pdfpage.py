from reportlab.pdfgen  import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image
from reportlab.lib import colors



class   Receipt:
    def __init__(self,  page_size =  A4 , name='class.pdf', title = "LakyPos Receipt"):
        self.pdf = canvas.Canvas(name, pagesize=page_size)
        self.width, self.height = page_size

        self.each_row_height = [
            self.height * 0.2,  # 20% of the height
            self.height * 0.77,
            self.height * 0.03

        ]

        self.set_title(title)

        self.main_table()






    def save(self):
        self.pdf.showPage()
        self.pdf.save()

    def set_title(self, title ):
        self.pdf.setTitle(title)


    def set_page_layout(self):
        pass

    def main_table(self):
        table_main = Table([
            # to divide a table with one col  and 3 rows to make header, body, footer
            # each table will then have another table

            [self.gen_headerTable(self.width, self.each_row_height[0])],
            [self.gen_bodyTable(self.width, self.each_row_height[1])],
            [self.gen_footerTable(self.width, self.each_row_height[2])],
        ],

            # if one value it applies to all row
            # if list it applies to each row
            colWidths=self.width,
            rowHeights= self.each_row_height
        )

        table_main.setStyle([
            # (styleproperty, stat cell(x,y), end cell , value
            #  indexing    X= 0 OR -1
            # Y=0 OR -3     0,0
            # Y=1 OR -2     1,0
            # Y=2 OR -1     2,0

            # ('GRID', (0, 0), (-1, -1), 1, 'red'),
            ('LEFTPADDING', (0, 0), (-1, 2), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -2), 0)
        ])

        table_main.wrapOn(self.pdf, 0, 0)
        table_main.drawOn(self.pdf, 0, 0)



    def gen_headerTable(self, width, height):
        width_list = [
            width * 55 / 100,
            width * 45 / 100
        ]

        tbh = Table([
            ['col 1', 'col 2'],
        ],
            width_list,
            height)

        tbh.setStyle([
            #  indexing    X= 0 OR -2   X= 1 OR -1
            # Y=0 OR -1     0,0         0,1

            ('GRID', (0, 0), (-1, -1), 1, 'red'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ])

        return tbh
    def gen_bodyTable(self, width, height):
        return 'body'

    def gen_footerTable(self, width, height):
        tb = Table([
            ['Root 66 , 8453 dubai - Tif. : *47824 85475 00 - Email: polinagyamuaah@gmail.com - www.palmhotel.com']
        ],
            width, height)

        tb.setStyle([
            # ('GRID', (0,0), (-1,-1), 2, 'blue'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#003363')),
            ("TEXTCOLOR", (0, 0), (-1, -1), 'white'),

            ("ALIGN", (0, 0), (-1, -1), 'CENTER'),  # horizontal algn
            ("VALIGN", (0, 0), (-1, -1), 'MIDDLE'),  # vertical align
        ])

        return tb



if __name__ == '__main__':
    ppf = Receipt(title = "class pdf")
    ppf.save()
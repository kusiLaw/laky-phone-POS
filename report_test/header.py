
from reportlab.pdfgen  import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image
from reportlab.lib import colors


def gen_headerTable( width, height):
    width_list=[
        width * 55 / 100,
        width * 45/ 100,
        0  #to add extra text to overlay the img
    ]

    left_img_path = './coat.png'
    left_img_width= width_list[0]
    leftimg = Image(left_img_path,
                    left_img_width, height,
                    kind = "proportional"  #grow img fit it own size
                    )

    right_img_path = './gh.jpg'
    right_img_width= width_list[1]
    rightimg = Image(right_img_path,right_img_width,height,

                     )


    tbh = Table([
       [leftimg, rightimg, "Ghana"],
    ],
    width_list,
    height)

    tbh.setStyle([
        #  indexing    X= 0 OR -2   X= 1 OR -1
        # Y=0 OR -1     0,0         0,1

        # ('GRID', (0,0) , (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('ALIGN', (0,0),(0,0), 'CENTER'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),

        #for text overlay
        ('LEFTPADDING', (2, 0), (-1, -0), -width_list[1] + 120),
        ('FONTESIZE', (2, 0), (-1, -0), 20),
        ('BOTTOMPADDING', (2, 0), (-1, -0), 40)
    ])

    return tbh
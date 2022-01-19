from reportlab.pdfgen  import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.lib import colors

def gen_bodyTable( width, height):
    width_list =[
        width * 10/100,
        width * 80 / 100,
        width * 10 / 100,

    ]

    height_list=[
        height * 10/100,
        height * 15 / 100, #Contact
        height * 35 / 100,# PriceList
        height * 30 / 100, #  Description
        height * 10 / 100, # AboutT
    ]

    btb = Table([
        ["", "Offer", ""],
        ["", _genContactTable(width_list[1], height_list[1]), ""],
        ["", _genPriceListTable(width_list[1],height_list[2]), ""],
        ["",  _genDescriptionPara(), ""],
        ["", _genAboutTable(width_list[1], height_list[4]), ""],

    ],
    width_list,
    height_list
    )

    btb.setStyle([
        # ('GRID', (0,0), (-1,-1), 2, 'blue'),
        ('LINEBELOW', (1, 0), (1, 1), 5, colors.HexColor("003363")),

        ('LINEBELOW', (1, 3), (1, 3), 5, colors.HexColor("003363")),
        ('LEFTPADDING', (1, 0), (1, 3), 20),

        ("FONTSIZE", (1, 0), (1, 0), 30),
        ("BOTTOMPADDING", (1, 0), (1, 0), 30),
        ("BOTTOMPADDING", (1, 1), (1, 2), 0),

        ("BOTTOMPADDING", (1, 3), (1, 3), 40),

        ("BOTTOMPADDING", (1, 4), (1, 4), 0),
        ("LEFTPADDING", (1, 4), (1, 4), 0),


    ])
    return btb


def _genContactTable(width ,height):
    return 'contact'

def _genPriceListTable(width ,height):
    return  'price'

def _genDescriptionPara():
    return 'dis'

def _genAboutTable(width ,height):
    return 'about'


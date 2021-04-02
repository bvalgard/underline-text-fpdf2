from fpdf import FPDF

# pip install pillow
from PIL import ImageFont

def get_text_width(text_string, font):
    # the 2.6 works with times
    # 3 works pretty well with arial
    # why these numbers work... I don't know
    return font.getmask(text_string).getbbox()[2] / 2.6



# Create pdf object
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# set imagefont
font = ImageFont.truetype('times.ttf', 12)

# First Section - not underlined
pdf.set_font('times', '', 12)
text_string_1 = 'Hello world'
# get width of font and add it as width of cell
pdf.cell(get_text_width(text_string_1, font),
         10, text_string_1, ln=False)

# # Second Section - underlined
pdf.set_font('times', 'u', 12)
text_string_2 = 'this is me'
pdf.cell(get_text_width(text_string_2, font),
         10, text_string_2)

# Third Section - not underlined
pdf.set_font('times', '', 12)
text_string_3 = 'don\'t be a fool'
pdf.cell(10,10, text_string_3)

pdf.output('underlined.pdf')

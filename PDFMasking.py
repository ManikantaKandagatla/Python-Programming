__author__ = 'ManiKanta Kandagatla'

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate,Spacer
import re


mask_patterns=['[\s]*[^@]+@[^@]+\.[^@]+[\s$]*','[\s]*[7-9]+\d{9}[\s$]*']
mask_vals = ['dummymail@dummy.com','543432156']


def generate_mask_file(content):
    #text = file("C:/Users/ManiKanta Kandagatla/Desktop/Testdata.txt","r").read()
    #text = text.replace(word,mask_string)
    op_pdf = SimpleDocTemplate("C:/Users/ManiKanta Kandagatla/Desktop/Testdata_op.pdf", pagesize = letter)
    story = []
    style = getSampleStyleSheet()
    paragraphs = content.split('\n')
    for para in paragraphs:
        story.append(Paragraph(para, style['Normal']))
        story.append(Spacer(0, inch * .1))
    op_pdf.build(story)

def get_content_from_pdf(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()

    #text = text.replace(" the ", " maskstring ")
    #f = open("C:/Users/ManiKanta Kandagatla/Desktop/Testdata.txt","w")
    #f.write(text)
    count =0
    print text
    for str in mask_patterns:
        text = re.sub(str,mask_vals[count],text)
        count = count + 1
    print text
    generate_mask_file(text)
    output.close()

get_content_from_pdf('C:/Users/ManiKanta Kandagatla/Desktop/temp.pdf')

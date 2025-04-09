from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def generate_presentation(ppt_heading):
    prs = Presentation()
    blank_slide_layout = prs.slide_layouts[6]

    slide = prs.slides.add_slide(blank_slide_layout)

    # --- Add Images ---
    slide.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/gov_logo.png", Inches(-0.25), Inches(-0.7), height=Inches(3))
    slide.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/startupIndia.png", Inches(7.5), Inches(0.5), width=Inches(2))
    slide.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/seedFundScheme.png", Inches(3.0), Inches(1), height=Inches(4))

    # --- Add Heading Text Below Center Image ---
    left = Inches(0.3)
    top = Inches(4.7)
    width = Inches(10)
    height = Inches(1)

    textbox = slide.shapes.add_textbox(left, top, width, height)
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    p = text_frame.add_paragraph()
    p.text = "STARTUP INDIA SEED FUND SCHEME"
    p.font.bold = True
    p.font.size = Pt(32)
    p.font.color.rgb = RGBColor(47, 50, 144)
    p.alignment = PP_ALIGN.CENTER

    textbox = slide.shapes.add_textbox(left, Inches(5.5), width, height)
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    p = text_frame.add_paragraph()
    p.text = ppt_heading
    p.font.bold = True
    p.font.size = Pt(30)
    p.font.color.rgb = RGBColor(47, 50, 144)
    p.alignment = PP_ALIGN.CENTER

    # Save the presentation
    prs.save("/Users/aditya.narayan/Desktop/form-to-ppt/output/auto-generated-ppt.pptx")


# generate_presentation("ABRA KA DABRA")
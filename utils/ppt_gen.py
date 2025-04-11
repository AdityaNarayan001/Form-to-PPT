from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.dml.color import RGBColor
# from llm import llm

def generate_presentation(ppt_heading, explain_problem_you_are_solving):
    prs = Presentation()
    # --- Slide 1 ---
    blank_slide_layout = prs.slide_layouts[6]

    slide1 = prs.slides.add_slide(blank_slide_layout)

    # --- Add Images ---
    slide1.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/gov_logo.png", Inches(-0.25), Inches(-0.7), height=Inches(3))
    slide1.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/startupIndia.png", Inches(7.5), Inches(0.5), width=Inches(2))
    slide1.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/seedFundScheme.png", Inches(3.0), Inches(1), height=Inches(4))

    # --- Add Heading Text Below Center Image ---
    left = Inches(0.3)
    top = Inches(4.7)
    width = Inches(10)
    height = Inches(1)

    textbox = slide1.shapes.add_textbox(left, top, width, height)
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    p = text_frame.add_paragraph()
    p.text = "STARTUP INDIA SEED FUND SCHEME"
    p.font.bold = True
    p.font.size = Pt(32)
    p.font.color.rgb = RGBColor(47, 50, 144)
    p.alignment = PP_ALIGN.CENTER

    textbox = slide1.shapes.add_textbox(left, Inches(5.5), width, height)
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    p = text_frame.add_paragraph()
    p.text = ppt_heading
    p.font.bold = True
    p.font.size = Pt(30)
    p.font.color.rgb = RGBColor(47, 50, 144)
    p.alignment = PP_ALIGN.CENTER

    # --- Slide 2 ---
    blank_slide_layout = prs.slide_layouts[6]
    slide2 = prs.slides.add_slide(blank_slide_layout)

    # --- Add Images ---
    slide2.shapes.add_picture("/Users/aditya.narayan/Desktop/form-to-ppt/asset/slide1/seedFundScheme.png", Inches(8.5), Inches(0.1), width=Inches(1.2))
    # Add a yellow line
    h_line = slide2.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(0.1), Inches(0.2), Inches(7), Inches(0.2))
    h_line.line.color.rgb = RGBColor(250, 191, 62)
    h_line.line.width = Pt(1)

    v_line = slide2.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(0.2), Inches(0.1), Inches(0.1), Inches(7))
    v_line.line.color.rgb = RGBColor(250, 191, 62)
    v_line.line.width = Pt(1)

    # --- Add Heading Text Below Center Image ---
    left = Inches(-0.5)
    top = Inches(0.1)
    width = Inches(9.5)
    height = Inches(1)

    textbox = slide2.shapes.add_textbox(left, top, width, height)
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    p = text_frame.add_paragraph()
    p.text = "EXPLAIN THE PROBLEM YOU ARE SOLVING"
    p.font.bold = True
    p.font.size = Pt(32)
    p.font.color.rgb = RGBColor(47, 50, 144)
    p.alignment = PP_ALIGN.CENTER

    textbox = slide2.shapes.add_textbox(Inches(0.3), Inches(1.1), width, height)
    text_frame = textbox.text_frame
    text_frame.word_wrap = True

    p = text_frame.add_paragraph()
    p.text = explain_problem_you_are_solving
    p.font.bold = False
    p.font.size = Pt(30)
    p.font.color.rgb = RGBColor(47, 50, 144)
    p.alignment = PP_ALIGN.LEFT




    # Save the presentation
    prs.save("/Users/aditya.narayan/Desktop/form-to-ppt/output/auto-generated-ppt.pptx")
    print(f"🟢 Presentation saved as : auto-generated-ppt.pptx")


# generate_presentation(
#     "ABRA KA DABRA", 
#     llm("This project generates a professional PowerPoint presentation based on user input collected from a simple web form. It's powered by AI to refine your content, correct grammar, improve English, and add relevant images that visually align with the text on each slide."),
#     )
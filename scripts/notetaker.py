from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

def create_pdf(text_string, output_file="output.pdf"):
    try:
        # Create a PDF document
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        
        # Get a style sheet
        styles = getSampleStyleSheet()
        
        # Define custom styles
        heading1_style = ParagraphStyle(name='Heading1', parent=styles['Heading1'], fontSize=24, spaceAfter=12)
        heading2_style = ParagraphStyle(name='Heading2', parent=styles['Heading2'], fontSize=18, spaceAfter=10)
        heading3_style = ParagraphStyle(name='Heading3', parent=styles['Heading3'], fontSize=14, spaceAfter=8)
        heading4_style = ParagraphStyle(name='Heading4', parent=styles['Heading4'], fontSize=12, spaceAfter=6)
        code_style = ParagraphStyle(name='Code', parent=styles['Code'], fontSize=10, leading=12, spaceAfter=6)
        table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('FONTSIZE', (0, 0), (-1, 0), 12),
                                  ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                                  ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                  ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                                  ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                                  ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                                  ('FONTSIZE', (0, 1), (-1, -1), 10),
                                  ('TOPPADDING', (0, 1), (-1, -1), 4),
                                  ('BOTTOMPADDING', (0, 1), (-1, -1), 4)])
        
        # Split the text into lines
        lines = text_string.split("\n")
        
        # Create a list of elements
        elements = []
        
        for line in lines:
            if line.startswith("####"):
                elements.append(Paragraph(line[4:].strip(), heading4_style))
            elif line.startswith("###"):
                elements.append(Paragraph(line[3:].strip(), heading3_style))
            elif line.startswith("##"):
                elements.append(Paragraph(line[2:].strip(), heading2_style))
            elif line.startswith("#"):
                elements.append(Paragraph(line[1:].strip(), heading1_style))
            elif line.startswith("```"):
                code_block = []
                for codeline in lines[lines.index(line) + 1:]:
                    if codeline.startswith("```"):
                        break
                    code_block.append(codeline)
                elements.append(Paragraph("\n".join(code_block), code_style))
            elif line.startswith("|"):
                table_data = []
                for tableline in lines[lines.index(line):]:
                    if not tableline.startswith("|"):
                        break
                    cells = [cell.strip() for cell in tableline.split("|")][1:-1]
                    table_data.append(cells)
                table = Table(table_data)
                table.setStyle(table_style)
                elements.append(table)
            else:
                elements.append(Paragraph(line, styles["Normal"]))
            elements.append(Spacer(1, 6))
        
        # Build the PDF document
        doc.build(elements)
        
        print(f"PDF generated successfully: {output_file}")
    except Exception as e:
        print(f"Error creating PDF: {e}")
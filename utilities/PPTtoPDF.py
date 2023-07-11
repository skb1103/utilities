from glob import glob
import sys
import win32com.client

'''
This program works on a windows machine.
'''

# provide the path of pptx files
paths = glob('.\*\*.pptx')


def pptx_to_pdf(input_pptx_path, output_pdf_path):
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    presentation = powerpoint.Presentations.Open(input_pptx_path)
    presentation.SaveAs(output_pdf_path, 32)  # 32 is the value for saving as PDF
    presentation.Close()
    powerpoint.Quit()
    
    return None

for path_ in paths:
    path_ = path_
    input_file_path = os.path.abspath(path_)
    output_file_path = os.path.abspath(path_.split('.pptx')[0]+'.pdf')

    pptx_to_pdf(input_file_path, output_file_path)
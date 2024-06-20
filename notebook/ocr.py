import os
import pandas as pd
import requests
import pdfplumber

invoice_pdf =r"E:\work\Job-Recomendation\notebook\shubhi_shrotriya_resume_Deloitte.pdf"


with pdfplumber.open(invoice_pdf) as pdf:
     text=""
     pages = pdf.pages
     for page in pages:
         text += page.extract_text(x_tolerance=2)
         print(text)
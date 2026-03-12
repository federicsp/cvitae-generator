import yaml
import tempfile
import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from playwright.sync_api import sync_playwright

env = Environment(loader=FileSystemLoader("templates"))

with open("data/cv.yaml", "r") as f:
    data = yaml.safe_load(f)

template_data = dict(
    person=data['person'],
    skills=data['skills'],
    work=data['work'],
    tags=data['tags'],
    education=data['education'],
    cities=data['cities'],
    books=data['books']
)

# --- HTML output ---
html_template = env.get_template("cv_template.html")
html_content = html_template.render(**template_data)

Path("output").mkdir(exist_ok=True)
html_file = "output/cv.html"
with open(html_file, "w") as f:
    f.write(html_content)

# --- PDF output (template dedicato) ---
pdf_template = env.get_template("cv_template_pdf.html")
pdf_html_content = pdf_template.render(**template_data)

pdf_file = "output/cv.pdf"
with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as tmp:
    tmp.write(pdf_html_content)
    tmp_path = tmp.name

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(Path(tmp_path).resolve().as_uri())
        page.pdf(path=pdf_file, format="A4", print_background=True)
        browser.close()
finally:
    os.unlink(tmp_path)

print("CV HTML e PDF generati in output/")

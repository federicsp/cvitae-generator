import yaml                                   
from jinja2 import Environment, FileSystemLoader  
from pathlib import Path                      
from playwright.sync_api import sync_playwright  

env = Environment(loader=FileSystemLoader("templates"))  

with open("data/cv.yaml", "r") as f:           
    data = yaml.safe_load(f)                  

template = env.get_template("cv_template.html")  
html_content = template.render(               
    person=data['person'],
    skills=data['skills'],                    
    work=data['work'],                        
    tags=data['tags'],                        
    education=data['education'],              
    cities=data['cities'],                    
    books=data['books']                       
)

Path("output").mkdir(exist_ok=True)            
html_file = "output/cv.html"                   
pdf_file = "output/cv.pdf"                     

with open(html_file, "w") as f:                
    f.write(html_content)                      

with sync_playwright() as p:                   
    browser = p.chromium.launch()              
    page = browser.new_page()                  
    page.goto(Path(html_file).resolve().as_uri())  
    page.pdf(path=pdf_file, format="A4", print_background=True)  
    browser.close()                            

print("CV HTML e PDF generati in output")       

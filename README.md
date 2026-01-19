# CVitae Generator

CVitae Generator is a simple python tool to create HTML resumes from a YAML file

## Project Structure

    .
    ├── assets
    │   ├── css
    │   │   └── cv.css          # Styles
    │   └── images
    │       └── picture.jpg     # Image for the CV
    ├── cv_generator.py         # Main script to generate the CV
    ├── data
    │   └── cv.yaml             # Resume data (name, experiences, etc.)
    ├── output                  # Output folder for generated CVs HTML and PDF
    └── templates
        └── cv_template.html    # HTML template for the CV

## Requirements

- Python 3.12+
- Jinja2
- PyYAML
- Playwright


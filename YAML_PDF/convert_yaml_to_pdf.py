import yaml
from jinja2 import Template
import pdfkit

# Configure pdfkit to use the installed wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

# Load YAML data
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Define HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { font-size: 24px; }
        h2 { font-size: 20px; margin-top: 20px; }
        p { font-size: 16px; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <p><strong>Author:</strong> {{ author }}</p>
    <p><strong>Date:</strong> {{ date }}</p>
    {% for section in sections %}
        <h2>{{ section.title }}</h2>
        <p>{{ section.content }}</p>
    {% endfor %}
</body>
</html>
"""

# Render HTML from template and data
template = Template(html_template)
html_content = template.render(
    title=data['title'],
    author=data['author'],
    date=data['date'],
    sections=data['sections']
)

# Save HTML to file
with open('document.html', 'w') as file:
    file.write(html_content)

# Convert HTML to PDF
pdfkit.from_file('document.html', 'document.pdf', configuration=config)

print("PDF generated successfully.")


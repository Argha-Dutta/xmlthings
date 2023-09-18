'''from lxml import etree
import os

# Get the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load XML
xml_tree = etree.parse(os.path.join(script_dir, "employees.xml"))

# Load XSL
xsl_transform = etree.XSLT(etree.parse(os.path.join(script_dir, "transform.xsl")))

# Apply XSLT transformation
html_tree = xsl_transform(xml_tree)

# Validate against XSD
xmlschema = etree.XMLSchema(etree.parse(os.path.join(script_dir, "employee_schema.xsd")))
if xmlschema.validate(xml_tree):
    print("XML is valid against XSD.")
else:
    print("XML is not valid against XSD.")
    exit(1)

# Write transformed HTML to a file
with open(os.path.join(script_dir, "output.html"), "wb") as output_file:
    output_file.write(etree.tostring(html_tree, pretty_print=True))'''
    
from lxml import etree

# Load the XML and XSLT files
xml_file = "C:/Users/Hp/Documents/Imca-a/webstackdev_xml/employees.xml"
xslt_file = "C:/Users/Hp/Documents/Imca-a/webstackdev_xml/transform.xsl"

# Create an XSLT transformer
transformer = etree.XSLT(etree.parse(xslt_file))

# Apply the transformation
result_tree = transformer(etree.parse(xml_file))

# Save the result as an HTML file
output_html_file = "C:/Users/Hp/Desktop/Untitled.html"
result_tree.write(output_html_file, pretty_print=True)

print(f"Transformation complete. HTML saved as {output_html_file}")

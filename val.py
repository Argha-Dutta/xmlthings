'''from lxml import etree
import os

def validate_xml(xml_filename, xsd_filename):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        xml_path = os.path.join(script_dir, xml_filename)
        xsd_path = os.path.join(script_dir, xsd_filename)        
        xml_doc = etree.parse(xml_path)
        schema = etree.XMLSchema(file=xsd_path)  
        validator = schema.assertValid(xml_doc)
        print("XML document is valid.")
    except etree.DocumentInvalid as e:
        print("XML document is not valid.")
        print("Validation errors:")
        for error in e.error_log:
            print(f"Line {error.line}, Column {error.column}: {error.message}")

if __name__ == "__main__":
    xml_file = "employees.xml"
    xsd_file = "employee_schema.xsd"

    validate_xml(xml_file, xsd_file)'''
import xmlschema

xml_file_path = "C:/Users/Hp/Documents/Imca-a/webstackdev_xml/employees.xml"
xsd_file_path = "C:/Users/Hp/Documents/Imca-a/webstackdev_xml/employee_schema.xsd"

schema = xmlschema.XMLSchema(xsd_file_path)
if schema.is_valid(xml_file_path):
    print(f"{xml_file_path} is valid against {xsd_file_path}.")
else:
    print(f"{xml_file_path} is not valid against {xsd_file_path}.")
   
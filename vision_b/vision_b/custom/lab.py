import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_link_to_form, getdate
import os
from xml.etree import ElementTree

@frappe.whitelist()
def xml_file_upload(doc):
    upload_file=os.path.abspath(f'{frappe.utils.get_site_base_path()[2::]}'+doc)
    dom=ElementTree.parse(upload_file)
    results=[dom._root.attrib]
    list_value=[]
    for i in results:
        dict_value={}
        for j in i:
            dict_value[frappe.scrub(j)]=i[j]
    list_value.append(dict_value)
    return list_value
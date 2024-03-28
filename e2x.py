from Evtx.Evtx import Evtx
from Evtx.Views import evtx_file_xml_view
from datetime import datetime

"""
-------------------------------------------------
Script Name: e2x.py
Description: This script converts EVTX files to XML
Author: 4d4MP
Date: 2024-03-28
-------------------------------------------------
"""


def evtx_to_xml(file_path):
    """
    Function to convert EVTX files to XML
    """
    print("Converting", file_path, "to XML")
    start = datetime.now()
    print("Script started at ", start)
    with Evtx(file_path) as log:
        with open(file_path + ".xml", 'w') as f:
            f.write("<Events>\n")
            for xml, _ in evtx_file_xml_view(log.get_file_header()):
                try:
                    f.write(xml)
                    f.write("\n")
                except Exception as e:
                    print(e)
            f.write("</Events>\n")
    end = datetime.now()
    print("Script ended at ", end)
    print("Time taken: ", end - start)

evtx_to_xml("dc-1_0101.evtx")
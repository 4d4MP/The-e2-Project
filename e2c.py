from Evtx.Evtx import Evtx
from Evtx.Views import evtx_file_xml_view as view
from datetime import datetime
import csv
import xml.etree.ElementTree as ET


"""
-------------------------------------------------
Script Name: e2c.py
Description: This script converts EVTX files to CSV
Author: 4d4MP
Date: 2024-03-28
-------------------------------------------------
"""


def evtx_to_csv(file_path):
    """
    Function to convert EVTX files to CSV
    """
    start = datetime.now()
    print("Converting", file_path, "to CSV" + " at ", start)
    

    with Evtx(file_path) as log:
        with open(file_path + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for xml, _ in view(log.get_file_header()):
                try:
                    root = ET.fromstring(xml)
                    data = [elem.text for elem in root.iter()]
                    writer.writerow(data)
                except Exception as e:
                    print(e)
    end = datetime.now()
    print("Script ended at ", end, "with time taken: ", end - start)

evtx_to_csv("dc-1_0101.evtx")
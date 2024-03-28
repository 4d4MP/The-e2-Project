from Evtx.Evtx import Evtx
from Evtx.Views import evtx_file_xml_view as view
from datetime import datetime
import os
from threading import Thread
from threading import Semaphore

print("-------------------------------------------------")
print("Script Name: e2x_MT.py")
print("Description: This script converts EVTX files to XML.")
print("This script is a multi-threaded version of e2x.py with added capability to work on multiple files at the same time.")
print("Author: 4d4MP")
print("Date: 2024-03-28")
print("-------------------------------------------------")

FOLDER_PATH = "E:\\DATA\\log_onof\\"
THREAD_LIMITER = 5

def evtx_to_xml(file_path):
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

def get_files(path):
    """
    Function to get list of evtx files from the folder
    """
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.evtx')]
    print("Files to convert: ", files)
    return files
    
def main():
    """
    Main function to run the script
    """
    
    files = get_files(FOLDER_PATH)
    threads = []

    semaphore = Semaphore(THREAD_LIMITER)

    def thread_limited_evtx_to_xml(file):
        with semaphore:
            evtx_to_xml(file)

    for file in files:
        thread = Thread(target=thread_limited_evtx_to_xml, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
        
main()
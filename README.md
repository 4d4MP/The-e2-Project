## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Introduction

This project contains four Python scripts designed for the conversion of EVTX files to XML or CSV formats. These scripts are intended to simplify and automate the process of file conversion, making it more efficient and less prone to errors. Also added MT (multi-thread) options for faster result in a multi-file situation.

## Intended Use

These scripts are specifically designed for the conversion of EVTX files to XML or CSV. This can be particularly useful in situations where data from EVTX files needs to be analyzed or manipulated in a different format.

## Requirements

To use these scripts, you will need:

1. Python3 installed on your machine.
2. The necessary Python libraries installed. You can install them using pip:
    ```
    pip install -r requirements.txt
    ```
3. EVTX files that you want to convert.

## How to Use

1. Place your EVTX files in the same directory as the scripts.
2. Modify the path (or folder_path on the MT edition) to the desired EVTX file
2. Run the desired script:
    ```
    python <script_name.py>
    ```
3. The script will create a new XML or CSV file in the same directory.

Please note that these scripts are intended for use as is and customization may be required to suit your specific needs.
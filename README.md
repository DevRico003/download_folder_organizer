# Download Folder Organizer

## Overview

This Python script helps you to automatically sort files in your download folder based on their file extension. When a new file is detected in your download folder, it will be moved into a designated sub-folder according to its file type.

For example, all `.pdf` files will be moved into a `PDFs` folder, `.jpg` files into a `JPGs` folder, `.mp3` files into a `Music` folder, and so on.

## Requirements

- Python 3.x
- No additional packages are required

## Installation

1. Clone this repository or download the script.
2. Place the script wherever you like.

## Configuration

Open the script using a text editor and modify the `destination_folders` dictionary to fit your needs. By default, the script organizes the files into the following categories:

- PDFs
- JPGs
- PNGs
- Music (MP3)
- Videos (MP4, MOV)
- Word (DOCX)
- Powerpoint (PPTX, PPT)
- Programs (EXE)
- Zips
- Excel (XLSX, XLS)
- Python Scripts (PY)
- Bash Scripts (SH)
- SSH Keys (PEM, PPK)
- CSV Files
- TOML Files
- JSON Files
- Text Files (TXT)

## Usage

To run the script, simply execute it using Python:

```bash
python <path-to-the-script>
```

The script will now monitor your download folder and automatically move new files into their corresponding sub-folders.

## Warning

Please use this script responsibly. The files are moved without any prompt or confirmation. Make sure to backup important files before running the script to avoid accidental loss of data.

## Contributing

If you want to add more features or improve existing ones, feel free to create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
# Find Duplicates

Find Duplicates is a command-line tool for searching and identifying duplicate files within a directory. It compares files based on their name and size and provides options to display the duplicate files or generate output in various formats.

## Installation

1. Clone the repository:
```bash
git clone git@github.com:ValentinLibouton/find_duplicates.git
```
2. Navigate to the project directory:
```bash
cd find_duplicates
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script `find_duplicates.py` with the following command-line arguments:
```bash
python find_duplicates.py directory [output_type] [--duplicates]
```
- `directory` (required): The directory to search for duplicate files.
- `output_type` (optional): The type of output. Supported options are "terminal", "html", and "csv". The default is "terminal".
- `--duplicates` (optional): Display only duplicate files. If specified, the script will only show duplicate files; otherwise, it will display all files in the directory.

Examples:

- Search for duplicate files in a directory and display the results in the terminal:
```bash
python find_duplicates.py /path/to/directory
```
- Search for duplicate files in a directory and generate an HTML report:
```bash
python find_duplicates.py /path/to/directory html
```
- Search for duplicate files in a directory and generate a CSV file:
```bash
python find_duplicates.py /path/to/directory csv
```
- Search for duplicate files only and display the results in the terminal:
```bash
python find_duplicates.py /path/to/directory terminal --duplicates
```

## License

- This project is licensed under **...**
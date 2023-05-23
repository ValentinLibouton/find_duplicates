import os
import sys
import argparse
import datetime
import csv
from collections import Counter
from itertools import groupby
from tqdm import tqdm

def get_file_info(file_path):
    file_name = os.path.basename(file_path)
    try:
        modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    except FileNotFoundError:
        modified_time = None
    file_size = os.path.getsize(file_path)
    absolute_path = os.path.abspath(file_path)
    return [file_name, modified_time, file_size, absolute_path]

def search_files(directory):
    file_list = []
    file_count = sum(len(files) for _, _, files in os.walk(directory))
    with tqdm(total=file_count) as pbar:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_info = get_file_info(file_path)
                    file_list.append(file_info)
                except FileNotFoundError:
                    pass # Skip the file and continue
                pbar.update(1)
    return file_list

def sort_files(file_list):
    sorted_files = sorted(file_list, key=lambda x: (x[0], x[1], x[2]) if len(x) >= 3 else [])
    return sorted_files

def output_to_terminal(file_list):
    for file_info in file_list:
        print(file_info)

def output_to_csv(file_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'Modified Time', 'File Size', 'Absolute Path'])
        for file_info in file_list:
            writer.writerow(file_info)

def output_to_html(file_list, output_file):
    with open(output_file, 'w') as html_file:
        html_file.write('<html>\n')
        html_file.write('<head>\n')
        html_file.write('<title>File List</title>\n')
        html_file.write('</head>\n')
        html_file.write('<body>\n')
        html_file.write('<table>\n')
        html_file.write('<tr><th>File Name</th><th>Modified Time</th><th>File Size</th><th>Absolute Path</th></tr>\n')
        for file_info in file_list:
            html_file.write('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(file_info[0], file_info[1], file_info[2], file_info[3]))
        html_file.write('</table>\n')
        html_file.write('</body>\n')
        html_file.write('</html>\n')

def get_duplicate_files(file_list):
    """
    Get a list of duplicate files based on file name and size.

    Args:
        file_list (list): List of files.

    Returns:
        list: List of duplicate files, where each file is represented as a list
        containing the file name, modified time, file size, and absolute path.
    """
    file_list.sort(key=lambda x: (x[0], x[2]))  # Sort the files by name and size
    duplicate_files = []
    for key, group in groupby(file_list, key=lambda x: (x[0], x[2])):
        files = list(group)
        if len(files) > 1:
            duplicate_files.extend(files)
    return duplicate_files

def main():
    parser = argparse.ArgumentParser(description='Recursive file search script')
    parser.add_argument('directory', help='The directory to search in')
    parser.add_argument('output_type', nargs='?', default='terminal', choices=['terminal', 'html', 'csv'], 
                        help='The type of output (terminal, html, csv)')
    parser.add_argument('--duplicates', action='store_true', help='Display only duplicate files')
    args = parser.parse_args()

    if not args.directory:
        parser.error('The directory argument is required.')

    file_list = search_files(args.directory)

    if args.duplicates:
        file_list = get_duplicate_files(file_list)

    sorted_files = sort_files(file_list)

    if args.output_type == 'terminal':
        output_to_terminal(sorted_files)
    elif args.output_type == 'html':
        output_to_html(sorted_files, 'output.html')
    elif args.output_type == 'csv':
        output_to_csv(sorted_files, 'output.csv')

if __name__ == '__main__':
    main()

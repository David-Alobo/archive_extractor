import Zipfile

def extract_archive(file_path, dest_dir):
    with Zipfile.Zipfile(file_path, 'r') as archive:
        archive.extractall(dest_dir)

if '__name__' == '__main__':
    extract_archive('C:\Users\2941522A\codebase\my_files\my_practice\Archive_Extractor\compressed.zip', 'C:\Users\2941522A\codebase\my_files\my_practice\Archive_Extractor')

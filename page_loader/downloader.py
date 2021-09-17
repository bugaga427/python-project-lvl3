from page_loader.cli import generate_parser
import requests
import os.path


def page_loader():
    parser = generate_parser()
    file_path = download(
        parser.url,
        parser.output
    )
    print(file_path)


def download(url: str, path_to_dir: str):
    file_name = build_file_name(url)
    content = requests.get(url).text
    file_path = os.path.join(path_to_dir, file_name)
    writing_to_file(file_path, content)
    return file_path


def build_file_name(url: str):
    if url.startswith('https://'):
        url = url[8:]
    elif url.startswith('http://'):
        url = url[7:]
    if url.endswith('/'):
        url = url[:-1]
    name = ''
    for char in url:
        if char.isalnum():
            name += char
        else:
            name += '-'
    name += '.html'
    return name


def writing_to_file(file_path: str, content):
    with open(file_path, 'w') as f:
        f.write(content)

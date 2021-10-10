from page_loader.cli import generate_parser
from bs4 import BeautifulSoup
import requests
import os


def page_loader():
    parser = generate_parser()
    url = parser.url[:-1] if parser.url.endswith('/') else parser.url
    file_path = download(
        url,
        parser.output
    )
    dir_path = os.path.split(file_path)[0]
    html_content = open(file_path).read()
    soup = BeautifulSoup(html_content, 'html5lib')
    for img_tag in soup.find_all('img'):
        if img_tag['src'].startswith('/'):
            image_url = url + img_tag['src']
            download_image(image_url, dir_path)
    print(file_path)


def download(url: str, path_to_dir: str):
    dir_name = build_name(url, '_files')
    os.mkdir(os.path.join(path_to_dir, dir_name))
    file_name = build_name(url, '.html')
    content = requests.get(url).text
    file_path = os.path.join(path_to_dir, dir_name, file_name)
    writing_to_file(file_path, content, 'w')
    return file_path


def download_image(url: str, path_to_dir: str):
    file_name = build_name(url[:-4], '.png')
    content = requests.get(url).content
    image_path = os.path.join(path_to_dir, file_name)
    writing_to_file(image_path, content, 'wb')
    return image_path


def build_name(url: str, tail: str):
    if url.startswith('https://'):
        url = url[8:]
    elif url.startswith('http://'):
        url = url[7:]
    name = ''
    for char in url:
        if char.isalnum():
            name += char
        else:
            name += '-'
    name += tail
    return name


def writing_to_file(file_path: str, content, mode='w'):
    with open(file_path, mode) as f:
        f.write(content)

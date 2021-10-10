from page_loader.downloader import download, download_image
from tempfile import TemporaryDirectory
import os.path
import requests_mock

path_to_expect_html = os.path.join(
    'tests',
    'fixtures',
    'page-loader-hexlet-repl-co-courses_files',
    'page-loader-hexlet-repl-co-courses.html'
)
path_to_expect_image = os.path.join(
    'tests',
    'fixtures',
    'page-loader-hexlet-repl-co-courses_files',
    'page-loader-hexlet-repl-co-assets-professions-nodejs.png'
)

html_url = 'https://page-loader.hexlet.repl.co/'
image_url = 'https://page-loader.hexlet.repl.co/assets/professions/nodejs.png'


def test_download_page():
    with TemporaryDirectory() as tmp:
        tmp_dir_name = tmp
        with requests_mock.Mocker() as m:
            m.get(
                html_url,
                text=open(path_to_expect_html).read()
            )
            html_path = download(
                html_url,
                tmp_dir_name
            )
        with open(path_to_expect_html) as expect:
            expect_content = expect.read()
            with open(html_path) as html:
                html_content = html.read()
                assert expect_content == html_content

        with requests_mock.Mocker() as m:
            m.get(
                image_url,
                content=open(path_to_expect_image, 'rb').read()
            )
        image_path = download_image(
            image_url,
            os.path.split(html_path)[0]
        )
        with open(path_to_expect_image, 'rb') as expect:
            expect_content = expect.read()
            with open(image_path, 'rb') as image:
                image_content = image.read()
                assert expect_content == image_content

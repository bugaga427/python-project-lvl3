from page_loader.downloader import download
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


def test_download_page():
    with TemporaryDirectory() as tmp:
        tmp_dir_name = tmp
        with requests_mock.Mocker() as m:
            m.get(
                'https://page-loader.hexlet.repl.co/',
                text=open(path_to_expect_html).read()
            )
            html_path = download(
                'https://page-loader.hexlet.repl.co/',
                tmp_dir_name
            )
        with open(path_to_expect_html) as expect:
            expect_content = expect.read()
            with open(html_path) as html:
                html_content = html.read()
                assert expect_content == html_content

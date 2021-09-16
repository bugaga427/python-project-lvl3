from page_loader.downloader import download
from tempfile import TemporaryDirectory


def test_download_page():
    path_to_expect = 'tests/fixtures/page-loader-hexlet-repl-co-courses.html'
    with open(path_to_expect) as expect:
        with TemporaryDirectory() as tmp:
            tmp_dir_name = tmp
            file_path = download('https://ru.hexlet.io/courses', tmp_dir_name)
            expect_content = expect.read()
            with open(file_path) as result:
                assert expect_content == result.read()

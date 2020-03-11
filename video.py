import requests
from lxml import html, etree
from bs4 import BeautifulSoup
import concurrent.futures


class VideoType(Exception):
    pass


class LectureVideoType(VideoType):
    pass


class PracticeVideoType(VideoType):
    pass


class FindVideo:
    headers = None

    def __init__(self, file_name):
        self.file_name = file_name

    def run(self, video_id):
        print(f'doing {video_id}')

        page = self._load_page(video_id)
        video_type, video_url = self._parse_page(page)
        self._save_to_file(video_id, video_type, video_url)

    def _load_page(self, video_id):
        url = f'https://sexologvasilenko.ru/dashboard/test/orgazm-school' \
              f'/videos/?showvideo={video_id}'
        res = requests.get(url, headers=self.headers)
        return res.text

    @staticmethod
    def _parse_page(page):
        soup = BeautifulSoup(page, 'lxml')
        try:
            video_url = soup.find(id='iframe_video_0').attrs.get('src')
            video_type = soup.find(field='title').find_all('div')[0].text
        except AttributeError as e:
            video_url, video_type = None, None

        return video_url, video_type

    def _save_to_file(self, video_id, video_type, video_link):
        if video_type:
            with open(self.file_name, 'a') as f:
                f.write(f'{video_id}, {video_type}, {video_link}\n')

            print(f'{video_id}, {video_type}, {video_link}')


if __name__ == "__main__":
    new_video = FindVideo('output.txt')

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(1, 100):
            executor.map(new_video.run, range(i * 1000 + 150, i * 1000 + 850,
                                              4))



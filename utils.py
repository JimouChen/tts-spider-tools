# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import os
import json
import re
from moviepy.editor import AudioFileClip
from loguru import logger


class DownloaderHelper:

    @classmethod
    def download_video(cls, save_dir: str,
                       url: str,
                       cookies_path: str = None):
        FileUtils.check_root_path(save_dir)

        if cookies_path:
            cmd = f'you-get --cookies {cookies_path} -o {save_dir} {url}'
        else:
            cmd = f'you-get -o {save_dir} {url}'

        logger.info('downloading...')
        logger.debug(cmd)
        os.system(cmd)

    @classmethod
    def video2audio(cls, video_path: str, audio_path: str):
        FileUtils.check_root_path(audio_path)
        logger.debug('video to audio...')
        for video in os.listdir(video_path):
            v_path = os.path.join(video_path, video)
            a_path = os.path.join(audio_path, video.split('.mp4')[0] + '.mp3')
            audio_clip = AudioFileClip(v_path)
            audio_clip.write_audiofile(a_path)
        logger.success("video2audio successfully!")


class FileUtils:
    @staticmethod
    def check_root_path(root_path):
        if not os.path.exists(root_path):
            os.makedirs(root_path, exist_ok=True)
            logger.warning(f'mkdir path: {root_path}')

    @staticmethod
    def write2json(json_path: str, data):
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        logger.info(f'write json to: {json_path}')

    @staticmethod
    def load_json(json_path: str):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data

    @staticmethod
    def load_html(html_path: str):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()


class YouKuCrawler:

    @classmethod
    def get_video_url(cls, html_path: str, save_path: str):
        FileUtils.check_root_path(save_path)
        html = FileUtils.load_html(html_path)
        url_list = re.compile('href="(.+?)"').findall(html)
        url_list = ['https:' + url.split('html')[0] + 'html' for url in url_list]
        title_list = re.compile('title="(.+?)"').findall(html)
        data = [{
            'title': title,
            'url': url_list[idx]
        } for idx, title in enumerate(title_list)]
        save_path = os.path.join(save_path,
                                 html_path.split('/')[-1].split('.')[0] + '.json')
        FileUtils.write2json(save_path, data)

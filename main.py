# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
from utils import *

if __name__ == '__main__':
    cfg_data = FileUtils.load_json('./conf/conf.json')

    YouKuCrawler.get_video_url(
        './data/raw_html/xfdwj.html',
        cfg_data['path']['json']['save_path']
    )

    # youku会检查翻墙，所以下载时关闭代理
    DownloaderHelper.download_video(save_dir=cfg_data['path']['video']['save_dir'],
                                    url='https://v.youku.com/v_show/id_XNTg3MDQ5ODY1Ng==.html')

    DownloaderHelper.video2audio(
        cfg_data['path']['video']['save_dir'],
        cfg_data['path']['audio']['save_path'])

# tts-spider-tools
- Crawlers download online videos, convert video to audio, etc.

## Environment
- open command line

```bash
pip3 install -r requirements.txt
```

## Populate your config file

```json
{
  "path": {
    "video": {
      "save_dir": "./data/video/xfdwj",
      "cookies_path": ""
    },
    "audio": {
      "save_path": "./data/audio/xfdwj"
    },
    "json": {
      "save_path": "./data/json"
    }
  }
}
```

## Directory Structure
```bash
├── conf
│   └── conf.json
├── data
│   ├── audio
│   │   └── xfdwj
│   │       └── xxx.mp3
│   ├── json
│   │   └── xfdwj.json
│   ├── raw_html
│   │   └── xfdwj.html
│   └── video
│       └── xfdwj
│           └── xxx.mp4
├── main.py
├── requirements.txt
└── utils.py

```

- If the video you crawl requires VIP authentication, you need to fill in the cookies path, as follows

> [reference link](https://www.jianshu.com/p/62c0b1d332b6)

## Run
```bash
python3 main.py
```
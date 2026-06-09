import json
from pathlib import Path


def load_config(path: Path) -> dict:
    """读取 JSON 配置；缺文件返回 {}，坏 JSON 抛 ValueError。"""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise ValueError("invalid config") from exc

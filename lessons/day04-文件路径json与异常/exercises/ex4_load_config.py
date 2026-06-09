from pathlib import Path


def load_config(path: Path) -> dict:
    """读取 JSON 配置文件并返回 dict。

    - 文件不存在：返回空 dict {}（捕获 FileNotFoundError）。
    - 文件存在但不是合法 JSON：抛出 ValueError("invalid config")。
    """
    # TODO: 读 JSON，处理两种异常
    raise NotImplementedError

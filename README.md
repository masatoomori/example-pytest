# pytest

## Installation

```bash
poetry add pytest
```

## Setting

テストファイルのあるディレクトリに `__init__.py` を作成し、下記のように記述する。

```python
import sys
import os

sys.path.append('path/to/your/project/root')
```

## Usage

ファイル名を指定しないと、テストファイルを全て実行する。

```bash
poetry run pytest
```

詳細の結果を表示する場合は `-v` オプションを付ける。

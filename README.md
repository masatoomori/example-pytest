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

## Test Run

```bash
$ cd tests/module_1
$ poetry run pytest -v

Configuration file exists at /path/to/pypoetry, reusing this directory.

Consider moving TOML configuration files to /path/to/pypoetry, as support for the legacy directory will be removed in an upcoming release.
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- /path/to/test-pytest/.venv/bin/python
cachedir: .pytest_cache
rootdir: /path/to/test-pytest/tests/module_1
collected 10 items

test_prime.py::test_is_prime[is_prime_test_data0] PASSED                                                                                                        [ 10%]
test_prime.py::test_is_prime[is_prime_test_data1] PASSED                                                                                                        [ 20%]
test_prime.py::test_is_prime[is_prime_test_data2] PASSED                                                                                                        [ 30%]
test_prime.py::test_is_prime[is_prime_test_data3] PASSED                                                                                                        [ 40%]
test_prime.py::test_is_prime[is_prime_test_data4] PASSED                                                                                                        [ 50%]
test_prime.py::test_is_prime[is_prime_test_data5] PASSED                                                                                                        [ 60%]
test_prime.py::test_is_prime[is_prime_test_data6] PASSED                                                                                                        [ 70%]
test_prime.py::test_is_prime[is_prime_test_data7] PASSED                                                                                                        [ 80%]
test_prime.py::test_is_prime[is_prime_test_data8] PASSED                                                                                                        [ 90%]
test_prime.py::test_is_prime[is_prime_test_data9] PASSED                                                                                                        [100%]

========================================================================= 10 passed in 0.01s ==========================================================================
```

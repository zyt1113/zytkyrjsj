"""test_calculator.py —— 单元测试

实验03 步骤2 示例代码，使用 pytest 对 calculator 模块做测试。
本地运行：pytest -v
CI 中由 GitHub Actions 自动执行。
"""

import pytest

from calculator import add, multiply


def test_add():
    """测试加法"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    """测试乘法"""
    assert multiply(3, 4) == 12
    assert multiply(2, 0) == 0

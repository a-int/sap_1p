import os
import subprocess
import sys
from main import binary_search

def test_binary_search_basic():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 9) == 4
    assert binary_search(arr, 5) == 2
    assert binary_search(arr, 2) == -1

def test_cli_runs_with_env():
    target = os.getenv("SEARCH_TARGET", "11")

    cmd = [sys.executable, "main.py", target]
    cp = subprocess.run(cmd, capture_output=True, text=True)

    assert cp.returncode == 0
    assert f"Поиск значения: {target}" in cp.stdout


import shutil
import subprocess
import random
from a7d import Archive
from pathlib import Path

def test_using_tester_dir(tester_dir):
    if not isinstance(tester_dir, Archive):
        tester_dir = Archive(tester_dir)
    test_dir = Path('test-' + str(random.randint(10**58, 10**59 - 1)))
    tester_dir.to_directory(test_dir)
    result = subprocess.run(test_dir/'test').returncode
    shutil.rmtree(test_dir)
    return result

"""
Installs whisper in an isolated environment.
"""

import os
from pathlib import Path

from isolated_environment import IsolatedEnvironment  # type: ignore

TENSOR_VERSION = "2.1.2"
CUDA_VERSION = "cu121"
TENSOR_CUDA_VERSION = f"{TENSOR_VERSION}+{CUDA_VERSION}"
EXTRA_INDEX_URL = f"https://download.pytorch.org/whl/{CUDA_VERSION}"

HERE = Path(os.path.abspath(os.path.dirname(__file__)))


def unit_test() -> None:
    """Unit test."""
    from tempfile import TemporaryDirectory  # pylint: disable=import-outside-toplevel

    with TemporaryDirectory() as tmpdir:
        print(f"Using temporary directory {tmpdir}")
        iso_env = IsolatedEnvironment(HERE / "transcribe_anything_env")
        iso_env.install_environment()
        iso_env.pip_install(
            package=f"torch=={TENSOR_VERSION}",
            build_options=EXTRA_INDEX_URL,
            full_isolation=False,
        )
        iso_env.pip_install(
            package="openai-whisper", build_options=None, full_isolation=False
        )
        iso_env.run(["whisper", "--help"])


if __name__ == "__main__":
    unit_test()

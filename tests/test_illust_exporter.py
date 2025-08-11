import os
import shutil
import sys
from unittest.mock import patch
from PIL import Image
import pytest

from src import illust_exporter


@pytest.fixture
def setup_test_environment():
    test_dir = "test_temp"
    os.makedirs(test_dir, exist_ok=True)
    # Create a dummy PSD file (as a PNG renamed to PSD)
    psd_path = os.path.join(test_dir, "test.psd")
    img = Image.new("RGB", (1000, 1000), color="red")
    png_path = os.path.join(test_dir, "test.png")
    img.save(png_path, "png")
    os.rename(png_path, psd_path)

    yield test_dir

    # Teardown
    shutil.rmtree(test_dir)
    output_dir_pixiv = f"{test_dir}_pixiv"
    if os.path.exists(output_dir_pixiv):
        shutil.rmtree(output_dir_pixiv)
    output_dir_other = f"{test_dir}_other"
    if os.path.exists(output_dir_other):
        shutil.rmtree(output_dir_other)


def test_e2e_pixiv(setup_test_environment):
    """Tests the 'pixiv' output type."""
    test_dir = setup_test_environment
    output_dir_pixiv = f"{test_dir}_pixiv"
    test_args = ["src/illust_exporter.py", test_dir, "pixiv"]
    with patch.object(sys, "argv", test_args):
        illust_exporter.main()

    # Check if output folder is created
    assert os.path.exists(output_dir_pixiv)
    # Check if JPEG file is created
    jpeg_path = os.path.join(output_dir_pixiv, "test.jpeg")
    assert os.path.exists(jpeg_path)
    # Check file size (assuming pixiv max size is 32MB from config)
    assert os.path.getsize(jpeg_path) <= 32 * 1024 * 1024


def test_e2e_other(setup_test_environment):
    """Tests the 'other' output type."""
    test_dir = setup_test_environment
    output_dir_other = f"{test_dir}_other"
    test_args = ["src/illust_exporter.py", test_dir, "other"]
    with patch.object(sys, "argv", test_args):
        illust_exporter.main()

    assert os.path.exists(output_dir_other)
    jpeg_path = os.path.join(output_dir_other, "test.jpeg")
    assert os.path.exists(jpeg_path)
    assert os.path.getsize(jpeg_path) <= 10 * 1024 * 1024
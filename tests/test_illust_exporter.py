import unittest
import os
import shutil
import sys
from unittest.mock import patch
from PIL import Image

import illust_exporter as illust_exporter

class TestIllustExporter(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_temp"
        self.output_dir_pixiv = f"{self.test_dir}_pixiv"
        self.output_dir_other = f"{self.test_dir}_other"
        os.makedirs(self.test_dir, exist_ok=True)
        # Create a dummy PSD file (as a PNG renamed to PSD)
        self.psd_path = os.path.join(self.test_dir, "test.psd")
        img = Image.new("RGB", (1000, 1000), color="red")
        png_path = os.path.join(self.test_dir, "test.png")
        img.save(png_path, "png")
        os.rename(png_path, self.psd_path)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(self.output_dir_pixiv):
            shutil.rmtree(self.output_dir_pixiv)
        if os.path.exists(self.output_dir_other):
            shutil.rmtree(self.output_dir_other)

    def test_e2e_pixiv(self):
        """Tests the 'pixiv' output type."""
        test_args = ["src/illust_exporter.py", self.test_dir, "pixiv"]
        with patch.object(sys, "argv", test_args):
            illust_exporter.main()

        # Check if output folder is created
        self.assertTrue(os.path.exists(self.output_dir_pixiv))
        # Check if JPEG file is created
        jpeg_path = os.path.join(self.output_dir_pixiv, "test.jpeg")
        self.assertTrue(os.path.exists(jpeg_path))
        # Check file size (assuming pixiv max size is 32MB from config)
        self.assertLessEqual(os.path.getsize(jpeg_path), 32 * 1024 * 1024)

    def test_e2e_other(self):
        """Tests the 'other' output type."""
        test_args = ["src/illust_exporter.py", self.test_dir, "other"]
        with patch.object(sys, "argv", test_args):
            illust_exporter.main()

        self.assertTrue(os.path.exists(self.output_dir_other))
        jpeg_path = os.path.join(self.output_dir_other, "test.jpeg")
        self.assertTrue(os.path.exists(jpeg_path))
        self.assertLessEqual(os.path.getsize(jpeg_path), 10 * 1024 * 1024)


if __name__ == "__main__":
    unittest.main()

import unittest
import os
import shutil
import sys
from unittest.mock import patch
from PIL import Image

import illust_exporter

class TestIllustExporter(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_temp"
        self.output_dir_pixiv = f"{self.test_dir}_pixiv"
        self.output_dir_other = f"{self.test_dir}_other"
        os.makedirs(self.test_dir, exist_ok=True)
        # Create a dummy PSD file (as a PNG renamed to PSD)
        self.psd_path = os.path.join(self.test_dir, "test.psd")
        img = Image.new('RGB', (1000, 1000), color = 'red')
        png_path = os.path.join(self.test_dir, "test.png")
        img.save(png_path, 'png')
        os.rename(png_path, self.psd_path)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(self.output_dir_pixiv):
            shutil.rmtree(self.output_dir_pixiv)
        if os.path.exists(self.output_dir_other):
            shutil.rmtree(self.output_dir_other)

    def test_e2e(self):
        test_args = ["illust_exporter.py", self.test_dir, "pixiv", "other"]
        with patch.object(sys, 'argv', test_args):
            illust_exporter.main()

            # Check if output folders are created
            self.assertTrue(os.path.exists(self.output_dir_pixiv))
            self.assertTrue(os.path.exists(self.output_dir_other))

            # Check if JPEG file is created in pixiv folder
            jpeg_path_pixiv = os.path.join(self.output_dir_pixiv, "test.jpeg")
            self.assertTrue(os.path.exists(jpeg_path_pixiv))

            # Check if JPEG file is created in other folder
            jpeg_path_other = os.path.join(self.output_dir_other, "test.jpeg")
            self.assertTrue(os.path.exists(jpeg_path_other))

            # Check file sizes
            self.assertLessEqual(os.path.getsize(jpeg_path_pixiv), 32 * 1024 * 1024)
            self.assertLessEqual(os.path.getsize(jpeg_path_other), 10 * 1024 * 1024)

if __name__ == '__main__':
    unittest.main()

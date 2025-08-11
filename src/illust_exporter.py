import argparse
import os
import shutil
import json
from PIL import Image


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        return json.load(f)


def resize_image(img, path, max_size_mb):
    max_size_bytes = max_size_mb * 1024 * 1024
    quality = 95

    while True:
        img.save(path, "jpeg", quality=quality)
        if os.path.getsize(path) <= max_size_bytes:
            break

        if quality > 10:
            quality -= 5
        else:
            width, height = img.size
            img = img.resize((int(width * 0.9), int(height * 0.9)), Image.Resampling.LANCZOS)


def main():
    OUTPUT_SPECS = load_config()
    parser = argparse.ArgumentParser(description="illust-exporter")
    parser.add_argument("folder_path", help="Path to the folder containing PSD files.")
    parser.add_argument(
        "output_types", nargs="+", help="Output types (e.g., pixiv, other)"
    )
    args = parser.parse_args()

    for output_type in args.output_types:
        if output_type not in OUTPUT_SPECS:
            print(f"Unknown output type: {output_type}")
            continue

        spec = OUTPUT_SPECS[output_type]
        output_folder_name = f"{os.path.basename(args.folder_path)}_{output_type}"
        output_path = os.path.join(
            os.path.dirname(args.folder_path), output_folder_name
        )

        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        shutil.copytree(args.folder_path, output_path)

        for filename in os.listdir(output_path):
            if filename.lower().endswith(".psd"):
                psd_path = os.path.join(output_path, filename)
                img = Image.open(psd_path)

                jpeg_path = os.path.join(
                    output_path, f"{os.path.splitext(filename)[0]}.jpeg"
                )
                resize_image(img, jpeg_path, spec["max_size_mb"])

                os.remove(psd_path)

        print(f"Successfully exported to {output_path}")


if __name__ == "__main__":
    main()

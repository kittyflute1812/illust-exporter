# illust-exporter
イラストを特定サイト用に書き出すツールです


## Usage

First, install the tool using `pipx`:

```bash
pipx install git+https://github.com/kittyflute1812/illust-exporter.git
```

Then, you can use the `illust-exporter` command:

```bash
illust-exporter [folder_path] [output_type_1] [output_type_2] ...
```

**Arguments:**

*   `folder_path`: The path to the folder containing your PSD files.
*   `output_types`: One or more output types to convert the images to. The available types are defined in `src/config.json`. Currently, you can use `pixiv` and `other`.

**Example:**

Let's say you have a folder named `my_art` on your Desktop containing your PSD files.

```
/Users/your_user/Desktop/my_art/
├───image1.psd
└───image2.psd
```

To convert these images for both `pixiv` and `other` types, you would run:

```bash
illust-exporter /Users/your_user/Desktop/my_art pixiv other
```

This will create two new folders on your Desktop:

*   `/Users/your_user/Desktop/my_art_pixiv`
*   `/Users/your_user/Desktop/my_art_other`

These new folders will contain the images from `my_art` converted to JPEG, with file sizes optimized for each output type. The original PSD files will be removed from the new folders.

## Development

For local development, you can run the script directly.

```bash
# installation
poetry install

# execution
poetry run illust-exporter [path/to/your/psd_folder] [output_type_1] [output_type_2] ...
```

## Testing

To run the tests, execute the following command from the root of the project:

```bash
poetry run pytest
```

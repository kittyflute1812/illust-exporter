# illust-exporter
イラストを特定サイト用に書き出すツールです

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/illust-exporter.git
    cd illust-exporter
    ```

2.  Install the project dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage (after installation)

After installation, you can use the command-line tool.

```bash
poetry run illust-exporter [path/to/your/psd_folder] [output_type_1] [output_type_2] ...
```

### Example

```bash
poetry run illust-exporter /Users/(Username)/Desktop/my_illustrations pixiv other
```

This command will create two new folders, `my_illustrations_pixiv` and `my_illustrations_other`, in the same directory as the source folder, with the converted images inside.

## Development

For local development, you can run the script directly.

```bash
poetry run illust-exporter [path/to/your/psd_folder] [output_type_1] [output_type_2] ...
```

## Building and Distributing

1.  Build the package:

    ```bash
    poetry build
    ```

2.  Publish to PyPI:

    ```bash
    poetry publish
    ```

## Testing

To run the tests, execute the following command from the root of the project:

```bash
poetry run pytest
```

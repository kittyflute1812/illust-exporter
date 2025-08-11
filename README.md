# illust-exporter
イラストを特定サイト用に書き出すツールです

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/illust-exporter.git
    cd illust-exporter
    ```

2.  Install the project in editable mode:

    ```bash
    pip install -e .
    ```

## Usage

```bash
illust-exporter [path/to/your/psd_folder] [output_type_1] [output_type_2] ...
```

### Example

```bash
illust-exporter /Users/(Username)/Desktop/my_illustrations pixiv other
```

This command will create two new folders, `my_illustrations_pixiv` and `my_illustrations_other`, in the same directory as the source folder, with the converted images inside.

## Testing

To run the tests, execute the following command from the root of the project:

```bash
python3 -m unittest discover tests
```

# illust-exporter

## Project Overview

`illust-exporter` is a Python command-line tool that processes a folder of PSD files. It copies the folder, renames it based on the specified output type, and converts the PSD files into a different format and size.

The project is structured as a Python package with the main source code in the `src` directory and tests in the `tests` directory. It uses a `pyproject.toml` file for packaging and dependency management.

## How to Run

1.  **Installation**: Install the project in editable mode from the root of the project:
    ```bash
    pip install -e .
    ```

2.  **Execution**: Run the tool from the command line:
    ```bash
    illust-exporter [path/to/your/psd_folder] [output_type_1] [output_type_2] ...
    ```

### Configuration

The output specifications (format, size, etc.) are defined in `src/config.json`.

### Output Types

-   **pixiv**:
    -   File Format: JPEG
    -   Data Size: Up to 32MB per image
-   **other**:
    -   File Format: JPEG
    -   Data Size: Up to 10MB per image

## Testing

To run the tests, execute the following command from the root of the project:

```bash
python3 -m unittest discover tests
```

## Tech Stack

-   Python
-   Pillow
-   psd-tools

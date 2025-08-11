# illust-exporter

## About this Project

`illust-exporter` is a Python command-line tool that processes a folder of PSD files. It copies the folder, renames it based on the specified output type, and converts the PSD files into a different format and size.

## Key Technologies

- Python
- Poetry for dependency management
- pytest for testing
- Pillow for image manipulation
- psd-tools for PSD file parsing

## High-level Code Structure

- `src/illust_exporter.py`: The main entry point of the application.
- `src/config.json`: Configuration for output formats and sizes.
- `tests/`: Contains the tests for the application.
- `pyproject.toml`: Defines project metadata and dependencies.

## Key Commands

- **Installation**: `pip install -e .`
- **Execution**: `illust-exporter [path/to/your/psd_folder] [output_type_1] [output_type_2] ...`
- **Testing**: `poetry run pytest`

## Configuration

The output specifications (format, size, etc.) are defined in `src/config.json`.
# illust-exporter

## Project Overview

`illust-exporter` is a Python script that processes a folder of PSD files. It copies the folder, renames it based on the specified output type, and converts the PSD files into a different format and size.

## How to Run

The script is executed from the command line with the following arguments:

- **Folder Path**: The path to the folder containing the PSD files.
- **Output Type**: The type of output to generate. Multiple output types can be specified.

### Output Types

1.  **pixiv**:
    -   File Format: JPEG
    -   Data Size: Up to 32MB per image

2.  **other**:
    -   File Format: JPEG
    -   Data Size: Up to 10MB per image

## Future Development

-   A desktop application version is planned for future development.
-   More output types will be added in the future.

## Tech Stack

-   Python

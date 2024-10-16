# chartctl

This is a Python command-line tool that generates flowcharts based on a JSON configuration file, and outputs them as a PNG.

## Requirements

- `graphviz` Python package (`pip install graphviz`)
- Graphviz system package (for the `dot` command)

### Installing the Graphviz System Package

- **Ubuntu/Debian**: `sudo apt-get install graphviz`
- **MacOS (Homebrew)**: `brew install graphviz`

## Installation

1. Clone this repository or download the script:

    ```bash
    git clone https://github.com/jsf0/chartctl.git
    cd chartctl
    ```

2. Install the required Python package:

    ```bash
    pip install graphviz
    ```

## Usage

### Command-Line Options

- `-i, --input` (required): Path to the JSON configuration file.
- `-o, --output` (optional): Path to save the output PNG file (without the PNG extension). Defaults to `flowchart.png`.

### Example Command

```bash
chartctl.py -i flowchart_config.json -o output_flowchart
```

### Example configs
See the examples directory for sample configurations. 

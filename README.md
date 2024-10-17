# chartctl

This is a Python command-line tool that generates flowcharts based on a JSON configuration file, and outputs them as a PNG.

## Requirements

- `graphviz` Python package (`pip install graphviz`)
- Graphviz binary (for the `dot` command)

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
See the examples directory for more sample configurations.

```
{
  "nodes": {
    "application_received": { "label": "Application Received", "shape": "oval", "fillcolor": "lightblue", "style": "filled" },
    "initial_interview": { "label": "Initial Interview", "shape": "rectangle", "fillcolor": "lightgreen", "style": "filled" },
    "background_check": { "label": "Background Check", "shape": "rectangle", "fillcolor": "lightyellow", "style": "filled" },
    "offer_made": { "label": "Offer Made?", "shape": "diamond", "fillcolor": "yellow", "style": "filled" },
    "offer_accepted": { "label": "Offer Accepted?", "shape": "diamond", "fillcolor": "lightyellow", "style": "filled" },
    "onboarding": { "label": "Onboarding Process", "shape": "rectangle", "fillcolor": "lightpink", "style": "filled" },
    "rejected": { "label": "Candidate Rejected", "shape": "rectangle", "fillcolor": "gray", "style": "filled" },
    "hired": { "label": "Candidate Hired", "shape": "oval", "fillcolor": "lightgray", "style": "filled" }
  },
  "connectors": [
    { "from": "application_received", "to": "initial_interview", "label": "Screened" },
    { "from": "initial_interview", "to": "background_check", "label": "Passed Interview" },
    { "from": "background_check", "to": "offer_made", "label": "Clear" },
    { "from": "offer_made", "to": "offer_accepted", "label": "Yes" },
    { "from": "offer_made", "to": "rejected", "label": "No", "color": "red" },
    { "from": "offer_accepted", "to": "onboarding", "label": "Yes", "color": "green" },
    { "from": "offer_accepted", "to": "rejected", "label": "No", "color": "red" },
    { "from": "onboarding", "to": "hired", "label": "Completed" }
  ]
}
```



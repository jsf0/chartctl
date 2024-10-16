#!/usr/bin/env python3
import json
import argparse
import os
from graphviz import Digraph

def validate_json(config):
    """
    Validate the structure of the JSON file.
    Ensure it has "nodes" and "edges" as top-level keys.
    """
    if not isinstance(config, dict):
        raise ValueError("JSON root must be an object (dictionary)")

    if 'nodes' not in config:
        raise ValueError('The JSON file must contain a "nodes" section.')
    
    if not isinstance(config['nodes'], dict):
        raise ValueError('"nodes" must be a dictionary of node definitions.')

    if 'edges' not in config:
        raise ValueError('The JSON file must contain an "edges" section.')
    
    if not isinstance(config['edges'], list):
        raise ValueError('"edges" must be a list of edge definitions.')

    # Optionally: Validate node and edge formats more strictly if needed

def generate_flowchart_from_json(config_file, output_file):
    """
    Generate a flowchart based on the provided JSON configuration file.
    """
    try:
        # Check if the input file exists
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"The input file '{config_file}' does not exist.")
        
        # Read and parse the JSON file
        with open(config_file, 'r') as f:
            config = json.load(f)

        # Validate the structure of the JSON
        validate_json(config)
        
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return
    except json.JSONDecodeError as json_error:
        print(f"Error parsing JSON: {json_error}")
        return
    except ValueError as val_error:
        print(f"Validation error: {val_error}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Create a new directed graph for the flowchart
    dot = Digraph(comment="Flowchart", format="png")

    # Add nodes with optional shape, fillcolor, style, and color
    if 'nodes' in config:
        for node, attributes in config['nodes'].items():
            label = attributes.get('label', node)
            shape = attributes.get('shape', 'rectangle')  # Default shape is rectangle if not specified
            fillcolor = attributes.get('fillcolor', 'white')  # Default fill color is white
            style = attributes.get('style', 'solid')  # Default style is solid
            color = attributes.get('color', 'black')  # Default border color is black
            dot.node(node, label, shape=shape, fillcolor=fillcolor, style=style, color=color)

    # Add edges with optional labels and colors
    if 'edges' in config:
        for edge in config['edges']:
            src = edge['from']
            dst = edge['to']
            label = edge.get('label', '')  # Optional label
            color = edge.get('color', 'black')  # Default edge color is black
            dot.edge(src, dst, label, color=color)

    # Render the flowchart to the specified output file
    dot.render(output_file)
    print(f"Flowchart saved as {output_file}.png")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a flowchart from a JSON configuration file.")
    
    # Input JSON file path
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input JSON configuration file')
    
    # Output file path (default is "flowchart.png")
    parser.add_argument('-o', '--output', type=str, default='flowchart', help='Path to save the output PNG file (without extension)')
    
    # Parse the arguments
    args = parser.parse_args()

    # Call the flowchart generation function with the provided input and output paths
    generate_flowchart_from_json(args.input, args.output)

if __name__ == "__main__":
    main()


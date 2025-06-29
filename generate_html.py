#!/usr/bin/env python3
"""
Script to generate HTML diagram from Mermaid markdown file.
"""

import re
import os
from pathlib import Path


def extract_mermaid_from_md(md_file_path):
    """Extract Mermaid diagram content from markdown file."""
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find Mermaid code blocks using regex
    pattern = r'```mermaid\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if not matches:
        raise ValueError("No Mermaid diagram found in the markdown file")
    
    # Return the first Mermaid diagram found
    return matches[0].strip()


def generate_html(mermaid_content, title="Mermaid Diagram", output_file="diagram.html"):
    """Generate HTML file with the Mermaid diagram."""
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@11.7.0/dist/mermaid.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }}
        .mermaid {{
            text-align: center;
            background-color: #fafafa;
            padding: 20px;
            border-radius: 4px;
            border: 1px solid #e1e1e1;
            overflow: auto;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 0.9em;
        }}
        .instructions {{
            text-align: center;
            margin-bottom: 15px;
            color: #888;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>

        <div class="mermaid">
{mermaid_content}
        </div>
        <div class="footer">
            Generated from han.md
        </div>
    </div>

    <script>
        mermaid.initialize({{ 
            startOnLoad: true,
            theme: 'default',
            flowchart: {{
                useMaxWidth: false,
                htmlLabels: true
            }}
        }});
    </script>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_template)
    
    return output_file


def main():
    """Main function to process the markdown file and generate HTML."""
    # File paths
    md_file = "han.md"
    dynasty = md_file.split(".")[0]
    output_file = f"{dynasty}.html"

    try:
        # Check if the markdown file exists
        if not os.path.exists(md_file):
            print(f"Error: {md_file} not found!")
            return
        
        print(f"Reading Mermaid diagram from {md_file}...")
        mermaid_content = extract_mermaid_from_md(md_file)
        
        print(f"Generating HTML file: {output_file}...")
        generated_file = generate_html(
            mermaid_content, 
            title=f"{dynasty.capitalize()} Dynasty", 
            output_file=output_file
        )
        
        print(f"Successfully generated {generated_file}")
        print(f"Open {os.path.abspath(generated_file)} in your browser to view the diagram")
        
        # Get the absolute path for easy copying
        abs_path = os.path.abspath(generated_file)
        print(f"Full path: file://{abs_path}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

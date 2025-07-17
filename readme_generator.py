from InquirerPy import prompt
from rich.console import Console

console = Console()

license_options = [
    "MIT License",
    "Apache License 2.0",
    "GNU General Public License (GPL v3)",
    "GNU Lesser General Public License (LGPL v3)",
    "Mozilla Public License 2.0 (MPL 2.0)",
    "Creative Commons Licenses (CC0, CC BY, etc.)",
    "Unlicense"
]

questions = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "installation", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Instructions:"},
    {"type": "list", "name": "license", "message": "Choose a license:", "choices": license_options},
    {"type": "input", "name": "author", "message": "Author Contact Information:"}
]

answers = prompt(questions)

readme_content = f"""# {answers['title']}

## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
This project is licensed under the {answers['license']}.

## Author
{answers['authort']}
"""

with open("README.md", "w") as f:
    f.write(readme_content)

console.print("[bold green]README.md has been successfully created![/bold green]")

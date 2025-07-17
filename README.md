# ReadMeGenerator

A Python-based tool that helps you quickly create professional README.md files for your GitHub projects. Simply run the script, answer a few questions about your project, and get a well-formatted README file instantly.

## Description

This interactive README generator uses Python to prompt you for essential project information and automatically generates a comprehensive README.md file. Perfect for developers who want to create consistent, professional documentation for their projects.

## Features

- Interactive prompts for project details
- Multiple license options to choose from
- Professional formatting with proper sections
- Beautiful terminal interface using Rich library
- Easy to use and customize

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GeorgePrempeh/ReadMeGenerator.git
   ```

2. Navigate into the project directory:

   ```bash
   cd ReadMeGeneratorProject
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # On Windows PowerShell
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate a README file, simply run:

```bash
python readme_generator.py
```

Follow the interactive prompts to provide:

- Project title
- Project description
- Installation instructions
- Usage instructions
- License selection
- Author information

The script will create a new `README.md` file in your current directory.

## Requirements

- Python 3.7+
- InquirerPy
- Rich

## License

This project is licensed under the MIT License.

## Author

GP Group

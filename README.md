# Kata Number to French Converter

This project provides a Python library, command-line interface (CLI), and web API for converting non-negative integers into their French word equivalents. The supported number range is 0 to 999,999, with options for both standard French and Belgian French.

## Project Structure

```
kata_number_to_french_converter/
├── README.md
├── app.py
├── cli.py
├── converter.py
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── tests
└──── test_converter.py
```

### Files Description

- **README.md**: Documentation file.
- **app.py**: Flask web application for number to French conversion.
- **cli.py**: Command-line interface for number to French conversion.
- **converter.py**: Core conversion logic encapsulated in `FrenchNumberTranslator` class.
- **poetry.lock**: Poetry lock file for dependency management.
- **pyproject.toml**: Poetry configuration file.
- **requirements.txt**: List of dependencies.
- **tests/**: Directory containing unit tests.

## Installation

1. Clone the repository: `git clone https://github.com/ajosegun/kata_number_to_french_converter.git`
2. Navigate to the project directory: `cd kata_number_to_french_converter`
3. To install the project dependencies, run:

```bash
pip install -r requirements.txt
```

or if you prefer Poetry:

```bash
poetry install
```

## Usage

Activate a virtual environment

```bash
poetry shell
```

### 1. Web API

1. Start the Web server:
   ```
   flask run
   ```
   By default, the server will run on http://127.0.0.1:5000.
2. To convert a number, make a GET request to /translate with the number query parameter.

```bash
curl "http://127.0.0.1:5000/translate?number=<number>"
```

Replace `<number>` with the number you want to translate.

3. The API will respond with the translated number.

For a request to `http://127.0.0.1:5000/translate?number=123`

You will get the below as a response

```json
{
  "translation": "cent-vingt-trois"
}
```

### 2. CLI

1. Run the CLI interface:

```bash
   python cli.py <number> --lang <language>
```

<number>: The number to convert.
--lang: Language variant (fr for standard French, be for Belgian French). Default is fr.

### 3. Python Library

You can use the converter directly in your Python code by importing translate_to_french function:

```python
from converter import translate_to_french

print(translate_to_french(123))  # cent-vingt-trois
```

## Testing

Testing
Unit tests are provided in the `tests` directory. To run the tests, use:

```bash
python -m unittest tests.test_converter
```

## See some tools and prompts used

[Tools](Tools.md)

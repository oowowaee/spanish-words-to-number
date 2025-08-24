# Spanish Word to Number

A Python package that converts Spanish words representing numbers to integers.

## Installation

```bash
pip install spanish-words-to-number
```

## Usage

```python
from spanish_word_to_number import spanish_words_to_number

# Convert Spanish words to numbers
result = spanish_words_to_number("veinticinco")
print(result)  # Output: 25

# Handle complex numbers
result = spanish_words_to_number("DOS MILLONES CIENTO CATORCE MIL QUINIENTOS SIETE")
print(result)  # Output: 2114507

# Case insensitive and accent insensitive
result = spanish_words_to_number("un millón")
print(result)  # Output: 1000000
```

## Features

- Converts Spanish number words to integers
- Handles compound numbers (e.g., "veinticinco" → 25)
- Supports large numbers up to millions
- Case insensitive
- Accent insensitive
- Handles plural forms

## Examples

- `"seis"` → 6
- `"veintitres"` → 23
- `"cuatrocientos"` → 400
- `"mil"` → 1000
- `"un millón"` → 1000000
- `"DOS MILLONES CIENTO CATORCE MIL QUINIENTOS SIETE"` → 2114507

## Development

To install in development mode:

```bash
git clone <repository-url>
cd spanish-words-to-number
pip install -e .
```

## Testing

```bash
python -m pytest tests/
```

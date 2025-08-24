#!/usr/bin/env python3
"""
Example usage of the spanish-word-to-number package
"""

from spanish_words_to_number import spanish_words_to_number

def main():
    # Test cases
    test_cases = [
        "seis",
        "veinticinco", 
        "cuatrocientos",
        "mil",
        "un millón",
        "DOS MILLONES CIENTO CATORCE MIL QUINIENTOS SIETE",
        "veintitres",
        "novecientos",
        "quinientos"
    ]
    
    print("Spanish Word to Number Converter")
    print("=" * 40)
    
    for test_case in test_cases:
        result = spanish_words_to_number(test_case)
        print(f"{test_case:35} → {result:,}")

if __name__ == "__main__":
    main() 
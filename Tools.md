### 1. ChatGPT

1. To create ReadMe

**Prompt**

Create a run documentation for this python project. Here is my project structure.

kata-number-to-french-converter
--README.md  
--app.py  
--cli.py  
--converter.py  
--poetry.lock  
--pyproject.toml  
--requirements.txt
--tests
----**init**.py
----test_converter.py

2. To create class doc string

**Prompt**

Write a docstring for a Python class that converts non-negative integers into their French word equivalents.
This class support numbers ranging from 0 to 999,999 and provide options for specifying the language variant (fr french, bg beligum)

3. To create test cases

**Prompt**
Duplicate the example test cases based on the input data

Example
self.assertEqual(translate_to_french(0), "zéro")

Input data
[0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]

### 2. CodeGPT

As pair-programming partner.

6/22:
Documenting python code 
https://realpython.com/documenting-python-code/#commenting-vs.-documenting-code

- Comments are not documentation. Comments help project maintainers understand past design decisions and what the code is doing. 
- Documenting code helps end-users understand your API.
- For light and accessible documentation Python uses docstrings, consisting of triple-double quotes (""") to document code within the code itself.
- By convention, docstrings are placed at the top of an object's definition (such as a class or function). Docstrings placed this way will be printed when the user checks an object's definition with the built-in "help" function.
- The more public your project the more critical good documentation is. All projects should at least include a Readme giving an overview, and code samples illustrating how the API works. More public projects should also include further details such as how to contribute and more extensive reference material.
- Example documentation: https://docs.djangoproject.com/en/2.2/

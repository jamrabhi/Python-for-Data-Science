
# ft_package

A small demonstration package created as part of the 42 Python module.  
It provides a simple utility function: **`count_in_list`**, which counts how many times a given value appears in a list.

----------

## 📦 Installation

After building your package, you can install it using:

`pip install ./dist/ft_package-0.0.1.tar.gz` 

or

`pip install ./dist/ft_package-0.0.1-py3-none-any.whl` 

Once installed, it will appear in:

`pip list
pip show -v ft_package` 

----------

## 🧰 Usage

Example script using the package:

```bash
from ft_package import count_in_list
```
```python
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
----------

## 📝 Functions

### `count_in_list(lst: list, value) -> int`

Counts the number of occurrences of `value` inside the list `lst`.

**Parameters**

-   `lst` — a list of elements
    
-   `value` — the element to count
    

**Returns**

-   An integer representing how many times `value` appears in `lst`
    

----------

## 📄 Project structure

```text
ft_package/
	__init__.py
	count_in_list.py

pyproject.toml
README.md
LICENSE
``` 

----------

## 👤 Author

-   **Name:** jamrabhi
    
-   **Email:** jamrabhi@student.42.fr
    
-   **GitHub:** [https://github.com/jamrabhi/](https://github.com/jamrabhi/)
    

----------

## 📜 License

This project is licensed under the MIT License.  
See the `LICENSE` file for more details.
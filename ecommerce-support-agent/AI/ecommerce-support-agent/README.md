# Ecommerce Support Agent

## Overview
The Ecommerce Support Agent project provides a set of tools and functionalities to assist customers with their orders, returns, and frequently asked questions. It is designed to streamline customer support processes for an ecommerce platform.

## Features
- Check the status of customer orders.
- Initiate returns for delivered orders.
- Lookup answers to common questions through an FAQ database.

## Project Structure
```
ecommerce-support-agent
├── src
│   ├── __init__.py
│   ├── tools.py
│   ├── api.py
│   └── db.py
├── tests
│   ├── __init__.py
│   └── test_tools.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ecommerce-support-agent.git
   ```
2. Navigate to the project directory:
   ```
   cd ecommerce-support-agent
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the tools provided by this project, you can import the functions from the `tools.py` module in your Python scripts. For example:

```python
from src.tools import get_order_status, initiate_return, faq_lookup

# Check order status
status = get_order_status("ORD123456")
print(status)

# Initiate a return
return_info = initiate_return("ORD789012", "Item was defective")
print(return_info)

# Lookup FAQ
faq_response = faq_lookup("return policy")
print(faq_response)
```

## Running Tests
To ensure that the functionalities work as expected, you can run the unit tests provided in the `tests` directory:

```
pytest tests/test_tools.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
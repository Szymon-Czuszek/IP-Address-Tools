# IP Address Tools

This Python module provides functions for working with IP addresses, including converting IP addresses to binary representation, determining their classes, and comparing them based on subnetting information.

## Functions

### 1. `convert_ip_to_binary(ip_address)`

Converts an IP address to a list of binary strings for each octet.

**Parameters:**

- `ip_address (str)`: The input IP address in dot-decimal notation.

**Returns:**

- `list`: A list of binary strings representing each octet.

**Example Usage:**

```python
from ip_address_tools import convert_ip_to_binary

binary_representation = convert_ip_to_binary("10.10.112.34")
print(binary_representation)
# Output: ['00001010', '00001010', '01110000', '00100010']
```

### 2. `get_ip_class_info(ip_address)`
Determines the class information of an IP address.

**Parameters:**

ip_address (str): The input IP address in dot-decimal, binary, or hex notation.

**Returns:**

tuple: A tuple containing the IP class, subnet mask length, and default subnet mask.
  
**Example Usage:**

```python
from ip_address_tools import get_ip_class_info

class_info = get_ip_class_info("192.168.1.1")
print(class_info)
# Output: ('C', 24, '255.255.255.0')
```

### 3. `convert_ip_format(ip_address, output_format = 'b')`
Converts an IP address between different formats (binary, hex, decimal).

**Parameters:**

ip_address (str): The input IP address.
output_format (str, optional): The desired output format ('b' for binary, 'h' for hex, 'd' for decimal). Default is 'b'.

**Returns:**

str: The converted IP address in the specified format.

**Example Usage:**

```python
from ip_address_tools import convert_ip_format

converted_ip = convert_ip_format("192.168.241.14", output_format='b')
print(converted_ip)
# Output: '192.168.241.14'
```

### 4. `compare_ip_addresses(ip1, ip2, mask1 = None, mask2 = None)`
Compares two IP addresses based on subnetting information.

**Parameters:**

ip1 (str): The first IP address in dot-decimal, binary, or hex notation.
ip2 (str): The second IP address in dot-decimal, binary, or hex notation.
mask1 (str, optional): The subnet mask for the first IP address.
mask2 (str, optional): The subnet mask for the second IP address.

**Returns:**

bool: True if the two IPs are subnets of the same net, False otherwise.
  
**Example Usage:**

```python
from ip_address_tools import compare_ip_addresses

result = compare_ip_addresses("10.10.112.34", "10.10.119.254")
print(result)
# Output: True
```

### The End

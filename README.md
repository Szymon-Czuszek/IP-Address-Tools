# IP Address Tools

A simple Python module with functions for working with IP addresses, including converting IP addresses to binary representation, determining their classes, and comparing them based on subnetting information.

## Functions

### 1. `convert_ip_to_binary(ip_address)`

Converts an IP address to a list of binary strings for each octet.

**Parameters:**
- `ip_address (str)`: The input IP address in dot-decimal notation.

**Returns:**
- `list`: A list of binary strings representing each octet.

### 2. `get_ip_class_info(ip_address)`

Determines the class information of an IP address.

**Parameters:**
- `ip_address (str)`: The input IP address in dot-decimal notation.

**Returns:**
- `tuple`: A tuple containing the IP class, subnet mask length, and default subnet mask.

### 3. `compare_ip_addresses(ip1, ip2, mask1=None, mask2=None)`

Compares two IP addresses based on subnetting information.

**Parameters:**
- `ip1 (str)`: The first IP address in dot-decimal notation.
- `ip2 (str)`: The second IP address in dot-decimal notation.
- `mask1 (str, optional)`: The subnet mask for the first IP address.
- `mask2 (str, optional)`: The subnet mask for the second IP address.

**Returns:**
- `bool`: True if the two IPs belong to different subnets, False otherwise.

## Example Usage

```python
from ip_address_tools import convert_ip_to_binary, get_ip_class_info, compare_ip_addresses

# Example 1
binary_representation = convert_ip_to_binary("10.10.112.34")
print(binary_representation)
# Output: ['00001010', '00001010', '01110000', '00100010']

# Example 2
class_info = get_ip_class_info("10.10.112.34")
print(class_info)
# Output: ('A', 8, '255.0.0.0')

# Example 3
result = compare_ip_addresses("10.10.112.34", "10.10.119.254")
print(result)
# Output: True

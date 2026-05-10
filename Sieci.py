#!/usr/bin/env python
# coding: utf-8

"""
===============================================================================
IP Address to Binary Converter
===============================================================================

This script converts an IPv4 address written in dot-decimal notation
into its binary representation.

Each octet of the IP address is:
- separated using the dot character "."
- converted into an integer
- transformed into binary format
- padded to 8 bits

Example:
-----------------------------------------------------------------------
Input:
    10.10.112.34

Output:
    ['00001010', '00001010', '01110000', '00100010']

This type of conversion is commonly used in:
- networking
- subnetting
- cybersecurity
- routing analysis
- CCNA/CCNP studies
"""


def convert_ip_to_binary(ip_address):
    """
    Converts an IPv4 address into binary representation.

    Parameters
    -------------------------------------------------------------------
    ip_address : str
        IPv4 address written in dot-decimal notation.

        Example:
            "192.168.1.1"

    Returns
    -------------------------------------------------------------------
    list
        List containing binary strings for each octet.

        Example:
            [
                '11000000',
                '10101000',
                '00000001',
                '00000001'
            ]
    """

    # Create empty list for binary octets
    binary_list = []

    # Split IP address into separate octets
    for octet in ip_address.split("."):

        # Convert octet to integer
        # Convert integer to binary
        # Pad binary string to 8 bits
        binary_octet = str(
            format(int(octet), "b")
        ).rjust(8, "0")

        # Store binary octet in result list
        binary_list.append(binary_octet)

    # Return final binary representation
    return binary_list


#==============================================================================
# Example Usage
#==============================================================================

# Input IPv4 address
example_ip = "10.10.112.34"

# Convert IP address to binary
binary_result = convert_ip_to_binary(example_ip)

# Display result
print(binary_result)


#==============================================================================
# Expected Output
#==============================================================================

# [
#     '00001010',
#     '00001010',
#     '01110000',
#     '00100010'
# ]


#==============================================================================
# Commentary
#==============================================================================

"""
ip_address.split(".")
-----------------------------------------------------------------------
Splits the IPv4 address into four separate octets.

Example:
-----------------------------------------------------------------------
"192.168.1.1"

becomes:

[
    "192",
    "168",
    "1",
    "1"
]


format(int(octet), "b")
-----------------------------------------------------------------------
Converts:
1. string octet -> integer
2. integer -> binary representation

Example:
-----------------------------------------------------------------------
10 -> '1010'


rjust(8, "0")
-----------------------------------------------------------------------
Pads the binary string with leading zeros
to ensure every octet contains exactly 8 bits.

Example:
-----------------------------------------------------------------------
'1010'

becomes:

'00001010'


Why 8 Bits?
-----------------------------------------------------------------------
IPv4 addresses consist of:
- 4 octets
- each octet contains 8 bits

Total:
-----------------------------------------------------------------------
32 bits


Practical Use Cases
-----------------------------------------------------------------------
- Network engineering
- Subnet calculations
- Firewall configuration
- Routing analysis
- Cybersecurity training
- Packet inspection
- CCNA/Networking education


Example Conversion
-----------------------------------------------------------------------
Decimal IP:
    10.10.112.34

Binary Representation:
    00001010.00001010.01110000.00100010
"""


# In[2]:


def get_ip_class_info(ip_address):
    """
    Determines the class information of an IP address.

    Parameters:
    - ip_address (str): The input IP address in dot-decimal, binary, or hex notation.

    Returns:
    - tuple: A tuple containing the IP class, subnet mask length, and default subnet mask.
    """
    # Convert the input IP address to dot-decimal notation
    if any(c.isalpha() for c in ip_address):
        # If it contains letters, assume hex
        ip_address = '.'.join(str(int(octet, 16)) for octet in ip_address.split('.'))
    elif ip_address.count('.') == 3 and len(ip_address.split('.')[0]) == 8:
        # If it has 8 characters until the first dot, assume binary
        ip_address = '.'.join(str(int(octet, 2)) for octet in ip_address.split('.'))

    first_octet = int(ip_address.split(".")[0])
    if first_octet in range(0, 128):
        return "A", 8, "255.0.0.0"
    elif first_octet in range(128, 192):
        return "B", 16, "255.255.0.0"
    elif first_octet in range(192, 224):
        return "C", 24, "255.255.255.0"
    elif first_octet in range(224, 240):
        return "D", None, None
    elif first_octet in range(240, 256):
        return "E", None, None
    else:
        raise ValueError(f"{ip_address} isn't a valid IP address!")

# Example use:
# [in]:  get_ip_class_info("192.168.1.1")
# [out]: ('C', 24, '255.255.255.0')

# [in]:  get_ip_class_info("11000000.10101000.00000001.00000001")
# [out]: ('C', 24, '255.255.255.0')

# [in]:  get_ip_class_info("C0.A8.01.01")
# [out]: ('C', 24, '255.255.255.0')


# In[3]:


def convert_ip_format(ip_address, output_format = 'b'):
    """
    Converts an IP address between different formats (binary, hex, decimal).

    Parameters:
    - ip_address (str): The input IP address.
    - output_format (str, optional): The desired output format ('b' for binary, 'h' for hex, 'd' for decimal).
                                    Default is 'b'.

    Returns:
    - str: The converted IP address in the specified format.
    """
    if any(c.isalpha() for c in ip_address):
        input_format = 'h'  # If it contains letters, assume hex
    elif ip_address.count('.') == 3 and len(ip_address.split('.')[0]) == 8:
        input_format = 'b'  # If it has 8 characters until the first dot, assume binary
    else:
        input_format = 'd'  # Otherwise, assume decimal

    # If input and output formats are the same, return the input
    if input_format == output_format:
        # print(f"Input format is the same as output format ('{output_format}'). Returning the input as is.")
        return ip_address

    # Convert input IP address to binary
    if input_format == 'b':
        binary_list = ip_address.split('.')
    elif input_format == 'h':
        hex_octets = ip_address.split('.')
        binary_list = [format(int(hex_octet, 16), '08b') for hex_octet in hex_octets]
    else:
        binary_list = [format(int(octet), '08b') for octet in ip_address.split('.')]

    # Convert binary to the desired output format
    if output_format == 'd':
        return '.'.join(str(int(binary, 2)) for binary in binary_list)
    elif output_format == 'h':
        return '.'.join(hex(int(binary, 2))[2:].upper() for binary in binary_list)
    else:
        return '.'.join(binary_list)

# Example use:
# [in]:  convert_ip_format("192.168.241.14", output_format = 'b')
# [out]: '192.168.241.14'
# [print]: Input format is the same as output format ('b'). Returning the input as is.


# In[4]:


def compare_ip_addresses(ip1, ip2, mask1 = None, mask2 = None):
    """
    Compares two IP addresses based on subnetting information.

    Parameters:
    - ip1 (str): The first IP address in dot-decimal, binary, or hex notation.
    - ip2 (str): The second IP address in dot-decimal, binary, or hex notation.
    - mask1 (str, optional): The subnet mask for the first IP address.
    - mask2 (str, optional): The subnet mask for the second IP address.

    Returns:
    - bool: True if the two IPs belong to different subnets, False otherwise.
    """
    # Convert IP addresses to dot-decimal notation
    ip1_decimal = convert_ip_format(ip1, output_format = 'd')
    ip2_decimal = convert_ip_format(ip2, output_format = 'd')

    binary_ip = convert_ip_to_binary(ip1_decimal), convert_ip_to_binary(ip2_decimal)
    if mask1 is None or mask2 is None:
        binary_mask = convert_ip_to_binary(get_ip_class_info(ip1_decimal)[2]), convert_ip_to_binary(get_ip_class_info(ip2_decimal)[2])
    else:
        binary_mask = convert_ip_to_binary(mask1), convert_ip_to_binary(mask2)

    print(binary_ip[0], binary_ip[1])
    print(binary_mask[0], binary_mask[1])

    result_ip1 = []
    result_ip2 = []
    for a, b, c, d in zip(binary_ip[0], binary_mask[0], binary_ip[1], binary_mask[1]):
        subnet_bits = ""
        host_bits = ""
        for i in range(8):
            subnet_bits += str(int(a[i]) and int(b[i]))
            host_bits += str(int(c[i]) and int(d[i]))
        result_ip1.append(subnet_bits)
        result_ip2.append(host_bits)

    print(result_ip1, result_ip2)
    subnet_bit_count = str(binary_mask[0]).count("1")
    return "".join(result_ip1)[:subnet_bit_count] == "".join(result_ip2)[:subnet_bit_count]

# Example use:
# [in]:  compare_ip_addresses("10.10.112.34", "10.10.119.254")
# [out]: ['00001010', '00001010', '01110000', '00100010'] ['00001010', '00001010', '01110111', '11111110']
#        ['11111111', '00000000', '00000000', '00000000'] ['11111111', '00000000', '00000000', '00000000']
#        ['00001010', '00000000', '00000000', '00000000'] ['00001010', '00000000', '00000000', '00000000']
#        True


# ###### The End

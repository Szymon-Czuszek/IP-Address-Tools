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


#==============================================================================
# IP Address Class Identification
#==============================================================================

"""
This script determines the class of an IPv4 address.

The function supports multiple input formats:
- Dot-decimal notation
- Binary notation
- Hexadecimal notation

The script identifies:
- IP address class
- Default subnet mask length
- Default subnet mask

Supported Classes:
-----------------------------------------------------------------------
Class A -> Large networks
Class B -> Medium networks
Class C -> Small networks
Class D -> Multicast
Class E -> Experimental

Example:
-----------------------------------------------------------------------
Input:
    192.168.1.1

Output:
    ('C', 24, '255.255.255.0')
"""


def get_ip_class_info(ip_address):
    """
    Determines IPv4 address class information.

    Parameters
    -------------------------------------------------------------------
    ip_address : str
        IPv4 address in one of the following formats:
        - Dot-decimal
        - Binary
        - Hexadecimal

        Examples:
            "192.168.1.1"
            "11000000.10101000.00000001.00000001"
            "C0.A8.01.01"

    Returns
    -------------------------------------------------------------------
    tuple
        Contains:
        (
            IP class,
            subnet mask length,
            default subnet mask
        )

        Example:
            ('C', 24, '255.255.255.0')
    """

    #==========================================================================
    # STEP 1: Convert input to dot-decimal notation
    #==========================================================================

    # Detect hexadecimal notation
    if any(c.isalpha() for c in ip_address):

        # Convert hexadecimal octets to decimal
        ip_address = '.'.join(
            str(int(octet, 16))
            for octet in ip_address.split('.')
        )

    # Detect binary notation
    elif (
        ip_address.count('.') == 3
        and len(ip_address.split('.')[0]) == 8
    ):

        # Convert binary octets to decimal
        ip_address = '.'.join(
            str(int(octet, 2))
            for octet in ip_address.split('.')
        )

    #==========================================================================
    # STEP 2: Extract first octet
    #==========================================================================

    first_octet = int(ip_address.split(".")[0])

    #==========================================================================
    # STEP 3: Determine IP address class
    #==========================================================================

    # Class A
    if first_octet in range(0, 128):

        return (
            "A",
            8,
            "255.0.0.0"
        )

    # Class B
    elif first_octet in range(128, 192):

        return (
            "B",
            16,
            "255.255.0.0"
        )

    # Class C
    elif first_octet in range(192, 224):

        return (
            "C",
            24,
            "255.255.255.0"
        )

    # Class D (Multicast)
    elif first_octet in range(224, 240):

        return (
            "D",
            None,
            None
        )

    # Class E (Experimental)
    elif first_octet in range(240, 256):

        return (
            "E",
            None,
            None
        )

    # Invalid IP address
    else:

        raise ValueError(
            f"{ip_address} isn't a valid IP address!"
        )


#==============================================================================
# Example Usage
#==============================================================================

# Example 1: Dot-decimal notation
print(
    get_ip_class_info("192.168.1.1")
)

# Example 2: Binary notation
print(
    get_ip_class_info(
        "11000000.10101000.00000001.00000001"
    )
)

# Example 3: Hexadecimal notation
print(
    get_ip_class_info("C0.A8.01.01")
)


#==============================================================================
# Expected Output
#==============================================================================

# ('C', 24, '255.255.255.0')
# ('C', 24, '255.255.255.0')
# ('C', 24, '255.255.255.0')


#==============================================================================
# Commentary
#==============================================================================

"""
Input Format Detection
-----------------------------------------------------------------------
The function automatically detects whether the input is:
- hexadecimal
- binary
- decimal

This makes the function flexible and reusable.


Hexadecimal Detection
-----------------------------------------------------------------------
any(c.isalpha() for c in ip_address)

Checks whether the address contains alphabetic characters:
- A
- B
- C
- D
- E
- F

If yes:
- assumes hexadecimal notation


Hexadecimal Conversion
-----------------------------------------------------------------------
int(octet, 16)

Converts hexadecimal octets into decimal values.

Example:
-----------------------------------------------------------------------
"C0"

becomes:

192


Binary Detection
-----------------------------------------------------------------------
len(ip_address.split('.')[0]) == 8

Binary octets typically contain exactly 8 bits.

Example:
-----------------------------------------------------------------------
11000000


Binary Conversion
-----------------------------------------------------------------------
int(octet, 2)

Converts binary strings into decimal numbers.

Example:
-----------------------------------------------------------------------
11000000

becomes:

192


IP Address Classes
-----------------------------------------------------------------------

Class A
--------
Range:
    0 - 127

Default Mask:
    255.0.0.0

CIDR:
    /8


Class B
--------
Range:
    128 - 191

Default Mask:
    255.255.0.0

CIDR:
    /16


Class C
--------
Range:
    192 - 223

Default Mask:
    255.255.255.0

CIDR:
    /24


Class D
--------
Range:
    224 - 239

Purpose:
    Multicast


Class E
--------
Range:
    240 - 255

Purpose:
    Experimental / Reserved


ValueError
-----------------------------------------------------------------------
Raises an exception if:
- input format is invalid
- octets are outside valid ranges


Practical Use Cases
-----------------------------------------------------------------------
- Networking education
- Subnetting exercises
- CCNA preparation
- IP classification tools
- Cybersecurity analysis
- Network automation
- Infrastructure validation


Example Conversion Flow
-----------------------------------------------------------------------

Input:
    C0.A8.01.01

Hexadecimal Conversion:
    192.168.1.1

Class Detection:
    Class C

Output:
    ('C', 24, '255.255.255.0')
"""

#==============================================================================
# IP Address Format Converter
#==============================================================================

"""
This script converts IPv4 addresses between multiple formats:

Supported Formats
-----------------------------------------------------------------------
'b' -> Binary
'h' -> Hexadecimal
'd' -> Decimal (dot-decimal notation)

The function automatically detects the input format
and converts it into the desired output format.

Example Conversions
-----------------------------------------------------------------------
Decimal:
    192.168.241.14

Binary:
    11000000.10101000.11110001.00001110

Hexadecimal:
    C0.A8.F1.0E

This type of functionality is commonly used in:
- networking
- cybersecurity
- subnetting
- infrastructure automation
- packet analysis
"""


def convert_ip_format(ip_address, output_format='b'):
    """
    Converts IPv4 addresses between decimal, binary,
    and hexadecimal formats.

    Parameters
    -------------------------------------------------------------------
    ip_address : str
        Input IPv4 address.

    output_format : str, optional
        Desired output format:
        - 'b' -> binary
        - 'h' -> hexadecimal
        - 'd' -> decimal

        Default:
            'b'

    Returns
    -------------------------------------------------------------------
    str
        Converted IPv4 address in requested format.
    """

    #==========================================================================
    # STEP 1: Detect input format
    #==========================================================================

    # Detect hexadecimal notation
    if any(c.isalpha() for c in ip_address):

        input_format = 'h'

    # Detect binary notation
    elif (
        ip_address.count('.') == 3
        and len(ip_address.split('.')[0]) == 8
    ):

        input_format = 'b'

    # Otherwise assume decimal notation
    else:

        input_format = 'd'

    #==========================================================================
    # STEP 2: Check whether conversion is necessary
    #==========================================================================

    if input_format == output_format:

        # Return original value unchanged
        return ip_address

    #==========================================================================
    # STEP 3: Convert input address into binary representation
    #==========================================================================

    # Input already in binary
    if input_format == 'b':

        binary_list = ip_address.split('.')

    # Convert hexadecimal to binary
    elif input_format == 'h':

        hex_octets = ip_address.split('.')

        binary_list = [
            format(int(hex_octet, 16), '08b')
            for hex_octet in hex_octets
        ]

    # Convert decimal to binary
    else:

        binary_list = [
            format(int(octet), '08b')
            for octet in ip_address.split('.')
        ]

    #==========================================================================
    # STEP 4: Convert binary representation into desired output format
    #==========================================================================

    # Convert to decimal
    if output_format == 'd':

        return '.'.join(
            str(int(binary, 2))
            for binary in binary_list
        )

    # Convert to hexadecimal
    elif output_format == 'h':

        return '.'.join(
            hex(int(binary, 2))[2:].upper()
            for binary in binary_list
        )

    # Return binary format
    else:

        return '.'.join(binary_list)


#==============================================================================
# Example Usage
#==============================================================================

# Decimal -> Binary
print(
    convert_ip_format(
        "192.168.241.14",
        output_format='b'
    )
)

# Decimal -> Hexadecimal
print(
    convert_ip_format(
        "192.168.241.14",
        output_format='h'
    )
)

# Binary -> Decimal
print(
    convert_ip_format(
        "11000000.10101000.11110001.00001110",
        output_format='d'
    )
)

# Hexadecimal -> Decimal
print(
    convert_ip_format(
        "C0.A8.F1.0E",
        output_format='d'
    )
)


#==============================================================================
# Expected Output
#==============================================================================

# 11000000.10101000.11110001.00001110
# C0.A8.F1.0E
# 192.168.241.14
# 192.168.241.14


#==============================================================================
# Commentary
#==============================================================================

"""
Automatic Input Detection
-----------------------------------------------------------------------
The function automatically identifies whether the input is:
- binary
- hexadecimal
- decimal

This makes the converter flexible and user-friendly.


Hexadecimal Detection
-----------------------------------------------------------------------
any(c.isalpha() for c in ip_address)

Checks whether the address contains letters:
- A
- B
- C
- D
- E
- F

If yes:
- input is treated as hexadecimal


Binary Detection
-----------------------------------------------------------------------
len(ip_address.split('.')[0]) == 8

Binary octets normally contain exactly 8 bits.

Example:
-----------------------------------------------------------------------
11000000


format(..., '08b')
-----------------------------------------------------------------------
Converts numbers into 8-bit binary strings.

Example:
-----------------------------------------------------------------------
192

becomes:

11000000


int(binary, 2)
-----------------------------------------------------------------------
Converts binary values into decimal numbers.

Example:
-----------------------------------------------------------------------
11000000

becomes:

192


hex(...)[2:].upper()
-----------------------------------------------------------------------
Converts decimal values into hexadecimal notation.

Breakdown:
-----------------------------------------------------------------------
hex(192)      -> '0xc0'
[2:]          -> removes '0x'
upper()       -> converts to uppercase

Final Result:
-----------------------------------------------------------------------
C0


Why Binary Conversion First?
-----------------------------------------------------------------------
The script standardizes all conversions through binary format.

Advantages:
- simplifies conversion logic
- reduces duplicated code
- improves maintainability


Supported Conversion Paths
-----------------------------------------------------------------------

Decimal -> Binary
Decimal -> Hexadecimal

Binary -> Decimal
Binary -> Hexadecimal

Hexadecimal -> Decimal
Hexadecimal -> Binary


Practical Use Cases
-----------------------------------------------------------------------
- Networking education
- CCNA/CCNP training
- Cybersecurity exercises
- Packet analysis
- Infrastructure automation
- IP address validation
- Subnetting calculations


Example Conversion Flow
-----------------------------------------------------------------------

Input:
    192.168.241.14

Step 1:
    Convert decimal -> binary

Result:
    11000000.10101000.11110001.00001110

Step 2:
    Convert binary -> hexadecimal

Result:
    C0.A8.F1.0E
"""

#==============================================================================
# IP Address Format Converter
#==============================================================================

"""
This script converts IPv4 addresses between multiple formats:

Supported Formats
-----------------------------------------------------------------------
'b' -> Binary
'h' -> Hexadecimal
'd' -> Decimal (dot-decimal notation)

The function automatically detects the input format
and converts it into the desired output format.

Example Conversions
-----------------------------------------------------------------------
Decimal:
    192.168.241.14

Binary:
    11000000.10101000.11110001.00001110

Hexadecimal:
    C0.A8.F1.0E

This type of functionality is commonly used in:
- networking
- cybersecurity
- subnetting
- infrastructure automation
- packet analysis
"""


def convert_ip_format(ip_address, output_format='b'):
    """
    Converts IPv4 addresses between decimal, binary,
    and hexadecimal formats.

    Parameters
    -------------------------------------------------------------------
    ip_address : str
        Input IPv4 address.

    output_format : str, optional
        Desired output format:
        - 'b' -> binary
        - 'h' -> hexadecimal
        - 'd' -> decimal

        Default:
            'b'

    Returns
    -------------------------------------------------------------------
    str
        Converted IPv4 address in requested format.
    """

    #==========================================================================
    # STEP 1: Detect input format
    #==========================================================================

    # Detect hexadecimal notation
    if any(c.isalpha() for c in ip_address):

        input_format = 'h'

    # Detect binary notation
    elif (
        ip_address.count('.') == 3
        and len(ip_address.split('.')[0]) == 8
    ):

        input_format = 'b'

    # Otherwise assume decimal notation
    else:

        input_format = 'd'

    #==========================================================================
    # STEP 2: Check whether conversion is necessary
    #==========================================================================

    if input_format == output_format:

        # Return original value unchanged
        return ip_address

    #==========================================================================
    # STEP 3: Convert input address into binary representation
    #==========================================================================

    # Input already in binary
    if input_format == 'b':

        binary_list = ip_address.split('.')

    # Convert hexadecimal to binary
    elif input_format == 'h':

        hex_octets = ip_address.split('.')

        binary_list = [
            format(int(hex_octet, 16), '08b')
            for hex_octet in hex_octets
        ]

    # Convert decimal to binary
    else:

        binary_list = [
            format(int(octet), '08b')
            for octet in ip_address.split('.')
        ]

    #==========================================================================
    # STEP 4: Convert binary representation into desired output format
    #==========================================================================

    # Convert to decimal
    if output_format == 'd':

        return '.'.join(
            str(int(binary, 2))
            for binary in binary_list
        )

    # Convert to hexadecimal
    elif output_format == 'h':

        return '.'.join(
            hex(int(binary, 2))[2:].upper()
            for binary in binary_list
        )

    # Return binary format
    else:

        return '.'.join(binary_list)


#==============================================================================
# Example Usage
#==============================================================================

# Decimal -> Binary
print(
    convert_ip_format(
        "192.168.241.14",
        output_format='b'
    )
)

# Decimal -> Hexadecimal
print(
    convert_ip_format(
        "192.168.241.14",
        output_format='h'
    )
)

# Binary -> Decimal
print(
    convert_ip_format(
        "11000000.10101000.11110001.00001110",
        output_format='d'
    )
)

# Hexadecimal -> Decimal
print(
    convert_ip_format(
        "C0.A8.F1.0E",
        output_format='d'
    )
)


#==============================================================================
# Expected Output
#==============================================================================

# 11000000.10101000.11110001.00001110
# C0.A8.F1.0E
# 192.168.241.14
# 192.168.241.14


#==============================================================================
# Commentary
#==============================================================================

"""
Automatic Input Detection
-----------------------------------------------------------------------
The function automatically identifies whether the input is:
- binary
- hexadecimal
- decimal

This makes the converter flexible and user-friendly.


Hexadecimal Detection
-----------------------------------------------------------------------
any(c.isalpha() for c in ip_address)

Checks whether the address contains letters:
- A
- B
- C
- D
- E
- F

If yes:
- input is treated as hexadecimal


Binary Detection
-----------------------------------------------------------------------
len(ip_address.split('.')[0]) == 8

Binary octets normally contain exactly 8 bits.

Example:
-----------------------------------------------------------------------
11000000


format(..., '08b')
-----------------------------------------------------------------------
Converts numbers into 8-bit binary strings.

Example:
-----------------------------------------------------------------------
192

becomes:

11000000


int(binary, 2)
-----------------------------------------------------------------------
Converts binary values into decimal numbers.

Example:
-----------------------------------------------------------------------
11000000

becomes:

192


hex(...)[2:].upper()
-----------------------------------------------------------------------
Converts decimal values into hexadecimal notation.

Breakdown:
-----------------------------------------------------------------------
hex(192)      -> '0xc0'
[2:]          -> removes '0x'
upper()       -> converts to uppercase

Final Result:
-----------------------------------------------------------------------
C0


Why Binary Conversion First?
-----------------------------------------------------------------------
The script standardizes all conversions through binary format.

Advantages:
- simplifies conversion logic
- reduces duplicated code
- improves maintainability


Supported Conversion Paths
-----------------------------------------------------------------------

Decimal -> Binary
Decimal -> Hexadecimal

Binary -> Decimal
Binary -> Hexadecimal

Hexadecimal -> Decimal
Hexadecimal -> Binary


Practical Use Cases
-----------------------------------------------------------------------
- Networking education
- CCNA/CCNP training
- Cybersecurity exercises
- Packet analysis
- Infrastructure automation
- IP address validation
- Subnetting calculations


Example Conversion Flow
-----------------------------------------------------------------------

Input:
    192.168.241.14

Step 1:
    Convert decimal -> binary

Result:
    11000000.10101000.11110001.00001110

Step 2:
    Convert binary -> hexadecimal

Result:
    C0.A8.F1.0E
"""

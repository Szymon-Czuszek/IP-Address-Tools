#!/usr/bin/env python
# coding: utf-8

# In[1]:


def convert_ip_to_binary(ip_address):
    """
    Converts an IP address to a list of binary strings for each octet.

    Parameters:
    - ip_address (str): The input IP address in dot-decimal notation.

    Returns:
    - list: A list of binary strings representing each octet.
    """
    binary_list = []
    for octet in ip_address.split("."):
        binary_list.append(str(format(int(octet), "b")).rjust(8, "0"))
    return binary_list

# Example use:
# [in]:  convert_ip_to_binary("10.10.112.34")
# [out]: ['00001010', '00001010', '01110000', '00100010']

def get_ip_class_info(ip_address):
    """
    Determines the class information of an IP address.

    Parameters:
    - ip_address (str): The input IP address in dot-decimal notation.

    Returns:
    - tuple: A tuple containing the IP class, subnet mask length, and default subnet mask.
    """
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
# [in]:  get_ip_class_info("10.10.112.34")
# [out]: ('A', 8, '255.0.0.0')

def compare_ip_addresses(ip1, ip2, mask1=None, mask2=None):
    """
    Compares two IP addresses based on subnetting information.

    Parameters:
    - ip1 (str): The first IP address in dot-decimal notation.
    - ip2 (str): The second IP address in dot-decimal notation.
    - mask1 (str, optional): The subnet mask for the first IP address.
    - mask2 (str, optional): The subnet mask for the second IP address.

    Returns:
    - bool: True if the two IPs belong to different subnets, False otherwise.
    """
    binary_ip = convert_ip_to_binary(ip1), convert_ip_to_binary(ip2)
    if mask1 is None or mask2 is None:
        binary_mask = convert_ip_to_binary(get_ip_class_info(ip1)[2]), convert_ip_to_binary(get_ip_class_info(ip2)[2])
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
    return result_ip1 == result_ip2 and "".join(binary_ip[0])[-subnet_bit_count:] != "".join(binary_ip[1])[-subnet_bit_count:]

# Example use:
# [in]:  compare_ip_addresses("10.10.112.34", "10.10.119.254")
# [out]: ['00001010', '00001010', '01110000', '00100010'] ['00001010', '00001010', '01110111', '11111110']
#        ['11111111', '00000000', '00000000', '00000000'] ['11111111', '00000000', '00000000', '00000000']
#        ['00001010', '00000000', '00000000', '00000000'] ['00001010', '00000000', '00000000', '00000000']
#        True
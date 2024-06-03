#!/usr/bin/env python3
import sys

def address_validation(address):
    octets = address.split(".")             ##Make inputted address into a list

    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False
    
    return True

def ip_to_binary(address):
    octets = address.split(".")             ##Make inputted address into a list
    binary_octets = []

    for octet in octets:                    ##For every octet, format the value into binary and append it to an empty list
        binary = format(int(octet), '08b')
        binary_octets.append(binary)

    binary_ip = ''.join(binary_octets)     ##Join each value in the list with a "."
    return binary_ip                

#Takes in address and returns the IP Class
def ip_class(address):
    class_answer = ''
    if address[0] >= 1 and address[0] <= 126:
        class_answer = 'A'
    elif address[0] >= 128 and address[0] <= 191:
        class_answer = 'B'
    elif address[0] >= 192 and address[0] <= 223:
        class_answer = 'C'
    elif address[0] >= 224 and address[0] <= 239:
        class_answer = 'D'
    elif address[0] >= 240 and address[0] <= 255:
        class_answer = 'E'
    return class_answer                     ##Returns in string format

def bit_info(cidr, subnet):
    subnet_formatting = ip_to_binary(subnet)        ##Formats subnet mask in #.#.#.# binary
    bit_count = subnet_formatting.count("1")        ##Counts how many 1's are in the subnet

    borrowing_bits = bit_count - cidr
    return borrowing_bits                           ##Returns in int format

def range_info(address, subnet):
    add_bin = ip_to_binary(address)
    sub_bin = ip_to_binary(subnet)
    
    net_start_bin = ''.join('1' if add_bin[i] == '1' and sub_bin[i] == '1' else '0' for i in range(32))
    net_start_bin_period = '.'.join(net_start_bin[i:i+8] for i in range(0, 32, 8))
   
    net_start_list = []
    for octet in net_start_bin_period.split("."):
        net_start_list.append(str(int(octet, 2)))
    net_start = '.'.join(net_start_list)
    print("Starting network address: ", net_start)

    net_broad_bin = ''.join('1' if sub_bin[i] == '0' else net_start_bin[i] for i in range(32))
    net_broad_bin_period = '.'.join(net_broad_bin[i:i+8] for i in range(0, 32, 8))

    net_end_list = []
    for octet in net_broad_bin_period.split("."):
        net_end_list.append(str(int(octet, 2)))
    net_end = '.'.join(net_end_list)
    print("Broadcast Address: ", net_end)

#-----------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------#
if __name__=="__main__": 
    #Ask user for input
    ##addr = input("Enter I.P. Address: ")
    ##cidr = int(input("Enter CIDR: "))
    ##subnet_mask = input("Enter subnet mask: ")

    while True:
        try: 
            addr = input("Enter I.P. Address: ")
            cidr = int(input("Enter CIDR: "))
            subnet_mask = input("Enter subnet mask: ")
        except ValueError:
            print("Please input a valid response")
            continue

        



    
#-----------------------------------------------------------------------#
    #Make user inputted address into [#, #, #, #] format
    addr_string = addr.split(".")
    addr_list = []                              ##[#, #, #, #] Format
    for ele in addr_string:
        addr_list.append(int(ele))
    
    sub_string = subnet_mask.split(".")
    sub_list = []                               ##[#, #, #, #] Format
    for ele in sub_string:
        sub_list.append(int(ele))
#-----------------------------------------------------------------------#

    print("Your address: ", addr)
    print("IP Class: ", ip_class(addr_list))

    borrowing = bit_info(cidr, subnet_mask)
    new_subnet_count = 2**borrowing
    new_host_count = 2**(32-borrowing-cidr)-2
    print("Borrowing Bits: ", borrowing)
    print("Number of new subnets: ", new_subnet_count)
    print("Number of hosts per subnet: ", new_host_count)

    range_info(addr, subnet_mask)

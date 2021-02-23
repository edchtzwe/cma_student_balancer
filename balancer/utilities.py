# python imports
import sys
import re

def IsEmpty(p_string):
    # at least one non-space character
    if not re.search("\S+", str(p_string)):
        return True
    return False;

def ModelObjToPyDict(p_model_object):
    py_dict = dict()
    model_fields = p_model_object.get_iterable_fields()

    for field in model_fields:
        py_dict[field] = getattr(p_model_object, field)
    return py_dict

def IsNumber(p_value):
    if re.search("\d+\.?\d*", str(p_value)):
        return True
    return False;

def IsInteger(p_value):
    if not IsNumber(p_value):
        # would probably throw a type mismatch error at the caller
        # but that would still be better than letting this pass silently
        return None
    if re.search("\.+", str(p_value)):
        return False
    return True

"""
p_list : the list to be operated on
p_packet_size : number of records per packet
"""
def ReturnQueryPackets(p_list, p_packet_size):
    return_dict = {}
    # no data, return an empty list
    if len(p_list) < 1:
        return return_dict
    # no slice number given, return the original list
    if (int(p_packet_size) <= 1):
        return return_dict

    # number of items / numrecords per page
    num_pages = len(p_list) / int(p_packet_size)
    # if not int, then modulo > 0, then add 1 page for the remainder
    if not IsInteger(num_pages):
        num_pages = int(len(p_list) / int(p_packet_size)) + 1
    offset_1 = 0
    offset_2 = int(p_packet_size)
    for i in range(num_pages):
        curr_list = p_list[offset_1:offset_2]
        if len(curr_list) < 1:
            pass
        return_dict.update({str(i):curr_list})

        # get from the next nth iteration
        offset_1 += int(p_packet_size)
        # and the slice offset has to be double the starting index
        offset_2 = offset_1 * 2
    return return_dict
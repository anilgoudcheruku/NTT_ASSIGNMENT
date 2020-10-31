##########################################################################
# Project         : NTT ASSIGNMENT
# Title           : flaskapp.py
# Description     : This file implements user defined functions which
#                   consumes by api
# Author          : ANIL GOUD CHERUKU
# Date            : 30-Oct-2020
# Version         : 1.0.0
# Python_version  : 3.6.3
##########################################################################


import re
import os
file_path = "ntt_interfaces_source.txt"
current_directory = str(os.path.dirname(__file__))
file_path = str(current_directory + "\\\\{}".format(file_path))


def retrieve_interfaces_from_source():
    try:
        source_content = open(file_path, 'r').read()

        text = source_content.replace('\n', ' ')

        text_length = len(text)
        extracts = []
        i = 0
        # extract the valid pattern
        while i < text_length:
            r = re.search(r'interface(.*?)!', text)
            if r is not None and r.group(1):
                extracts.append(text[r.regs[0][0]:r.regs[0][1]])
                text = text[r.regs[0][1]:]
                text_length = len(text)
            else:
                break
        # Extraction of pattern is done
        results = []
        # Now lets form json values
        for e in extracts:
            d = {
                "interface": '',
                'ip_address': '',
                'subnet': '',
                "description": ''
            }
            # find the interface name
            r = re.search(r'interface(.*?)(description|ip address)', e)
            if r is not None and r.group(1):
                d['interface'] = str(r.group(1)).strip()
            else:
                print("Issue with content, continuing to "
                      "check for remaining data")
                continue
            r = re.search(r'description(.*?)(!|ip address)', e)
            if r is not None and r.group(1):
                d['description'] = str(r.group(1)).strip()
            else:
                print("Issue with content, continuing to "
                      "check for remaining data")
                continue
            r = re.search(r'ip address(.*?)(!|description)', e)
            if r is not None and r.group(1):
                ip_config = r.group(1).strip().split()
                d['ip_address'] = ip_config[0]
                d['subnet'] = ip_config[1]
            else:
                print("Issue with content, continuing to "
                      "check for remaining data")
                continue
            results.append(d)

        return results

    except Exception as ex:
        print("Exception in reading Source file", ex)


def retrieve_interface_by_name(interface):
    try:
        interfaces = retrieve_interfaces_from_source()
        i = [i for i in interfaces if i['interface'] == interface]
        if len(i) > 0:
            return [i[0]]
        return None
    except Exception as e:
        print(f"Exception while retrieving interface details. Exception "
              f"Details: {str(e)}")

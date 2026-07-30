import logging
import xml.etree.ElementTree as ET


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def find_incoming_by_group_number(file_path, group_number):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

    return None


result = find_incoming_by_group_number(
    "work_with_xml/groups.xml",
    2
)

logging.info(f"Incoming value: {result}")
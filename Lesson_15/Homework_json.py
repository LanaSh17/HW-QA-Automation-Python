import json
import logging
import os


logging.basicConfig(
    filename="json__Shanava.log",
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)


folder = os.path.join(os.path.dirname(__file__), "work_with_json")


for file_name in os.listdir(folder):
    if file_name.endswith(".json"):

        file_path = os.path.join(folder, file_name)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                json.load(file)

        except json.JSONDecodeError as error:
            logging.error(
                f"{file_name} is not valid JSON: {error}"
            )
# coding=iso-8859-1

import os
import re
import json
import csv
import codecs

from googletrans import Translator
from pymongo import MongoClient

translator = Translator()


def translate(text):
    return translator.translate(text, src="fr", to="en").text if text else ""


filename_regex = re.compile('[^A-Za-z0-9]+')


SPECIFICATION = "Spécification"


def process_dataset(path):
    with open(os.path.join(path, "info.json")) as f:
        meta = json.load(f)
        resources = meta.get("resources")
        if not resources:
            print(f"no resources for {path}")
            return
        processed_path = os.path.join(os.getcwd(), 'processed', os.path.basename(path))
        os.makedirs(processed_path, exist_ok=True)
        for res in resources:
            table_desc = translate(res.get("title"))
            table_file_name = filename_regex.sub('-', res.get("title"))
            table_path = os.path.join(path, table_file_name + '.csv')
            processed_values = []
            with open(table_path, encoding='iso-8859-1') as table_file:
                table = csv.reader(table_file)
                header_row = next(table)
                if not header_row:
                    header_row = next(table)
                # elif len(header_row) == 1:
                    # processed_values = process_yearly_table_rows(table, header_row)
                if header_row and header_row[0] in ("Année", "Year"):
                    processed_values = process_annual_table_rows(table, header_row)
                if not processed_values:
                    return
                out_map = {
                    "path": table_path,
                    "table_description": table_desc,
                    "values": processed_values
                }
                with codecs.open(os.path.join(processed_path,
                                 f"{table_file_name}-processed.json"), "w", encoding='iso-8859-1') as out_file:
                    json.dump(out_map, out_file, indent=4, sort_keys=True)


def process_yearly_table_rows(table, header_row):
    pass


def process_annual_table_rows(table, header_row):
    values = []
    when_headers = header_row[1:]
    spec_row = next(table)
    if len(spec_row) > 0 and spec_row[0] == SPECIFICATION:
        tags = [translate(x) for x in spec_row if x]
        #tags = [x for x in spec_row if x]
        print(tags)
        for row in table:
            if not row:
                continue
            translated_tags = {tags[i]: translate(row[i]) for i in range(len(tags)) if row[i]}
            # translated_tags = {tags[i]: row[i] for i in range(len(tags))}
            print(translated_tags)
            print(when_headers)
            for i, value in enumerate(row[len(tags):], len(translated_tags)):
                try:
                    int_value = int(value)
                except Exception:
                    continue
                values.append({"value": int_value,
                               "what": ", ".join(translated_tags.values()),
                               "when": when_headers[i - len(tags)]})
    return values


def process_matching_table_rows(table):
    pass


def upload_to_db(value_dict):
    pass


if __name__ == "__main__":
    for dataset in os.listdir("data"):
        dataset_path = os.path.join(os.getcwd(), 'data', dataset)
        process_dataset(dataset_path)


# coding=iso-8859-1

import os
import re
import json
import csv
import codecs
import shutil

from googletrans import Translator
from pymongo import MongoClient

translator = Translator()


def translate(text):
    try:
        return translator.translate(text, src="fr", to="en").text
    except Exception as e:
        print(f"{e} on {text}")
        return text


filename_regex = re.compile('[^A-Za-z0-9]+')
years_double_regex = re.compile("\d\d\d\d/\d\d\d\d - \d\d\d\d/\d\d\d\d")
years_regex = re.compile("\d\d\d\d - \d\d\d\d")


SPECIFICATION = "Spécification"


def process_dataset(path):
    with open(os.path.join(path, "info.json")) as f:
        meta = json.load(f)
        resources = meta.get("resources")
        if not resources:
            print(f"no resources for {path}")
            return
        processed_path = os.path.join(os.getcwd(), 'processed_en_2', os.path.basename(path))
        for res in resources:
            table_desc = translate(res.get("title").strip())
            # table_desc = res.get("title")
            table_desc = years_double_regex.sub('', table_desc)
            table_desc = years_regex.sub('', table_desc)

            table_file_name = filename_regex.sub('-', res.get("title"))
            table_path = os.path.join(path, table_file_name + '.csv')
            if not os.path.isfile(table_path):
                continue
            if os.path.exists(f"{processed_path}/{table_file_name}-processed.json"):
                continue
            processed_values = []
            with open(table_path, encoding='iso-8859-1') as table_file:
                print(f"processing table {table_path}")
                table = csv.reader(table_file)
                header_row = next(table)
                if not header_row:
                    header_row = next(table)
                elif header_row[0].startswith("Année - ") or header_row[0].startswith("Annee - "):
                    try:
                        processed_values = process_yearly_table_rows(table, header_row)
                    except Exception as e:
                        print(e)
                        pass
                if header_row and header_row[0] in ("Année", "Year"):
                    try:
                        processed_values = process_annual_table_rows(table, header_row)
                    except Exception as e:
                        print(e)
                        pass
                if not processed_values:
                    return
                out_map = {
                    "url": meta.get("page"),
                    "path": table_path,
                    "table_description": table_desc,
                    "values": processed_values
                }
                if not os.path.exists(f"processed_en_2/{os.path.basename(path)}"):
                    os.makedirs(f"processed_en_2/{os.path.basename(path)}")
                with codecs.open(os.path.join(processed_path,
                                 f"{table_file_name}-processed.json"), "w", encoding='utf-8') as out_file:
                    json.dump(out_map, out_file, indent=4, sort_keys=True)


def process_yearly_table_rows(table, header_row):
    year = header_row[0].split("-")[1].strip()
    values = []
    spec_row = next(table)
    if not spec_row:
        spec_row = next(table)
    headers = [x for x in spec_row[1:] if x]
    print(headers)
    next(table)  # skip row
    for row in table:
        if not row:
            continue
        what = row[0].strip()
        print(row)
        print(what)
        for i, value in enumerate(row[1:], len(headers)):
            try:
                int_value = int(value)
            except Exception:
                continue
            values.append({"value": int_value,
                           "what": translate(f"{what} {headers[i].strip()}"),
                           "when": year})
    return values


def process_annual_table_rows(table, header_row):
    values = []
    when_headers = header_row[1:]
    spec_row = next(table)
    if len(spec_row) > 0 and spec_row[0] == SPECIFICATION:
        tags = [translate(x.strip()) for x in spec_row if x]
        # tags = [x.strip() for x in spec_row if x]
        print(tags)
        for row in table:
            if not row:
                continue
            translated_tags = {tags[i]: translate(row[i].strip()) for i in range(len(tags)) if row[i]}
            # translated_tags = {tags[i]: row[i].strip() for i in range(len(tags))}
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


def modify_existing(name):
    with open(f"data/{name}/info.json") as f:
        meta = json.load(f)
        resources = meta.get("resources")
        for res in resources:
            table_file_name = filename_regex.sub('-', res.get("title"))
            processed_path = f"processed_en_2/{name}/{table_file_name}-processed.json"
            if os.path.exists(processed_path):
                with open(processed_path) as processed_json:
                    processed = json.load(processed_json)
                    processed["url"] = meta["page"]
                with codecs.open(processed_path, "w", encoding='utf-8') as out_file:
                    json.dump(processed, out_file, indent=4, sort_keys=True)


if __name__ == "__main__":
    # process_dataset("/Users/hyperboreus/PycharmProjects/lquiz-backend/data/relations-economiques-exterieures-balance-des-paiements-investissements-directs-etrangers-methodologie-mbp5-1995-2012")
    # processed_list = os.listdir("processed_en")
    for dataset in os.listdir("data"):
        dataset_path = os.path.join(os.getcwd(), 'data', dataset)
        process_dataset(dataset_path)

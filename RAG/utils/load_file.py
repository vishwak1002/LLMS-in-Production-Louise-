import csv
from .chunking import split_into_chunks

def load_csv(file_path):
    chunks = [] 
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for idx,row in enumerate(reader):
            if idx == 0:
                continue
            chunks.extend(split_into_chunks(row[1]))
    return chunks


def convert_to_pandas_dataframe(file_path):
    import pandas as pd
    df = pd.DataFrame(load_csv(file_path),columns=['chunk'])
    return df
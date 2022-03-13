import pandas as pd
from data_quality.quality_check import ensure_quality
from helpers.helper_functions import transform
import logging
import os


def logger(file_name: str) -> None:
    logging.basicConfig(
        filename=f'logs/{file_name}',
        format="%(asctime)s - %(filename)s - %(message)s",
        level=logging.DEBUG,
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )


def app():
    CWD = os.getcwd()

    # fetch data
    df_1 = pd.read_json(f"{CWD}/source/created_tickets.json")
    df_2 = pd.read_json(f"{CWD}/source/ticket_updates.json")

    # data quality
    df_1 = ensure_quality(df_1, 'created_at')
    df_2 = ensure_quality(df_2, 'updated_at')

    # data transformation
    df_final = transform(df_1, df_2)

    # data load
    df_final.to_csv(os.path.join(f'{CWD}/storage', f'grouped_tickets'), index=False)


if __name__ == '__main__':
    logger('data_quality_log')
    app()

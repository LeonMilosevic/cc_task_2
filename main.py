import pandas as pd
from data_quality.quality_check import ensure_quality
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
    df_1 = pd.read_json(f"{CWD}/source/created_tickets.json", lines=True)
    df_2 = pd.read_json(f"{CWD}/source/ticket_updates.json", lines=True)

    # data quality
    df_1_clean = ensure_quality(df_1, 'created_at')
    df_2_clean = ensure_quality(df_2, 'updated_at')

    # data transformation

    # goal: aggregate 2 json files into 1. contain all ticket comments, latest tags, and latest ticket status.

    # 2nd approach

    # get df_1, df_2
    # df_1, df_2 remove duplicates
    # df_2, get latest occurence of the ticket
    # from tickets that will get dropped keep comments
    # remove tags from created_ticket
    # once we have latest tickets, we merge them to the created_tickets

    # df_2.sort_values('updated_at').groupby(['id', 'brand_id']) \
    #     .agg({'status': 'last',
    #           'tags': 'last',
    #           'url': 'last',
    #           'updated_at': 'last',
    #           'via': 'last',
    #           'comment': list,
    #           'public_comment': 'last'})


if __name__ == '__main__':
    logger('data_quality_log')
    app()

import pandas as pd
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


if __name__ == '__main__':
    logger('data_quality_log')
    app()

from helpers import helper_functions
import pandas as pd
import pytest


def df_for_test():
    return pd.DataFrame({
        "id": [1, 1, 1],
        "brand_id": [2, 2, 2],
        "tags": [['tag_1', 'tag_2'], ['tag_1', 'tag_2'], 'tag_3'],
        "status": ['open', 'open', 'closed'],
        "url": ['url_1', 'url_2', 'url_3'],
        "comment": ['comment_1', 'comment_2', 'comment_3'],
        "via": ['1', '2', '3'],
        "updated_at": pd.to_datetime(["2022-03-05T16:00:00", "2022-03-05T17:00:00", "2022-03-10T18:00:00"]),
        "public_comment": ['yes', 'no', 'no']
    })


aggregates = {'status': 'last',
              'tags': 'last',
              'url': 'last',
              'updated_at': 'last',
              'via': 'last',
              'comment': list,
              'public_comment': 'last'}


def test_implode():
    df = pd.DataFrame({
        "id": [1, 1, 1],
        "tags": ['tag_1', 'tag_2', 'tag_3'],
        "brand_id": [2, 2, 2]
    })

    x = helper_functions.implode(df, 'tags')

    assert len(x) == 1


def test_keep_latest_ticket_by_date():
    df = df_for_test()
    x = helper_functions.keep_latest_ticket_by_date(df, aggregates)

    assert x.updated_at.values[0] == pd.to_datetime("2022-03-10T18:00:00")  # testing if latest ticket was kept


def test_keep_latest_ticket_by_date_comments():
    df = df_for_test()
    x = helper_functions.keep_latest_ticket_by_date(df, aggregates)

    assert len(x.comment.values[0]) == 3  # testing if comments are appended in a list from previous tickets


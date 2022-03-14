import pandas as pd


def implode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Reverses explode function.

    Args:
        df (pd.DataFrame)
        column (pd.DataFrame): column on which to reverse explode

    Returns:
        pd.DataFrame: imploded dataframe
    """
    keys = [c for c in df if c != column]
    return df.groupby(keys, as_index=False).agg({column: list})[df.columns]


def difference(df_1: pd.DataFrame, df_2: pd.DataFrame) -> int:
    """Gets the length difference between two dataframes.

    Args:
        df_1 (pd.DataFrame)
        df_2 (pd.DataFrame)

    Returns:
        x (int): Difference between two dataframes as int.
    """
    return len(df_1) - len(df_2)


def keep_latest_ticket_by_date(df: pd.DataFrame, aggregates: dict) -> pd.DataFrame:
    """Keeps the latest ticket for a given day, appends comments together from all the tickets.

    Args:
        df (pd.DataFrame)
        aggregates (dict): dictionary containing column names and functions to apply on each.

    Returns:
        pd.DataFrame: Latest tickets by day with appended list of comments.
    """
    x = df.copy()
    return x.sort_values('updated_at').groupby(['id', 'brand_id']).agg(aggregates).reset_index()


def transform(df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
    """Wrapper function that calls multiple transformation functions.

    Args:
        df_1 (pd.DataFrame)
        df_2 (pd.DataFrame)

    Returns:
        x (pd.DataFrame): Merged and concatenated dataframe with the latest tickets.
    """
    columns_to_keep = ['id', 'created_at', 'email', 'subject']
    aggregates = {'status': 'last',
                  'tags': 'last',
                  'url': 'last',
                  'updated_at': 'last',
                  'via': 'last',
                  'comment': list,
                  'public_comment': 'last'}
    x_1 = df_1.copy()
    x_2 = df_2.copy()

    x_2 = keep_latest_ticket_by_date(x_2, aggregates)

    return pd.merge(x_1[columns_to_keep], x_2, how="left", on="id")

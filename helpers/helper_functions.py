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
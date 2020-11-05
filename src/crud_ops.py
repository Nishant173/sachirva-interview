import pandas as pd
import utils

def get_all_records():
    df = utils.read_dataframe()
    return df.to_dict(orient='records')

def get_record(id_):
    """
    Gets one record (dictionary) based on it's ID.
    If the ID given doesn't exist, returns empty dictionary.
    """
    df = utils.read_dataframe()
    df_record = df[df['ID'] == id_]
    if df_record.empty:
        return {}
    if len(df_record) == 1:
        dict_record = df_record.iloc[0].to_dict()
        dict_record['Age'] = int(dict_record['Age'])
        return dict_record
    raise Exception("Multiple records with same ID exists")

def add_record(name, age, fav_sport):
    """Adds one record to the database (CSV file)"""
    df = utils.read_dataframe()
    df_record_to_add = pd.DataFrame(data={
        "ID": utils.generate_random_id(),
        "Name": name,
        "Age": age,
        "FavouriteSport": fav_sport
    }, index=[0])
    df_concatenated = pd.concat(objs=[df, df_record_to_add], ignore_index=True, sort=False)
    utils.save_dataframe(data=df_concatenated)
    return None

def delete_record(id_):
    """
    Deletes one record based on it's ID.
    If the ID given doesn't exist, nothing will be deleted.
    """
    df = utils.read_dataframe()
    df_altered = df[df['ID'] != id_]
    utils.save_dataframe(data=df_altered)
    return None

def update_record(id_, name=None, age=None, fav_sport=None):
    """
    Updates one record based on it's ID, and some specified parameters.
    If the ID given doesn't exist, nothing will be updated.
    >>> update_record(id_="U0E4CXQSWC4S", name="SomeNewName", age=20, fav_sport="SomeNewFavouriteSport")
    """
    df = utils.read_dataframe()
    df_record_to_update = df[df['ID'] == id_]
    if df_record_to_update.empty:
        return None
    if len(df_record_to_update) == 1:
        if name:
            df.loc[df['ID'] == id_, 'Name'] = name
        if age:
            df.loc[df['ID'] == id_, 'Age'] = age
        if fav_sport:
            df.loc[df['ID'] == id_, 'FavouriteSport'] = fav_sport
        utils.save_dataframe(data=df)
        return None
    raise Exception("Multiple records with same ID exists")
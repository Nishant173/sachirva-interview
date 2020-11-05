import utils

def get_filtered_records(id_=None, name=None, age=None, fav_sport=None, min_age=None, max_age=None):
    """Gets list of records filtered by criteria specified"""
    df = utils.read_dataframe()
    if id_:
        df = df[df['ID'] == id_]
    if name:
        df = df[df['Name'] == name]
    if age:
        df = df[df['Age'] == age]
    if fav_sport:
        df = df[df['FavouriteSport'] == fav_sport]
    if min_age:
        df = df[df['Age'] >= min_age]
    if max_age:
        df = df[df['Age'] <= max_age]
    if df.empty:
        return []
    return df.to_dict(orient='records')
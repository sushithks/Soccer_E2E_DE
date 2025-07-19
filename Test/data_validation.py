
import pandas as pd

data = pd.read_csv('stadium_data.csv')
#print(data.count())


def stadium_count(data):

    stadiums_df = pd.DataFrame(data)

    # Group by country and count
    country_counts = stadiums_df[['country']].value_counts().reset_index(name='stadium_count')

    validate_df = country_counts.sort_values(by=['stadium_count', 'country'], ascending=[False, True])

    print(validate_df)



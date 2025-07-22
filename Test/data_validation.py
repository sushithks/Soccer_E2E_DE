
import pandas as pd

data = pd.read_csv('stadium_data.csv')
#print(data.count())


def stadium_count(data):

    stadiums_df = pd.DataFrame(data)

    # Group by country and count
    country_counts = stadiums_df[['country']].value_counts().reset_index(name='stadium_count')

    validate_df = country_counts.sort_values(by=['stadium_count', 'country'], ascending=[False, True])

    print(validate_df)




def stadium_capacity(data):
    stadiums_df = pd.DataFrame(data)

    stadiums_df['capacity'] = pd.to_numeric(stadiums_df['capacity'], errors='coerce')
    grouped_df = stadiums_df.groupby('region')['capacity'].mean()

    # Reset index to turn the result into a DataFrame
    grouped_df = grouped_df.reset_index()

    grouped_df = grouped_df.rename(columns={'capacity': 'avg_capacity'})
    grouped_df = grouped_df.sort_values(by='avg_capacity', ascending=False)

    # Final result
    print(grouped_df)



def stadium_rank(data) :

    stadiums_df = pd.DataFrame(data)

    stadiums_df['region_rank'] = stadiums_df.groupby('region')['capacity'] \
        .rank(method='min', ascending=False)


    ranked_df = stadiums_df[['rank', 'stadium', 'region', 'region_rank']]
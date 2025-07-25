
import pandas as pd

data = pd.read_csv('stadium_data.csv')
#print(data.count())


def top_stadium(data):
    stadiums_df = pd.DataFrame(data)
    top_5 = stadiums_df.sort_values(by='capacity', ascending=False).head(5)

    top_stadium_df = top_5[['rank', 'stadium', 'capacity']]
    return top_stadium_df

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
    stadiums_df['capacity'] = pd.to_numeric(stadiums_df['capacity'], errors='coerce')

    stadiums_df['region_rank'] = stadiums_df.groupby('region')['capacity'] \
        .rank(method='min', ascending=False)


    ranked_df = stadiums_df[['rank', 'stadium', 'region', 'region_rank']]
    return ranked_df

def stadium_capacity_avg(data):
    stadiums_df = pd.DataFrame(data)
    stadiums_df['capacity'] = pd.to_numeric(stadiums_df['capacity'], errors='coerce')


    # Step 1: Calculate avg_capacity per region
    avg_df = (
        stadiums_df.groupby('region', as_index=False)['capacity']
        .mean()
        .rename(columns={'capacity': 'avg_capacity'})
    )

    # Step 2: Merge original df with the average df
    merged_df = pd.merge(stadiums_df, avg_df, on='region', how='left')

    # Step 3: Filter rows where capacity > avg_capacity
    filtered_df = merged_df[merged_df['capacity'] > merged_df['avg_capacity']]

    capacity_df = filtered_df[['stadium', 'region', 'capacity', 'avg_capacity']].sort_values(by='region')
    return capacity_df

def stadium_regional_capacity(data) :

    stadiums_df = pd.DataFrame(data)
    stadiums_df['capacity'] = pd.to_numeric(stadiums_df['capacity'], errors='coerce')

    # Compute the median capacity per region
    median_df = (
        stadiums_df.groupby('region')['capacity']
        .median()
        .reset_index()
        .rename(columns={'capacity': 'median_capacity'})
    )

    # Merge original DataFrame with median capacities
    merged = pd.merge(stadiums_df, median_df, on='region')

    # Compute absolute difference from median
    merged['abs_diff'] = (merged['capacity'] - merged['median_capacity']).abs()

    # Rank by closeness to median within each region
    merged['median_rank'] = merged.groupby('region')['abs_diff'].rank(method='first')

    # Filter to get only the closest stadium(s) per region
    closest_to_median = merged[merged['median_rank'] == 1]

    result = closest_to_median[['rank', 'stadium', 'region', 'capacity', 'median_rank']]
    return result

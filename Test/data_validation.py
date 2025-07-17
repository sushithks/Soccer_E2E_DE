
import pandas as pd


def validation(**kwargs):

    data = kwargs['ti'].xcom_pull(key='rows', task_ids='transform_wikipedia_data')
    data = json.loads(data)
    stadiums_df = pd.DataFrame(data)

    # Group by country and count
    country_counts = stadiums_df[['country']].value_counts().reset_index(name='stadium_count')

    validate_df = country_counts.sort_values(by=['stadium_count', 'country'], ascending=[False, True])

    print(validate_df)
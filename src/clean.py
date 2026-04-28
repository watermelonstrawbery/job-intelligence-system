def name(x):
    if x and isinstance(x, dict) and 'display_name' in x:
        return x['display_name']
    else:
        return 'Unknown'


def clean_jobs(data_frame):
    cleaned_df = data_frame.copy()

    cleaned_df = cleaned_df.loc[:, ['title', 'company', 'description', 'location']]
    cleaned_df['company'] = cleaned_df['company'].apply(name)
    cleaned_df['location'] = cleaned_df['location'].apply(name)


    cleaned_df['title'] = cleaned_df['title'].apply(lambda x: str.lower(x))
    cleaned_df['company'] = cleaned_df['company'].apply(lambda x: str.lower(x))
    cleaned_df['description'] = cleaned_df['description'].apply(lambda x: str.lower(x))
    cleaned_df['location'] = cleaned_df['location'].apply(lambda x: str.lower(x))

    return cleaned_df
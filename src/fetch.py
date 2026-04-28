import requests
import pandas as pd

def fetch_jobs():
    data = requests.get("http://api.adzuna.com/v1/api/jobs/gb/search?app_id=dae99f52&app_key=af6f3bf30e451d7ad6b320abdfab56d0&what_or=data,it,software,trainee,ai,python&results_per_page=20")

    data_dict = data.json()
    results = data_dict['results']
    df = pd.DataFrame(results)

    return df


#pd.set_option('display.max_columns', None)
#print(json.dumps(results, indent=4, sort_keys=True))

#clean_df = clean_jobs(df)
#print(clean_df)







#create_features(clean_df)
#clean_df = total_score(clean_df)

#print(clean_df)










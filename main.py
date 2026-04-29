from src import fetch, clean, features, scoring
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

#def log(msg):
#    with open(r"C:\Users\saina\PycharmProjects\JobIntelligenceSystem\log.txt", "a") as f:
#        f.write(msg + "\n")

#log("SCRIPT STARTED")
df = fetch.fetch_jobs()
#log("STEP 1: fetch klart")

clean_df = clean.clean_jobs(df)
#log("STEP 2: clean klart")

featured_df = features.create_features(clean_df)
#log("STEP 3: features klart")
#log(f"TYPE: {type(featured_df)}")

scored_df = scoring.total_score(featured_df)
#log("STEP 4: scoring klart")

#log("STEP 5: GET TOP 10")
#log(f"TYPE: {type(scored_df)}")
top_ten = scored_df.head(10)

#print(top_ten)
filename = f"C:\\Users\\saina\\PycharmProjects\\JobIntelligenceSystem\\outputs\\top_ten_{today}.csv"
top_ten.to_csv(filename)
#log("STEP 6: saving csv")

#log("SCRIPT FINISHED")


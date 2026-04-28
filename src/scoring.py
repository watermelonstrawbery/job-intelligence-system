def score_counter(row):
    score = 0
    if row["has_ai"]:
        score += 2

    if row["has_python"]:
        score += 2

    if row["has_data"]:
        score += 1

    return score


def total_score(df):
    new_df = df.copy()

    new_df['score'] = new_df.apply(score_counter, axis=1)
    new_df = new_df.sort_values(by='score', ascending=False)

    return new_df

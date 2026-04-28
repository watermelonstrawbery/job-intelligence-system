def has_ai(row):
    if "ai" in row['title'].split(" ") or "ai" in row['description'].split(" "):
        return 1
    else:
        return 0

def has_python(row):
    if "python" in row['title'].split(" ") or "python" in row['description'].split(" "):
        return 1
    else:
        return 0

def has_data(row):
    if "data" in row['title'].split(" ") or "data" in row['description'].split(" "):
        return 1
    else:
        return 0

def create_features(df):
    df = df.copy()

    df['has_ai'] = df.apply(has_ai, axis=1)
    df['has_python'] = df.apply(has_python, axis=1)
    df['has_data'] = df.apply(has_data, axis=1)
    return df



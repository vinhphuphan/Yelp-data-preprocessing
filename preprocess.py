def preprocess_and_split_data(input_file):
    # Read the CSV data
    df = pd.read_csv(input_file)

    # Extract "reviews.text" and "reviews.rating" columns
    df = df[['text', 'stars']]

    # Drop rows with missing values
    df.dropna(subset=['text', 'stars'], inplace=True)

    # Rename the columns to match the desired format
    df.rename(columns={'text': 'sentence', 'stars': 'label'}, inplace=True)

    # Convert ratings to binary labels
    df['label'] = df['label'].apply(lambda x: 1 if x >= 4 else 0)

    # Split the data into training, validation, and test sets
    train_df, val_df, test_df = np.split(df.sample(frac=1, random_state=42), [int(.7*len(df)), int(.8*len(df))])

    # Save the datasets to CSV files
    train_df.to_csv("yelp_train.csv", index=False, columns=['label', 'sentence'], header=['label', 'sentence'])
    val_df.to_csv("yelp_val.csv", index=False, columns=['label', 'sentence'], header=['label', 'sentence'])
    test_df.to_csv("yelp_test.csv", index=False, columns=['label', 'sentence'], header=['label', 'sentence'])

# Example usage:
input_file = "yelp.csv"  # Replace with the actual CSV file path
preprocess_and_split_data(input_file)
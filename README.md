## Yelp Review Full Star Dataset

### ORIGIN

The Yelp reviews dataset consists of reviews from Yelp. It is extracted from the Yelp Dataset Challenge 2015 data. For more information, please refer to http://www.yelp.com/dataset_challenge

### DESCRIPTION

The Yelp reviews full star dataset is constructed by randomly taking 130,000 training samples and 10,000 testing samples for each review star from 1 to 5. In total there are 650,000 trainig samples and 50,000 testing samples.

The files yelp.csv contain all the training samples as comma-sparated values. There are 2 columns in them, corresponding to class index (1 to 5) and review text. The review texts are escaped using double quotes ("), and any internal double quote is escaped by 2 double quotes (""). New lines are escaped by a backslash followed with an "n" character, that is "\n".

### PREPROCESSING

This preprocessing involved reading the original CSV data, extracting and renaming columns, converting star ratings into binary labels (1 for positive and 0 for negative), and splitting the data into training, validation, and test sets. The resulting datasets were saved as 'yelp_train.csv', 'yelp_val.csv', and 'yelp_test.csv', making them suitable for natural language processing and sentiment analysis tasks.

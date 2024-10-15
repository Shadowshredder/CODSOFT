import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split

def collaborative_filtering(item_type='movie'):
    # Sample ratings dataset
    if item_type == 'movie':
        ratings_dict = {
            'itemID': [1, 1, 2, 2],
            'userID': ['A', 'B', 'A', 'B'],
            'rating': [5, 4, 4, 5]
        }
    elif item_type == 'book':
        ratings_dict = {
            'itemID': [3, 3, 4, 4],
            'userID': ['X', 'Y', 'X', 'Y'],
            'rating': [5, 4, 4, 5]
        }
    else:
        ratings_dict = {
            'itemID': [5, 5, 6, 6],
            'userID': ['M', 'N', 'M', 'N'],
            'rating': [5, 4, 4, 5]
        }

    ratings = pd.DataFrame(ratings_dict)
    
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings[['userID', 'itemID', 'rating']], reader)
    
    trainset, testset = train_test_split(data, test_size=0.25)
    
    algo = KNNBasic()
    algo.fit(trainset)
    
    predictions = algo.test(testset)
    
    for uid, iid, true_r, est, _ in predictions:
        print(f'User {uid} - Item {iid}: True Rating = {true_r}, Predicted = {est}')

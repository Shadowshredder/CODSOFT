import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def content_based_filtering(item_type='movie'):
    # Load the dataset
    items = pd.read_csv('data/items.csv')
    
    descriptions = {
        'movie': ['Animation, Adventure, Comedy', 'Adventure, Family, Fantasy'],
        'book': ['Fantasy, Adventure', 'Fantasy, Magic, Adventure'],
        'product': ['Smartphone, Technology', 'Smartphone, Android, Technology']
    }
    
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(descriptions[item_type])
    
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    item_index = 0
    sim_scores = list(enumerate(cosine_sim[item_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    print(f"Top 3 recommendations for '{items[items['type'] == item_type].iloc[item_index]['title']}':")
    for i, score in sim_scores[1:4]:
        print(f"{items[items['type'] == item_type].iloc[i]['title']} - Similarity: {score}")

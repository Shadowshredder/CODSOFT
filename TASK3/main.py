from src.collaborative_filtering import collaborative_filtering
from src.content_based_filtering import content_based_filtering

if __name__ == '__main__':
    print("Collaborative Filtering:")
    collaborative_filtering('movie')  # Run for movies
    collaborative_filtering('book')   # Run for books
    collaborative_filtering('product')  # Run for products
    
    print("\nContent-Based Filtering:")
    content_based_filtering('movie')  # Run for movies
    content_based_filtering('book')   # Run for books
    content_based_filtering('product')  # Run for products

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


class SimilarityEngine:
    def __init__(self, books, queries, batch_size=100):
        self.vectorizer = TfidfVectorizer(
            analyzer='char',
            ngram_range=(2, 4),
            min_df=1,
            max_df=0.9,
            max_features=2000
        )
        self.books_vectors = self.vectorizer.fit_transform(books)
        self.queries = queries
        self.batch_size = batch_size

        self.nn = NearestNeighbors(n_neighbors=3, metric='cosine')
        self.nn.fit(self.books_vectors)

    def compute_similarity(self):
        queries_vectors = self.vectorizer.transform(self.queries)
        num_queries = queries_vectors.shape[0]
        results = []

        for start in range(0, num_queries, self.batch_size):
            end = min(start + self.batch_size, num_queries)
            batch_queries = queries_vectors[start:end]
            distances, indices = self.nn.kneighbors(batch_queries)
            results.extend(indices.tolist())

        return results


n = int(input())
books = [input().strip() for _ in range(n)]
m = int(input())
queries = [input().strip() for _ in range(m)]

engine = SimilarityEngine(books, queries, batch_size=100)

results = engine.compute_similarity()

for res in results:
    print(len(res))
    print('\n'.join([books[i] for i in res]))

Types:
1. Non-Personalized (youtube trending): Base on popularity
    + new stuff
    - might see stuff you don't want to
    Cold Start: Problem where new users aren't yet personalized
        -How to establish users, promote obscure content?
2. Content-based: Recommendation by features
    - Pigeon-holed into similar choices
    + Promotes more content that you like 
    Similarity Metrics: How to measure the distance between objects based on features.
        Methods:
        1. Euclidean: shortest distance calculation
            - As n approaches infinite, the euclidean distance approaches a constant
        2. Jaccard Index: A not B / A union B (1 or 0, implicit rating)
            - Missing data (sentiment, polarity
        3. Cosine Similarity: dot product (A dot B / ||A|| ||B||)
            + Insensitive to document length
3. Collaborative Filtering (Netflix, Spotify, Amazon): Recommends items based on other user ratings
    Utility Matrix: ratings of different items (user columns, movie columns, etc.)
    * Collaborative filtering seeks to fill out blank spots in the utility matrix
    + Personalized
    - Popularity bias
    - Hardware-intensive
    - Requires data
    Methods:
    1. Memory-Based: Get similarity values, then compute a weighted average for a user
        a. Item-Item Similarity (faster if more users than items)
        b. User-User Similarity (less predictable because people), O^t(m^2 * n)
    2. Model-Based: Singular Vector via matrix factorization
    3. Decomposition (Single Value Decomposition)
        * Separate utlity matrix to user and item matrices
        * Other dimensions are latent features
        * Gradient descent, Alternating Least Squares (parallelizable)
        + Best-in-class
        - Difficult to interpret

Translating words to numbers: 
1. Bag of Words: Get a jumble of words!
    + get summary!
    + get word frequency!
    Token: a discrete unit of measurement for a vector
    - How to compare words (synonyms, etc.)
    - High time complexity
    - No order, loss of meaning
    Sparse Matrix: not like a dense matrix
2. TF-IDF: Term Frequence * Inverse Document Frequency
    TF: # of times a term appears / total # of terms
    ITF: Significance of work, ln(# docs / # docs with term t)
    * Convert document to matrix
    + Promotes significant words
    - Still loss of meaning (no order)

Surprise: for smaller databases
Pyspark: for large databases
Stop Words: "Useless" words (the, and, uh, etc.)

fangfang.lee@flatironschool.com

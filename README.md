

 **🎬 Personalized Movie Recommendation System**
 
This project implements a scalable and efficient Movie Recommendation System using a Two-Tower Embedding (TTE) architecture inspired by Uber’s ML platform. It encodes user preferences and movie metadata into dense vector embeddings, enabling fast and personalized recommendations through Approximate Nearest Neighbor (ANN) search.

Movies have a unique way of resonating with people across different cultures and backgrounds, yet our tastes in films are highly individualistic. Whether we lean towards genres like thrillers, romance, or sci-fi, or we have particular preferences for actors and directors, our movie choices are as diverse as we are. While it's difficult to pinpoint a single movie that appeals universally, data scientists use behavioral analysis to identify patterns in movie preferences across different groups.

Finding the perfect movie to watch can be overwhelming given the sheer volume of options available. To make this process easier, I’ve built a simple yet powerful movie recommendation system using Python's Tkinter library and Pandas. This system allows users to search for movies, view their details, and receive personalized recommendations based on their preferences. Here’s a walkthrough of how we created this interactive movie recommendation tool.

**1. Dataset Preparation

The system relies on a dataset containing information about movies, including titles, genres, release dates, languages, and ratings. This dataset was loaded into a Pandas DataFrame for easy manipulation and querying.

**2. Preprocessing Data

To ensure smooth functioning of the recommendation system, handled missing values and prepared the dataset for user queries. For instance, I replaced NaN values in the genre column with empty strings to avoid errors during filtering.

🚀 Features
Built using a Two-Tower Neural Network: separate towers for users and movies.

Utilizes cosine similarity for matching user and movie embeddings.

Trained with in-batch negatives, logQ correction, and layer sharing to enhance embedding quality and model performance.

Supports evaluation using Recall@k to measure recommendation effectiveness.

Designed for scalability across large user and item datasets.

🧠 Machine Learning Techniques Used
Collaborative Filtering for learning user-item interaction patterns.

Two-Tower Deep Learning Architecture for encoding user and item features independently.

Cosine Similarity for efficient matching of embedding vectors.

In-Batch Negatives Sampling to reduce training cost while improving generalization.

LogQ Correction to adjust popularity bias in training.

Layer Sharing between towers to reduce model size and improve embedding consistency.

Recall@k for model evaluation and ranking effectiveness.

🛠️ Tech Stack & Tools
Python

NumPy, Pandas

Scikit-learn

Deep Learning Framework (e.g., PyTorch or TensorFlow)

ANN libraries (e.g., FAISS or ScaNN for retrieval)

📈 Evaluation Metrics
Recall@k – Evaluates how many relevant movies are retrieved in the top-k results.

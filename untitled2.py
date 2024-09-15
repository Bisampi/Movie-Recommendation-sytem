import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

# Load the movie dataset
file_path = r"C:\Users\B.pallavi\Downloads\top10K-TMDB-movies (1).csv"  # Update this path to the correct location
movies_df = pd.read_csv(file_path)

# Handle NaN values in the 'genre' column
movies_df['genre'] = movies_df['genre'].fillna('')

# Filter data by title or genre
def search_movies():
    search_text = search_var.get().lower()
    genre_selected = genre_var.get()

    global filtered_movies
    filtered_movies = movies_df

    if search_text:
        filtered_movies = filtered_movies[filtered_movies['title'].str.lower().str.contains(search_text)]

    if genre_selected != "All":
        filtered_movies = filtered_movies[filtered_movies['genre'].str.contains(genre_selected)]

    if filtered_movies.empty:
        messagebox.showinfo("No results", "No movies found for your search.")
    else:
        update_movie_list(filtered_movies)

def update_movie_list(filtered_df):
    movie_list.delete(0, tk.END)  # Clear the current list
    for index, row in filtered_df.iterrows():
        movie_list.insert(tk.END, f"{row['title']} ({row['release_date'][:4]})")

def show_movie_details(event):
    selection = movie_list.curselection()
    if selection:
        selected_movie = filtered_movies.iloc[selection[0]]
        details_text.set(f"Title: {selected_movie['title']}\n"
                         f"Genres: {selected_movie['genre']}\n"
                         f"Language: {selected_movie['original_language']}\n"
                         f"Release Date: {selected_movie['release_date']}\n"
                         f"Rating: {selected_movie['vote_average']}/10\n\n"
                         f"Overview:\n{selected_movie['overview']}")
        recommend_movies(selected_movie)

def recommend_movies(selected_movie):
    selected_genres = set(selected_movie['genre'].split(','))

    # Filter movies with similar genres
    def genre_similarity(movie_genres):
        movie_genres_set = set(movie_genres.split(','))
        return len(selected_genres.intersection(movie_genres_set)) > 0

    recommended_df = movies_df[movies_df['genre'].apply(genre_similarity)]
    
    # Sort by vote average or popularity (you can adjust this)
    recommended_df = recommended_df[recommended_df['title'] != selected_movie['title']]  # Exclude the selected movie
    recommended_df = recommended_df.sort_values(by='vote_average', ascending=False).head(5)

    # Update recommendation listbox
    recommendation_list.delete(0, tk.END)
    if recommended_df.empty:
        recommendation_list.insert(tk.END, "No recommendations available.")
    else:
        for index, row in recommended_df.iterrows():
            recommendation_list.insert(tk.END, f"{row['title']} ({row['release_date'][:4]}) - Rating: {row['vote_average']}")

# Tkinter main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Search box
search_var = tk.StringVar()
search_label = tk.Label(root, text="Search by Title:")
search_label.grid(row=0, column=0, padx=10, pady=10)
search_entry = tk.Entry(root, textvariable=search_var, width=30)
search_entry.grid(row=0, column=1, padx=10, pady=10)

# Genre dropdown
genres = ["All"] + sorted(set(g for sublist in movies_df['genre'].str.split(',') for g in sublist if g))
genre_var = tk.StringVar(value="All")
genre_label = tk.Label(root, text="Filter by Genre:")
genre_label.grid(row=1, column=0, padx=10, pady=10)
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, values=genres, state="readonly")
genre_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Search button
search_button = tk.Button(root, text="Search", command=search_movies)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Movie listbox
movie_list = tk.Listbox(root, height=15, width=50)
movie_list.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
movie_list.bind("<<ListboxSelect>>", show_movie_details)

# Movie details
details_text = tk.StringVar()
details_label = tk.Label(root, textvariable=details_text, justify=tk.LEFT, anchor="w", wraplength=400)
details_label.grid(row=2, column=3, rowspan=5, padx=10, pady=10)

# Recommendation label and listbox
recommendation_label = tk.Label(root, text="Recommendations:", font=('Arial', 14, 'bold'))
recommendation_label.grid(row=7, column=0, padx=10, pady=10)

recommendation_list = tk.Listbox(root, height=10, width=50)
recommendation_list.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()

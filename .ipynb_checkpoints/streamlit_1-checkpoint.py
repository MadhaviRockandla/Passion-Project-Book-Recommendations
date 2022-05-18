import streamlit as st
import pandas as pd
from PIL import Image

st.image('/Users/madhavirockandla/Passion-Project-Book-Recommendations/images/banner.jpeg', width=810, use_column_width=True )

dataset = pd.read_csv("BRS-Dataset/Best_Book_21st.csv")

# Not using this Data set as it is very large


# books = pd.read_csv("BRS-Dataset/Books.csv") ## 23.7 MB Dataset size
# users = pd.read_csv("BRS-Dataset/Users.csv") ## 11 MB Dataset size
# ratings = pd.read_csv("BRS-Dataset/Book-Ratings.csv") ## 20.8 MB Dataset size
#
#
# dataset = pd.merge(books, ratings, on='ISBN', how='inner')
# dataset = pd.merge(dataset, users, on='User-ID', how='inner')

st.dataframe(dataset)
st.sidebar.header('Ratings')

with st.sidebar:
    Horror = st.slider('Horror', 1, 10)
    Romance = st.slider('Romance', 1, 10)
    Thriller = st.slider('Thriller', 1, 10)
    Non_Fiction = st.slider('Non_Fiction', 1, 10)


searched_genre = ('List of Books Recommondation based on your Ratings')
books = st.sidebar.selectbox('Genre', ['Horror', 'Romance', 'Thriller', 'Non_Fiction', 'Crime', 'Fantasy'])

# ## Explicit Ratings Dataset
# dataset1 = dataset[dataset['Book-Rating'] != 0]
# dataset1 = dataset1.reset_index(drop = True)
#
# ## Implicit Ratings Dataset
# dataset2 = dataset[dataset['Book-Rating'] == 0]
# dataset2 = dataset2.reset_index(drop = True)





#searched_genre = st.selectbox(' List of Books Recommondation based on your Ratings', ['Horror', 'Romance', 'Thriller', 'Non_Fiction'])
# def popularity_based(dataframe, n):
#     if 1 <= n <= len(dataframe):
#         data = pd.DataFrame(dataframe.groupby('ISBN')['Book-Rating'].count()).sort_values('Book-Rating',
#                                                                                           ascending=False).head(n)
#         result = pd.merge(data, books, on='ISBN', left_index=False)
#         return result
#     return "Invalid number of books entered!!"
#
# def get_books(dataframe, name, n):
#     print("\nBooks by same Author:\n")
#     au = dataframe['Book-Author'].unique()
#
#     data = dataset2[dataset2['Book-Title'] != name]
#
#     if au[0] in list(data['Book-Author'].unique()):
#         k2 = data[data['Book-Author'] == au[0]]
#     k2 = k2.sort_values(by=['Book-Rating'])
#     print(books (k2, n))
#
#     print("\n\nBooks by same Publisher:\n")
#     au = dataframe['Publisher'].unique()
#
#     if au[0] in list(data['Publisher'].unique()):
#         k2 = pd.DataFrame(data[data['Publisher'] == au[0]])
#     k2 = k2.sort_values(by=['Book-Rating'])
#     print(books(k2, n))
#
#     if books in list(dataset1['Book-Title'].unique()):
#         d = dataset2[dataset2['Book-Title'] == books]
#     get_books(books)
#     print("Invalid Book Name!!")

# st.recommender(searched_genre)


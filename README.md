# 🎬 Movie Recommendation System 🎥

This project is a web-based **movie recommendation system** built using Flask. It allows users to:  

✨ **Search for movies** and get recommendations based on similarity.  
🎭 **Browse top-rated movies** from various genres.  
🍿 **Get movie recommendations by genre** tailored to your preferences.  

---

## 🚀 Features

1. 🔍 **Search for Movies**: Enter a movie title to receive similar recommendations.  
2. 🎞️ **Genre Recommendations**: Get top-rated movies from a specific genre.  
3. 🌟 **Top-Rated Movies**: Explore a curated list of the highest-rated movies.  

---

## 📂 Folder Structure

The project has the following structure:  

```
movie-recommendation-system/
│
├── app/
│   ├── templates/
│   │   ├── index.html              # 🏠 Home page template
│   │   ├── recommendations.html    # 🎯 Recommendations page template
│   │   ├── no_recommendations.html # ❌ No recommendations template
│   │
│   ├── static/
│   │   ├── styles.css              # 🎨 CSS for the application
│   │
│   ├── app.py                      # 🐍 Main Python application
│
├── data/
│   ├── movies.csv                  # 📁 Movie dataset
│   ├── ratings.csv                 # 📁 Ratings dataset
│
├── assets/
│   ├── Project_example1.PNG        
│   ├── Project_example2.PNG
│   ├── Project_example3.PNG
│
└── 
```

---

## 🛠️ Installation and Setup

Follow these steps to set up and run the project:  

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-repository/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

Install the required Python libraries using:  

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare the Dataset

Ensure the following files are available in the `data/` folder:  

- 📁 `movies.csv`  
- 📁 `ratings.csv`  

### 5️⃣ Run the Application

Start the Flask server by running:  

```bash
python app/app.py
```

Access the application in your web browser at `http://127.0.0.1:5000`.

---

## 💻 Usage

1. **🏠 Home Page**: Browse top-rated movies or search for recommendations.  
2. **🔍 Search Recommendations**: Enter a movie title to find similar movies.  
3. **🎭 Genre Recommendations**: Enter a genre to find highly-rated movies in that genre.  

---

## 📦 Dependencies

The project uses the following libraries:  

- Flask 🌐  
- pandas 🐼  
- scikit-learn 🤖   

---

## 📸 Screenshots  

1. **Home Page**  
   Displays top-rated movies and forms for searching by title or genre.  

2. **Movie Recommendations Page**  
   Shows recommended movies based on user input.  

3. **Genre Recommendations Page**  
   Shows genre recommended movies based on user input. 

---

## 🙌 Credits  

- **📊 Datasets**: Movies and ratings data are sourced from the [MovieLens dataset](https://grouplens.org/datasets/movielens/).  
- **🛠️ Framework**: Built using [Flask](https://flask.palletsprojects.com/).  

---

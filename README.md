# 🎬 MoodFlix - Mood-Based Movie Recommendation Engine

A smart movie recommendation system that suggests films based on your current mood using **Django**, **SQLite**, **Bootstrap**, and **Machine Learning**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-3.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Machine Learning Model](#machine-learning-model)
- [Contributing](#contributing)
- [License](#license)

## 🎯 About

MoodFlix is an intelligent movie recommendation system that analyzes your mood and suggests movies tailored to how you're feeling. Using machine learning algorithms, it provides personalized recommendations to enhance your viewing experience.

## ✨ Features

- 🎭 **Mood-Based Recommendations** - Get movie suggestions based on your current emotional state
- 🤖 **Machine Learning Powered** - Uses ML algorithms for accurate predictions
- 🎨 **Clean UI** - Bootstrap-powered responsive interface
- 📊 **Movie Database** - SQLite database with extensive movie collection
- 🔍 **Smart Search** - Find movies by mood, genre, or title
- ⚡ **Fast & Lightweight** - Quick response times with efficient database queries

## 🛠️ Tech Stack

- **Backend**: Django 3.x
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Machine Learning**: Jupyter Notebook, Pandas, NumPy, Scikit-learn
- **Python Version**: 3.8+

## 📁 Project Structure

```
MoodFlix/
├── Data/                    # Movie datasets and data files
├── ML/                      # Machine learning models and notebooks
├── Main/                    # Django project settings
├── Moodflix/                # Main Django app
├── templates/
│   └── Moodflix/           # HTML templates
├── manage.py               # Django management script
├── load_movies.py          # Script to load movies into database
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

## 🚀 Installation

Follow these steps to set up MoodFlix on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/krish26/MoodFlix.git
cd MoodFlix
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run Django migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Load Movie Data

Populate the database with movie data:

```bash
python load_movies.py
```

### 6. Create a Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 💻 Usage

1. **Open your browser** and navigate to `http://127.0.0.1:8000/`

2. **Select your mood** from the available options on the homepage

3. **Browse recommendations** - View personalized movie suggestions based on your selected mood

4. **Explore movie details** - Click on any movie to see more information

5. **Admin Panel** (optional) - Access at `http://127.0.0.1:8000/admin/` to manage movies and data

## 🧠 Machine Learning Model

The recommendation engine uses machine learning algorithms trained on movie datasets. The model considers various factors:

- Movie genres
- User mood patterns
- Historical preferences
- Sentiment analysis
- Movie ratings and popularity

The ML notebooks are located in the `ML/` directory for reference and experimentation.

## 🎨 Customization

### Modifying Moods

Edit the mood categories in `Moodflix/models.py` or through the admin panel.

### Adding Movies

Use the admin panel or the `load_movies.py` script to add new movies to the database.

### Styling

Customize the look and feel by editing templates in `templates/Moodflix/` and static files.

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError`
```bash
# Solution: Ensure all dependencies are installed
pip install -r requirements.txt
```

**Issue**: Database errors
```bash
# Solution: Reset migrations and database
python manage.py makemigrations
python manage.py migrate
```

**Issue**: Port already in use
```bash
# Solution: Run on a different port
python manage.py runserver 8080
```

## 📝 Development

### Running Tests

```bash
python manage.py test
```

### Checking Code Style

```bash
# Install flake8 if not already installed
pip install flake8

# Run linter
flake8 .
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**krish26**
- GitHub: [@krish26](https://github.com/krish26)

## 🙏 Acknowledgments

- Django community for excellent documentation
- Movie datasets providers
- All contributors and supporters

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the Django documentation

---

**Note**: This project is for educational purposes. Make sure to check movie licensing and data usage rights when deploying to production.

Happy watching! 🍿🎬
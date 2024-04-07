from src.main import app

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', default=5000)))
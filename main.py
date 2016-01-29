from app import app
from models import City
import views

if __name__ == '__main__':
    City.create_table(True)
    app.run()

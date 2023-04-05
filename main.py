from app import app
import os
from scripts import scheduler

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))


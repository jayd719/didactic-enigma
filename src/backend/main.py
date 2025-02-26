import os
import logging

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)

DATABASE = "/Users/jashan/projects/stockAnalysis/src/backend/database"
DATABASE = DATABASE if os.path.exists(DATABASE) else "this"
logging.warning(f"Database set to. {DATABASE} ")

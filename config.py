from datetime import timedelta

BASE_DIR = "d:/PythonWorkSpace/Neruo-sama/"

class Config:
    raw_dir = BASE_DIR + "data/raw/"
    cleaned_dir = BASE_DIR + "data/cleaned/"

    #screen spam detection parameters
    MIN_REPEAT_COUNT = 3
    MAX_GAP = timedelta(seconds=5)


config = Config()
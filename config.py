from datetime import timedelta

BASE_DIR = "d:/PythonWorkSpace/Neruo-sama/"

class Config:
    output_dir = BASE_DIR + "output/"
    Pending_dir = BASE_DIR + "pending_data/"

    #screen spam detection parameters
    MIN_REPEAT_COUNT = 3
    MAX_GAP = timedelta(seconds=5)


config = Config()
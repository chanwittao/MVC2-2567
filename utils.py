import logging

def setup_logger(log_file):
    """ ตั้งค่า Logger ให้บันทึกข้อความไปที่ไฟล์ """
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
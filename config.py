"""
Конфигурационный файл с переменными окружения
Скопируйте этот файл в .env и заполните реальными значениями
"""

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# API Configuration
STEND_URL_API = os.getenv("STEND_URL_API", "https://your-api-url.com")
STEND_URL_UI = os.getenv("STEND_URL_UI", "https://your-ui-url.com")

# User Credentials
LOGIN = os.getenv("LOGIN", "your-email@example.com")
PASSWORD = os.getenv("PASSWORD", "your-password")

# Browser Configuration
BROWSER_TIMEOUT = int(os.getenv("BROWSER_TIMEOUT", "10"))
MAX_RETRY_ATTEMPTS = int(os.getenv("MAX_RETRY_ATTEMPTS", "3"))

# Проверка обязательных переменных
def validate_config():
    """Проверяет, что все обязательные переменные установлены"""
    required_vars = {
        "STEND_URL_API": STEND_URL_API,
        "STEND_URL_UI": STEND_URL_UI,
        "LOGIN": LOGIN,
        "PASSWORD": PASSWORD
    }
    
    missing_vars = []
    for var_name, var_value in required_vars.items():
        if var_value in ["https://your-api-url.com", "https://your-ui-url.com", 
                        "your-email@example.com", "your-password"]:
            missing_vars.append(var_name)
    
    if missing_vars:
        raise ValueError(f"Missing environment variables: {', '.join(missing_vars)}")
    
    return True

if __name__ == "__main__":
    validate_config()
    print("All environment variables are configured correctly!")

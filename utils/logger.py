import logging
import os

def get_logger():
    """Configura y devuelve una instancia de logger."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger("AutomationLogger")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(os.path.join(log_dir, "execution.log"))
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        # Console Handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
    return logger

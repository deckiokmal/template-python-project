from decouple import config as decouple_config
from dotenv import load_dotenv
from src.config import DevelopmentConfig, TestingConfig, ProductionConfig
import os


# * Load .env file variable
load_dotenv()


def create_app():
    global UUID_TYPE
    configure_logging()  # * setup logging
    app = Flask(__name__)

    # * Membaca konfigurasi dari file .env
    config_name = decouple_config("CONFIG_NAME", default="Production")

    # * Memilih konfigurasi berdasarkan nama
    if config_name == "Development":
        app.config.from_object(DevelopmentConfig)
    elif config_name == "Testing":
        app.config.from_object(TestingConfig)
    elif config_name == "Production":
        app.config.from_object(ProductionConfig)
    else:
        raise ValueError(
            "Invalid CONFIG_NAME. Expected 'Development', 'Testing', or 'Production'."
        )

    # * Register blueprints
    from .controllers.main_controller import main_bp
    app.register_blueprint(main_bp)

    return app

from app.app import create_app
from app.config import DevelopmentConfig, ProductionConfig

application = create_app(ProductionConfig)

if __name__ == '__main__':
    application.run()
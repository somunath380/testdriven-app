class BaseConfig:
    """Base configuration."""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration."""
    pass

class ProductionConfiguration(BaseConfig):
    """Production configuration."""
    pass

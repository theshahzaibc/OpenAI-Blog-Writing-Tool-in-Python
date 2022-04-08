##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

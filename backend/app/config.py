import os

class Config:
    SECRET_KEY = 'nx_vzsn*ng$r&yqth$v5%0n=hare-$8e=$zy*u18qq9x_xz1m2'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/pagueemdia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '1daf6c17085b86a8656d3e38b7851e96afa2b6965a260c13327175f38b28163844bd0187fec90a56bfbd1ef1c488c60231b37b70626ed35df6d69f4e00151e79ed0c742e298930b3a156f604a8bbc8bac1d084a673e005bac2f6fa116bf7719566ca8585b574669205003a9bd97fa1e35c4401f44c557c399d4b87c6e4aa032a1aa46ab6689c6a7b8053b6cd7893948665b014841e48a33e7f9558d238f4b07090d34ed748e02025c013f30e4721e39b9d307c393b163d11a26801ae8ecb5ce347837241fdf62114dd9e00c09e7158203affa7626f7f25692a67ff4eed247e3a0f34c7a475b16746c7b9bd6dbcd7205c1136c790faa0e284c83ef375890a6463'
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
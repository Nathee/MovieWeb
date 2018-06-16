from schema import Schema, And, Use, Optional

rating_schema = Schema([{'rating': And(Use(float), lambda n: 0.0 <= n <= 10.0)}])


def validate_rating(json):
    try:
        validated = rating_schema.validate(json)
        return True
    except:
        return False

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

DEFAULT_IMG = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Cupcake app."""
class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__='cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMG)

    def serialize(self):
        """Returns dict version of self for JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    # def image_url(self):
    #     """Return image or default image"""
    #     return self.image or DEFAULT_IMG
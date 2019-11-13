from .base import BaseModel, db

class User(BaseModel):
  __tablename__ = "users"

  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  middle_name = db.Column(db.String(50), nullable=True)
  profile_pic = db.Column(db.String(1000), nullable=True)
  email_address = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(256), nullable=False)
  sex = db.Column(db.String(6), nullable=False)
  dob = db.Column(db.DateTime())

  def __init__(self, first_name, last_name, middle_name, profile_pic, email_address, password, sex, dob):
    self.first_name = first_name
    self.last_name = last_name
    self.middle_name = middle_name
    self.profile_pic = profile_pic
    self.email_address = email_address
    self.password = password
    self.sex = sex
    self.dob = dob

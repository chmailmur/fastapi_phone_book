from pydantic import BaseModel


class dictionary(BaseModel):
    name: str
    age: int
    phone: str

contact_list = [
    dictionary(name='rustam', age=31, phone='77777'),
    dictionary(name='Alena', age=25, phone='8415151848')
]

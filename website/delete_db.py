from __init__ import db
from models import Note, User

# Xóa toàn bộ dữ liệu từ bảng Note
db.session.query(Note).delete()

# Xóa toàn bộ dữ liệu từ bảng User
db.session.query(User).delete()

# Lưu các thay đổi vào cơ sở dữ liệu
db.session.commit()

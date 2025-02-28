from datetime import datetime

from extensions import db


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    public = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "file_path": self.file_path,
            "uploaded_at": self.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
            "user_id": self.user_id,
            "public": self.public,
        }

    def __repr__(self):
        return f"<File {self.filename}>"

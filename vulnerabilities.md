# Vulnerabilities

**Route `/apps/files/upload`**

- routes/files.py@upload_file
  - Failed to validate file types

**Route `/apps/admin`**

- routes/admin.py@admin
  - Had an SQL injection vulnerability

**Route `/apps/notes/?user_id=<id>`**

- routes/notes.py@notes
  - Allowed any user to view each others notes

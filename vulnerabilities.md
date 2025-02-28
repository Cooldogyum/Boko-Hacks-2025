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

**Route `/apps/notes/search?q=<query>`**

- routes/notes.py@search_notes
  - Had an SQL injection vulnerability

**Route `/apps/notes/delete/<note>`**

- routes/notes.py@delete_note
  - Had an access control vulnerability allowing anyone to delete each others notes

**Route `/apps/notes/debug`**

- routes/notes.py@debug_database
  - Had an information disclosure vulnerability allowing non-admins to view data


**Notes `/apps/notes`**

- Notes had various XSS vulnerabilities
- Notes did not have max lengths enforced

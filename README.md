# BokoHacks-cnl 2025

A submission for Texas State University's 2025 BokoHacks

## Team Members

- Carter Dobbs
- Nate Gay
- Leo Leuzinger

## Overview

As part of the challenge we modified the provided app to resolve any security vulnerabilities and extend features.

## Requirements

- Python 3.8 or higher → [Download Python](https://www.python.org/downloads/)
- [Make](https://www.gnu.org/software/make/)
- Modern web browser (Chrome/Firefox recommended)

## Resources

- SonarQube
- CodeQL
- CI Pipelines
- hCaptcha
- PyAudit

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Nick4453/Boko-Hacks-2025.git
cd boko-hacks-2025
```

2. Open a git bash terminal and run:

```bash
make
```

3. Copy `.env.example` to `.env`

4. Start the application:

```bash
make run
```

6. Open <http://localhost:5000> in your browser

7. Shut Down the Application
To stop the application, press Ctrl + C in the terminal where the application is running. This will terminate the Flask server.

## Improvements Made
See [CHANGES.md](./CHANGES.md)

## Future Improvements

- Add multifactor authentication options
- Resolve any CSRF vulnerabilities
- Clean up code
- Avoid Python

## Learning Resources

If you're new to web application security testing, here are some resources to help you understand the vulnerabilities you might encounter:

1. [OWASP Top 10](https://owasp.org/www-project-top-ten/) - The standard awareness document for web application security
2. [PortSwigger Web Security Academy](https://portswigger.net/web-security) - Free, online web security training
3. [SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
4. [XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
5. [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - A list of useful payloads for bypassing security controls

## Development Notes

- The application uses Flask for the backend
- SQLite databases store application data
- Frontend uses vanilla JavaScript and CSS
- All vulnerabilities are intentional for educational purposes

## Security Notice

This application contains intentional security vulnerabilities for educational purposes. **DO NOT**:

- **Use real credentials or sensitive information while testing**
- Deploy this application on a public network or server
- Use techniques learned here against real websites without explicit permission
**NOTE: IF YOU USE REAL CREDENTIALS, IE: PASSWORDS YOU ACTUALLY USE, WHEN YOU UPLOAD YOUR REPO, THE DATABASE WILL BE PUBLIC. THIS DATABASE CAN BE CONVERTED EASILY ONLINE UNLESS ENCRYPTED**

## License

MIT License - See LICENSE file for details

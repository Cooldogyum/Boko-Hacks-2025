## Fixes
### Company News
- Fixed XSS vulns by sanitizing html input
- Even though UI was broken, any user could access "confidential" internal news via the route. You now need to be an admin to see these articles.
- Removed leaked secret key references in internal news articles
### Notes App
- Fixed an issue where you could see or delete other users notes
- Restricted /notes/debug route to be admin only
- Resolved a SQL injection vulnerability by sanitizing queries when searching notes
- Resolved XSS vulnerabilities by sanitizing html input
- Added max content length enforcement
### Document Upload
- Added file type validation
- Added max file size enforcement
- File permissions so not every file is public
### Admin Portal
- Resolved a SQL injection vulnerability by sanitizing queries
- Fixed XSS vulns by sanitizing html input
### 401(k) Portal
- Used database transaction to resolve a race condition where multiple transactions will be processed and added account balances.
- Account balances are now saved to the database
### Login/Registration
- Prevent bots from making accounts with a non hardcoded captcha via hCaptcha
## General
- Secret key and default admin creds were hardcoded we moved those to and env file that is not committed to the repo
- Developer improvements with UV for managing python env and `make` for quick commands
- PR requirements for merging code: Passing CI, one approving review
- Added biometrics using a needle to process user blood type. Pops out of space bar
- Added pre-commit hooks with vulnerability checking to prevent sec vulns from being committed
- Added CI pipeline to run more advanced vuln checking to prevent sec vulns from being merged to main and deployed
	- py-audit security checks running in pre-commit and on build
	- CodeQL quality analysis helping to identify vulnerabilities
	- SonarQube quality analysis to catch vulnerabilities
- Prevent supply chain attacks by using a lock file for dependencies
### Unfinished but preeetty close
- Almost got CSRF vunls fixed, working on all pages except admin panel

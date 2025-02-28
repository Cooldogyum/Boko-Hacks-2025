# Securing the Breach: Our Hackathon Security Journey

## INTRO [0:00-0:30]
*[Opening shot: Team working together at computers]*

**VOICEOVER:** "When we started this security hackathon, we were given a Flask and JavaScript application riddled with vulnerabilities. Today, we're excited to show you how we transformed it into a secure, robust platform. Let's walk through the critical vulnerabilities we discovered and fixed."

## SECTION 1: AUTHENTICATION & ACCESS CONTROL [0:30-1:15]
*[Screen recording showing login page and admin areas]*

**VOICEOVER:** "First, we tackled fundamental security issues. The application was storing secret keys and admin credentials directly in the code - a major security risk. We moved these to environment variables that aren't committed to the repository.

To prevent unauthorized access, we implemented proper role-based permissions. Previously, any user could access confidential internal news - now only admins can view these articles. We also restricted the notes debug route to admin users only.

For registration security, we integrated hCaptcha to prevent bot account creation, replacing the previous hardcoded captcha solution."

## SECTION 2: CROSS-SITE SCRIPTING (XSS) PROTECTION [1:15-1:45]
*[Demo showing before/after of sanitized inputs]*

**VOICEOVER:** "Cross-site scripting vulnerabilities were pervasive throughout the application. We systematically implemented HTML sanitization across multiple components:
- Company news section
- Notes application
- Admin portal

This prevents attackers from injecting malicious scripts that could steal user data or take control of user sessions."

## SECTION 3: SQL INJECTION PREVENTION [1:45-2:15]
*[Demo showing secure query handling]*

**VOICEOVER:** "SQL injection vulnerabilities in the notes search and admin portal posed serious data exposure risks. We implemented proper query sanitization to ensure user input can't manipulate our database queries. This prevents attackers from extracting sensitive data or executing unauthorized commands on our database."

## SECTION 4: FILE UPLOAD SECURITY [2:15-2:45]
*[Screen recording of secure file upload process]*

**VOICEOVER:** "The document upload system was another critical vulnerability. We implemented:
- File type validation to prevent malicious file uploads
- Maximum file size limits to prevent denial of service attacks
- Proper file permissions to ensure uploaded files aren't publicly accessible by default

These measures prevent attackers from uploading malicious scripts or accessing other users' files."

## SECTION 5: RACE CONDITIONS & TRANSACTIONS [2:45-3:15]
*[Animation showing race condition before/after fix]*

**VOICEOVER:** "In the 401(k) portal, we discovered a dangerous race condition where multiple transactions could process simultaneously, incorrectly adding to account balances. We implemented proper database transactions to ensure financial data integrity, and now account balances are properly saved to the database."

## SECTION 6: DEVELOPER IMPROVEMENTS [3:15-3:45]
*[Screen showing code review process and CI pipeline]*

**VOICEOVER:** "Beyond fixing vulnerabilities, we improved the development process with:
- UV for Python environment management
- Make commands for streamlined development
- Pre-commit hooks with security scanning
- CI pipeline with py-audit, CodeQL, and SonarQube for vulnerability detection
- PR requirements including passing CI and code review
- Dependency lock files to prevent supply chain attacks"

## SECTION 7: ONGOING WORK [3:45-4:00]
*[Screen showing CSRF protection implementation]*

**VOICEOVER:** "We're also nearly finished implementing CSRF protection across all pages, with only the admin panel remaining. This will prevent cross-site request forgery attacks where malicious sites could trick users into performing unwanted actions."

## CONCLUSION [4:00-4:30]
*[Team celebration shot]*

**VOICEOVER:** "Through systematic vulnerability remediation and process improvements, we've transformed this application from a security liability into a hardened platform. We implemented defense in depth with multiple layers of protection against the most common web application attacks. This hackathon has been a tremendous learning experience, and we're proud of the security improvements we've delivered."

*[Final slide with team name/logo]*

**VOICEOVER:** "Thank you for watching our security transformation journey!"

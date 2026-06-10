# GenAI-doc-generator
# GenAI Documentation Generator

## Overview
This project automates software documentation generation using n8n, Google Gemini API, GitHub API, Google Drive, and Gmail.

## Problem Statement
Developers spend significant time creating READMEs, code comments, and architecture documentation manually.

## Solution
An automated workflow that:
1. Receives a GitHub repository through a webhook
2. Extracts repository contents
3. Sends code to Gemini for analysis
4. Generates:
   - README documentation
   - Inline code comments
   - Architecture summaries
5. Stores outputs in Google Drive
6. Sends notification through Gmail

## Tech Stack
- n8n
- Google Gemini API
- GitHub API
- Google Drive API
- Gmail API

## Workflow
(Add workflow screenshots here)

## Key Features
- Automated documentation generation
- No-code workflow
- Cloud storage integration
- Email notifications

## Future Improvements
- Multi-language support
- Documentation versioning
- CI/CD integration

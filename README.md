# pseudonymization-ee

Anonymization for Estonian language.

It can mask the following entities:

- Names
- Organizations
- Dates
- Years
- Locations

Powered by EstNLTK and Spacy's multilingual transformer via Microsoft Presidio.

#Usage

Install needed dependencies and run ./app.py. Anonymizer is available in REST API format at 127.0.0.1:8000/anonymize.

API interface powered by FastAPI.

Python version: 3.7

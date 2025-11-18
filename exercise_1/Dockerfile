# Χρήση Python base image
FROM python:3.11-slim


# Δημιουργία φακέλου εργασίας
WORKDIR /app


# Αντιγραφή αρχείων στο container
COPY src/app.py .


# Ορισμός εντολής εκκίνησης
CMD ["python", "app.py", "10"]
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from application import Application, Document, ApplicationStatus

# Тест 1: Один валидный документ
def test_single_valid_document():
    doc = Document(name="Свидетельство", valid=True)
    app = Application(childname="Иван", documents=[doc])
    status = app.submit()
    assert status == ApplicationStatus.APPROVED

# Тест 2: Один невалидный документ
def test_single_invalid_document():
    doc = Document(name="Свидетельство", valid=False)
    app = Application(childname="Мария", documents=[doc])
    status = app.submit()
    assert status == ApplicationStatus.REJECTED

# Тест 3: Один валидный + один невалидный документ
def test_mixed_documents():
    docs = [
        Document(name="Свидетельство", valid=True),
        Document(name="Паспорт", valid=False)
    ]
    app = Application(childname="Петр", documents=docs)
    status = app.submit()
    assert status == ApplicationStatus.REJECTED

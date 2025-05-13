import pytest
import sys
import os
from unittest.mock import Mock
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from application import Application, Document, ApplicationStatus

@pytest.mark.parametrize(
    "docs, expected_status",
    [
        # Тест 1: Один валидный документ → APPROVED
        ([Document("паспорт", True)], ApplicationStatus.APPROVED),

        # Тест 2: Один невалидный → REJECTED
        ([Document("паспорт", False)], ApplicationStatus.REJECTED),

        # Тест 3: Валидный + невалидный → REJECTED
        ([Document("1", True), Document("2", False)], ApplicationStatus.REJECTED),

        # Тест 4: Все валидные → APPROVED
        ([Document("1", True), Document("2", True)], ApplicationStatus.APPROVED),

        # Тест 5: Пустой список → APPROVED (по текущей логике)
        ([], ApplicationStatus.APPROVED),
    ]
)
def test_application_with_various_inputs(docs, expected_status):
    app = Application(childname="Тестовый", documents=docs)
    result = app.submit()
    assert result == expected_status

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

# 🔹 Тест с mock-документом
def test_mock_document_rejected():
    mock_doc = Mock()
    mock_doc.is_valid.return_value = False

    app = Application(childname="Тестовый", documents=[mock_doc])
    result = app.submit()

    assert result == ApplicationStatus.REJECTED
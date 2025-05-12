from enum import Enum

# Перечисление возможных статусов заявки
class ApplicationStatus(Enum):
    PENDING = "PENDING"       # Ожидает проверки
    APPROVED = "APPROVED"     # Заявка одобрена
    REJECTED = "REJECTED"     # Заявка отклонена

# Класс документа, прикреплённого к заявке
class Document:
    def __init__(self, name, valid=True):
        self.name = name
        self.valid = valid

    def is_valid(self):
        """Проверка валидности документа"""
        return self.valid

# Основной класс заявки
class Application:
    def __init__(self, childname, documents: list):
        self.childname = childname             # Имя ребёнка
        self.documents = documents             # Список документов
        self.status = ApplicationStatus.PENDING  # Изначально заявка в статусе "Ожидание"

    def validate_documents(self):
        """Проверяет, что все документы валидны"""
        return all(doc.is_valid() for doc in self.documents)

    def submit(self):
        """Подача заявки. Устанавливает статус APPROVED или REJECTED"""
        if self.validate_documents():
            self.status = ApplicationStatus.APPROVED
        else:
            self.status = ApplicationStatus.REJECTED
        return self.status


if __name__ == "__main__":
    # Создаём список документов: один валидный
    docs = [Document(name="Свидетельство о рождении", valid=True)]

    # Создаём заявку
    app = Application(childname="Иван Иванов", documents=docs)

    # Подаём заявку
    result = app.submit()

    # Печатаем результат
    print(f"Статус заявки: {result.name}")
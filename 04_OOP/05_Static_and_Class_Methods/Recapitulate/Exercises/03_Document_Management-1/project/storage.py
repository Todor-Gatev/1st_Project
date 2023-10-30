from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        c = self.find_object(self.categories, "id", str(category_id))
        c.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        t = self.find_object(self.topics, "id", str(topic_id))
        t.name = new_topic
        t.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        d = self.find_object(self.documents, "id", str(document_id))
        d.file_name = new_file_name

    def delete_category(self, category_id: int):
        c = self.find_object(self.categories, "id", str(category_id))
        self.categories.remove(c)

    def delete_topic(self, topic_id: int):
        t = self.find_object(self.topics, "id", str(topic_id))
        self.topics.remove(t)

    def delete_document(self, document_id: int):
        d = self.find_object(self.documents, "id", str(document_id))
        self.documents.remove(d)

    def get_document(self, document_id: int):
        return self.find_object(self.documents, "id", str(document_id))

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)

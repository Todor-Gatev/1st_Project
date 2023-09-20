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
    def find_instance_via_id(data: list, instance_id: int):
        for result in data:
            if result.id == instance_id:
                return result

    # @staticmethod
    # def find_object(collection: list, attribute: str, value: int):
    #     for obj in collection:
    #         if getattr(obj, attribute) == value:
    #             return obj

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
        category = self.find_instance_via_id(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_instance_via_id(self.topics, topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc = self.find_instance_via_id(self.documents, document_id)
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.find_instance_via_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_instance_via_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        doc = self.find_instance_via_id(self.documents, document_id)
        self.documents.remove(doc)

    def get_document(self, document_id):
        doc = self.find_instance_via_id(self.documents, document_id)

        return doc

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)

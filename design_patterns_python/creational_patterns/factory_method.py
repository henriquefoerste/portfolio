# Step 1: Define the Product Interface (Document)
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create(self):
        pass

# Step 2: Create Concrete Products (Resume, Report, Letter)
class Resume(Document):
    def create(self):
        print("Creating a Resume")

class Report(Document):
    def create(self):
        print("Creating a Report")

class Letter(Document):
    def create(self):
        print("Creating a Letter")

# Step 3: Create the Factory
class DocumentFactory:
    def create_document(self, doc_type):
        if doc_type == "Resume":
            return Resume()
        elif doc_type == "Report":
            return Report()
        elif doc_type == "Letter":
            return Letter()
        else:
            raise ValueError("Invalid document type")

# Step 4: Test the Factory
if __name__ == "__main__":
    factory = DocumentFactory()

    # Get user input
    doc_type = input("Enter document type (Resume, Report, Letter): ").strip()

    # Create document and call its create method
    try:
        document = factory.create_document(doc_type)
        document.create()
    except ValueError as e:
        print(e)

# Explanation:

#     Product Interface (Document):

#         Defines the interface for all document types. Each document must implement the create() method.

#     Concrete Products (Resume, Report, Letter):

#         Implement the Document interface and provide specific behavior for the create() method.

#     Factory (DocumentFactory):

#         Decides which document type to instantiate based on the input. It encapsulates the object creation logic.

#     Client Code:

#         Uses the factory to create documents without knowing the specific class being instantiated.
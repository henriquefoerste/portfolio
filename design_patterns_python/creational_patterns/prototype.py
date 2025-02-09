import copy

# Step 1: Define the Prototype Interface
class DocumentPrototype:
    def clone(self):
        pass

# Step 2: Create Concrete Prototypes (Resume, Report, Letter)
class Resume(DocumentPrototype):
    def __init__(self, name, skills, experience):
        self.name = name
        self.skills = skills
        self.experience = experience

    def clone(self):
        # Use deepcopy to ensure a true copy of mutable attributes
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Resume: Name={self.name}, Skills={self.skills}, "
                f"Experience={self.experience}")

class Report(DocumentPrototype):
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Report: Title={self.title}, Content={self.content}, "
                f"Author={self.author}")

class Letter(DocumentPrototype):
    def __init__(self, recipient, body, sender):
        self.recipient = recipient
        self.body = body
        self.sender = sender

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Letter: Recipient={self.recipient}, Body={self.body}, "
                f"Sender={self.sender}")

# Step 3: Test the Prototype Pattern
if __name__ == "__main__":
    # Create prototype instances
    resume_prototype = Resume("John Doe", ["Python", "Java"], "5 years")
    report_prototype = Report("Quarterly Report", "Financial data...", "Jane Smith")
    letter_prototype = Letter("Alice", "Hello Alice, ...", "Bob")

    # Clone the prototypes to create new instances
    cloned_resume = resume_prototype.clone()
    cloned_report = report_prototype.clone()
    cloned_letter = letter_prototype.clone()

    # Modify the cloned instances (optional)
    cloned_resume.name = "Jane Doe"
    cloned_report.title = "Annual Report"
    cloned_letter.recipient = "Charlie"

    # Print the original and cloned instances
    print("Original Resume:", resume_prototype)
    print("Cloned Resume:", cloned_resume)
    print("\nOriginal Report:", report_prototype)
    print("Cloned Report:", cloned_report)
    print("\nOriginal Letter:", letter_prototype)
    print("Cloned Letter:", cloned_letter)


    # Explanation:

    # Prototype Interface (DocumentPrototype):

    #     Defines the clone() method that all concrete prototypes must implement.

    # Concrete Prototypes (Resume, Report, Letter):

    #     Implement the clone() method to create a deep copy of the object using copy.deepcopy().

    # Client Code:

    #     Creates prototype instances and clones them to create new objects. The cloned objects can be modified independently of the original.
# Step 1: Define the Handler Interface
class Approver:
    def __init__(self, name, approval_limit):
        self.name = name
        self.approval_limit = approval_limit
        self.next_approver = None  # Reference to the next approver in the chain

    def set_next_approver(self, next_approver):
        self.next_approver = next_approver

    def process_request(self, amount):
        if amount <= self.approval_limit:
            self.approve(amount)  # Approve the request
        elif self.next_approver is not None:
            self.next_approver.process_request(amount)  # Pass to the next approver
        else:
            print(f"Request for ${amount} cannot be approved. No higher authority available.")

    def approve(self, amount):
        print(f"{self.name} approved the request for ${amount}.")

# Step 2: Create Concrete Handlers (Approvers)
class Manager(Approver):
    def __init__(self, name):
        super().__init__(name, approval_limit=1000)  # Manager can approve up to $1000

class Director(Approver):
    def __init__(self, name):
        super().__init__(name, approval_limit=5000)  # Director can approve up to $5000

class CEO(Approver):
    def __init__(self, name):
        super().__init__(name, approval_limit=20000)  # CEO can approve up to $20000

# Step 3: Build the Chain of Responsibility
def build_approval_chain():
    # Create approvers
    manager = Manager("John (Manager)")
    director = Director("Alice (Director)")
    ceo = CEO("Bob (CEO)")

    # Build the chain
    manager.set_next_approver(director)
    director.set_next_approver(ceo)

    # Return the first approver in the chain
    return manager

# Step 4: Test the Chain of Responsibility Pattern
if __name__ == "__main__":
    # Build the approval chain
    approval_chain = build_approval_chain()

    # Process purchase requests
    approval_chain.process_request(800)    # Manager approves
    approval_chain.process_request(3500)   # Director approves
    approval_chain.process_request(10000)  # CEO approves
    approval_chain.process_request(25000)  # Cannot be approved




    # Explanation:

    # Handler Interface (Approver):

    #     Defines the interface for all approvers.

    #     Each approver has a name, an approval_limit, and a reference to the next_approver in the chain.

    #     The process_request method checks if the approver can handle the request based on the amount. If not, it passes the request to the next approver.

    # Concrete Handlers (Manager, Director, CEO):

    #     Implement the approve method to handle the request in their own way.

    #     Each approver has a specific approval limit.

    # Building the Chain:

    #     The build_approval_chain function creates the approvers and links them together to form the chain.

    # Client Code:

    #     Sends purchase requests to the first approver in the chain.

    #     Each approver either approves the request or passes it to the next approver in the chain.
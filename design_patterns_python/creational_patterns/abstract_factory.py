# Step 1: Define Abstract Products (Chair, Sofa, Table)
from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class Table(ABC):
    @abstractmethod
    def place_item(self):
        pass

# Step 2: Create Concrete Products for Modern Style
class ModernChair(Chair):
    def sit_on(self):
        print("Sitting on a Modern Chair")

class ModernSofa(Sofa):
    def lie_on(self):
        print("Lying on a Modern Sofa")

class ModernTable(Table):
    def place_item(self):
        print("Placing an item on a Modern Table")

# Step 3: Create Concrete Products for Victorian Style
class VictorianChair(Chair):
    def sit_on(self):
        print("Sitting on a Victorian Chair")

class VictorianSofa(Sofa):
    def lie_on(self):
        print("Lying on a Victorian Sofa")

class VictorianTable(Table):
    def place_item(self):
        print("Placing an item on a Victorian Table")

# Step 4: Define the Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

# Step 5: Create Concrete Factories for Modern and Victorian Styles
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_table(self) -> Table:
        return ModernTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_table(self) -> Table:
        return VictorianTable()

# Step 6: Test the Abstract Factory Pattern
def create_furniture_set(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    table = factory.create_table()

    chair.sit_on()
    sofa.lie_on()
    table.place_item()

if __name__ == "__main__":
    # Get user input for furniture style
    style = input("Enter furniture style (Modern, Victorian): ").strip()

    # Create the appropriate factory based on user input
    if style == "Modern":
        factory = ModernFurnitureFactory()
    elif style == "Victorian":
        factory = VictorianFurnitureFactory()
    else:
        raise ValueError("Invalid furniture style")

    # Create and use the furniture set
    create_furniture_set(factory)


    # Explanation:

    # Abstract Products (Chair, Sofa, Table):

    #     Define the interface for each type of furniture.

    # Concrete Products (ModernChair, VictorianChair, etc.):

    #     Implement the abstract products for specific styles (e.g., Modern, Victorian).

    # Abstract Factory (FurnitureFactory):

    #     Declares methods for creating each type of furniture.

    # Concrete Factories (ModernFurnitureFactory, VictorianFurnitureFactory):

    #     Implement the abstract factory to produce furniture for a specific style.

    # Client Code (create_furniture_set):

    #     Uses the abstract factory to create a set of related furniture objects without knowing their concrete classes.
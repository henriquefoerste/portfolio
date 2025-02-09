# Step 1: Define the Product (Computer)
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return (f"Computer: CPU={self.cpu}, RAM={self.ram}, "
                f"Storage={self.storage}, GPU={self.gpu}")

# Step 2: Define the Builder Interface
class ComputerBuilder:
    def set_cpu(self, cpu):
        pass

    def set_ram(self, ram):
        pass

    def set_storage(self, storage):
        pass

    def set_gpu(self, gpu):
        pass

    def build(self):
        pass

# Step 3: Implement the Concrete Builder
class ConcreteComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # Return self for method chaining

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer

# Step 4: Define the Director (optional)
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_gaming_computer(self):
        return (self.builder
                .set_cpu("Intel i9")
                .set_ram("32GB")
                .set_storage("1TB SSD")
                .set_gpu("NVIDIA RTX 3080")
                .build())

    def construct_office_computer(self):
        return (self.builder
                .set_cpu("Intel i5")
                .set_ram("16GB")
                .set_storage("512GB SSD")
                .build())

# Step 5: Test the Builder Pattern
if __name__ == "__main__":
    # Create a builder
    builder = ConcreteComputerBuilder()

    # Use the builder directly
    custom_computer = (builder
                       .set_cpu("AMD Ryzen 7")
                       .set_ram("16GB")
                       .set_storage("1TB HDD")
                       .set_gpu("AMD Radeon RX 5700")
                       .build())
    print("Custom Computer:", custom_computer)

    # Use the Director to construct predefined configurations
    director = Director(builder)
    gaming_computer = director.construct_gaming_computer()
    office_computer = director.construct_office_computer()

    print("Gaming Computer:", gaming_computer)
    print("Office Computer:", office_computer)



    # Explanation:

    # Product (Computer):

    #     Represents the complex object to be built. It has attributes like cpu, ram, storage, and gpu.

    # Builder Interface (ComputerBuilder):

    #     Defines the steps required to build the product. Each method sets a component of the Computer.

    # Concrete Builder (ConcreteComputerBuilder):

    #     Implements the builder interface and constructs the Computer object step-by-step. It also provides a build() method to return the final product.

    # Director (Optional):

    #     Encapsulates the construction logic for predefined configurations (e.g., gaming computer, office computer).

    # Client Code:

    #     Uses the builder directly or through the director to create Computer objects.
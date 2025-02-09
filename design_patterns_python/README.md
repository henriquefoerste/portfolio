# Design Patterns in Python

This repository is dedicated to reviewing and implementing design patterns in Python. It aims to provide a comprehensive understanding of various design patterns and how they can be applied to create robust and maintainable software.

## SOLID Principles

The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable. These principles were introduced by Robert C. Martin and are widely accepted in the object-oriented programming community.

### 1. Single Responsibility Principle (SRP)
A class should have only one reason to change, meaning that a class should have only one job or responsibility. This principle helps to keep classes focused and manageable.

### 2. Open/Closed Principle (OCP)
Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that the behavior of a module can be extended without modifying its source code, typically achieved through inheritance or interfaces.

### 3. Liskov Substitution Principle (LSP)
Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. This principle ensures that a subclass can stand in for its superclass without causing errors or unexpected behavior.

### 4. Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use. This principle advocates for creating specific interfaces rather than a single general-purpose interface, promoting a more modular and decoupled design.

### 5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details. Details should depend on abstractions. This principle helps to decouple software components, making them easier to develop, test, and maintain.

## Folder Structure

- `creational_patterns/`: Contains examples of creational design patterns.
- `structural_patterns/`: Contains examples of structural design patterns.
- `behavioral_patterns/`: Contains examples of behavioral design patterns.
- `solid_principles/`: Contains examples and explanations of the SOLID principles.

## Getting Started

To get started with the examples in this repository, clone the repository and navigate to the desired pattern or principle folder. Each folder contains a README file with explanations and code examples.

```bash
git clone https://github.com/henriquefoerste/portfolio.git
cd portolio/design_patterns_python
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
 
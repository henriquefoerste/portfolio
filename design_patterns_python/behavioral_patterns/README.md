# Behavioral Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects. They help in defining how objects interact and communicate with each other. These patterns focus on improving or streamlining the communication between disparate objects in a system.

## Examples of Behavioral Design Patterns

### 1. Strategy Pattern
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows the algorithm to vary independently from clients that use it.

**Example:**
```python
class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

data = [5, 2, 9, 1]
context = Context(ConcreteStrategyA())
print(context.execute_strategy(data))  # Output: [1, 2, 5, 9]

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy(data))  # Output: [9, 5, 2, 1]
```

### 2. Observer Pattern
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**Example:**
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print("Observer notified")

subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()  # Output: Observer notified
```

### 3. Command Pattern
The Command Pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

**Example:**
```python
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

class Light:
    def on(self):
        print("Light is on")

class RemoteControl:
    def __init__(self):
        self._commands = []

    def set_command(self, command: Command):
        self._commands.append(command)

    def press_button(self):
        for command in self._commands:
            command.execute()

light = Light()
light_on_command = LightOnCommand(light)
remote = RemoteControl()
remote.set_command(light_on_command)
remote.press_button()  # Output: Light is on
```

These are just a few examples of behavioral design patterns. Each pattern serves a specific purpose and can be used to solve particular problems in software design.
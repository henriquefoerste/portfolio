# Step 1: Implement the Singleton Class
class ConfigurationManager:
    # Private class variable to hold the single instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Check if an instance already exists
        if cls._instance is None:
            # Create a new instance if it doesn't exist
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            # Initialize the instance (optional)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        # Ensure initialization happens only once
        if not self._initialized:
            self.settings = {}
            self._initialized = True

    def set_setting(self, key, value):
        """Add or update a setting."""
        self.settings[key] = value

    def get_setting(self, key):
        """Retrieve a setting."""
        return self.settings.get(key)

    def __str__(self):
        """Return the current settings as a string."""
        return str(self.settings)

# Step 2: Test the Singleton Pattern
if __name__ == "__main__":
    # Create the first instance of ConfigurationManager
    config_manager1 = ConfigurationManager()

    # Add some settings
    config_manager1.set_setting("theme", "dark")
    config_manager1.set_setting("language", "en")

    # Create a second instance of ConfigurationManager
    config_manager2 = ConfigurationManager()

    # Verify that both instances are the same
    print("Config Manager 1:", config_manager1)
    print("Config Manager 2:", config_manager2)

    # Add a new setting using the second instance
    config_manager2.set_setting("font_size", "14px")

    # Verify that the new setting is reflected in the first instance
    print("Config Manager 1 after update:", config_manager1)

    # Check if both instances are the same object
    print("Are config_manager1 and config_manager2 the same instance?",
          config_manager1 is config_manager2)
    

# Explanation:

#     Singleton Implementation:

#         The __new__ method is overridden to control the creation of the instance. It ensures that only one instance of the class is created.

#         The _instance class variable holds the single instance of the class.

#         The __init__ method ensures that initialization happens only once.

#     Configuration Management:

#         The set_setting method adds or updates a setting.

#         The get_setting method retrieves a setting.

#         The __str__ method provides a string representation of the current settings.

#     Client Code:

#         Creates two instances of ConfigurationManager and verifies that they are the same object.

#         Demonstrates that changes made through one instance are reflected in the other.


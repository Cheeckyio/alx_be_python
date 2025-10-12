class Calculator:
    """A class demonstrating the use of class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to class (cls) or instance (self).
        They behave like regular functions but belong to the class namespace.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods receive the class (cls) as the first parameter.
        They can access and modify class attributes.
        
        Args:
            cls: The class itself (automatically passed)
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Testing the Calculator class
if __name__ == "__main__":
    # Using static method - can call without creating an instance
    result_add = Calculator.add(10, 5)
    print(f"Addition: 10 + 5 = {result_add}")
    
    print()  # Blank line for readability
    
    # Using class method - can call without creating an instance
    result_multiply = Calculator.multiply(10, 5)
    print(f"Multiplication: 10 * 5 = {result_multiply}")
    
    print("\n" + "="*50 + "\n")
    
    # You can also call these methods from an instance
    calc = Calculator()
    
    print("Calling methods from an instance:")
    print(f"Instance - Addition: 7 + 3 = {calc.add(7, 3)}")
    print()
    print(f"Instance - Multiplication: 7 * 3 = {calc.multiply(7, 3)}")
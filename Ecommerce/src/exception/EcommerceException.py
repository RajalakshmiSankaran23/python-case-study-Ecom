class EcommerceException(Exception):
    """Base exception class for the E-commerce application."""
    pass


class CustomerNotFoundException(EcommerceException):
    """Exception raised when a customer is not found."""
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)



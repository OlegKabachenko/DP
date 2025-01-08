__all__ = "Integral"

from sympy import sympify, evalf


class Integral:

    def __init__(self, a, b, e):
        self.a = None
        self.b = None
        self.integrand = None
        self.variables = None

        self.set_integrand(e)
        self.set_limits(a, b)
        self.set_free_symbhola()

    def set_limits(self, a, b):
        a_validated = self.validate_limit(a)
        b_validated = self.validate_limit(b)

        self.a = a_validated
        self.b = b_validated

    @staticmethod
    def validate_limit(limit):
        try:
            s_limit = sympify(limit)
            if s_limit.free_symbols:
                raise ValueError("Limits can't have free variables!")
            return s_limit
        except Exception as e:
            raise Exception(f"Invalid limits! {e}")

    def set_integrand(self, e):
        i_validated = self.validate_integrand(e)
        self.integrand = i_validated

    def set_free_symbhola(self):
        self.variables = self.integrand.free_symbols

    @staticmethod
    def validate_integrand(e):
        try:
            return sympify(e)
        except Exception:
            raise Exception("Invalid integrand(check the parentheses and operators)")

    def calculate_integrand(self, **val):
        i_with_vars = self.integrand.subs(val)
        variable_names = {str(var) for var in self.variables}

        missing_vars = variable_names - set(val.keys())
        if missing_vars:
            raise Exception(f"Missing values for variables: {', '.join([str(var) for var in missing_vars])}")

        extra_vars = set(val.keys()) - variable_names
        if extra_vars:
            raise Exception(f"Unnecessary variables: {', '.join([str(var) for var in extra_vars])}")

        result = round(i_with_vars.evalf(), 6)
        return result

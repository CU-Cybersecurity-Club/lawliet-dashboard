"""
Custom versions of commonly used fields to plug into different forms
"""

from django import forms


class TextInput(forms.TextInput):
    """TextInput widget with custom styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.attrs["class"] = "uk-form-width-medium"


class PasswordInput(forms.PasswordInput):
    """TextInput widget with custom styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.attrs["class"] = "uk-form-width-medium"


class Textarea(forms.Textarea):
    """Textarea widget with custom styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.attrs["class"] = "uk-form-width-medium"
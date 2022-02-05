"""Contains all constants and regex patterns used in the application"""
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9\.]+$")

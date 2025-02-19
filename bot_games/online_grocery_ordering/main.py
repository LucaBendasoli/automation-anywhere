"""This module is the main file that contains the logic for solving the
Online Grocery Ordering Challange from Automation Anywhere - Bot Games. """

import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared', '.env'))

load_dotenv(dotenv_path)

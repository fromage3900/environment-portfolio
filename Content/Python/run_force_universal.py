"""Headless wrapper: rebuild M_Master_Toon_Universal with --force."""
import sys

sys.argv = ["setup_master_universal.py", "--force"]
import setup_master_universal

setup_master_universal.build()

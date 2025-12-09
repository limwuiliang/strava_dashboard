import streamlit as st
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import *
except Exception as e:
    st.error(f"Error loading app: {str(e)}")
    import traceback
    st.error(traceback.format_exc())

#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    
    This function allows NumPy to handle validation and
    raise its own exceptions with original messages.
    """
    # Minimal validation - just enough to ensure basic structure
    # but let NumPy handle the detailed error messages
    
    # Convert to numpy arrays - NumPy will validate types
    try:
        a = np.array(m_a, dtype=object)
        b = np.array(m_b, dtype=object)
    except Exception:
        # If basic array conversion fails, re-raise the exception
        # This handles cases like scalar operands
        raise
    
    # Try matrix multiplication
    # NumPy will raise appropriate errors for:
    # - empty matrices
    # - non-rectangular matrices  
    # - type mismatches
    # - multiplication incompatibility
    try:
        result = np.matmul(a, b)
        return result
    except Exception:
        # Re-raise NumPy's exception with its original message
        raise

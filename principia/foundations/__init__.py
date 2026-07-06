"""
principia.foundations — Pedagogical Foundation Module
=====================================================

This package teaches the mathematical foundations of Principia Psychedelia
through runnable Python code. Each module mirrors a section of Chapter 0.

Modules
-------
sets      : Finite set operations (union, intersection, complement, power set)
figurate  : Figurate number sequences (triangular, square, polygonal)
modular   : Modular arithmetic and finite field basics (Z/pZ)

Usage
-----
    python -m principia.foundations.sets
    python -m principia.foundations.figurate
    python -m principia.foundations.modular
"""

from principia.foundations.sets import FiniteSet
from principia.foundations.figurate import triangular, square, polygonal
from principia.foundations.modular import ModularInt

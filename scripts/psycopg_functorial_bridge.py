#!/usr/bin/env python3
"""
Psycopg3 Functorial Bridge: Category Theory in Practice

This script demonstrates the "psycopg3 parallel" from Principia Psychedelia
Vol I, Chapter 0. It serves as a Rosetta Stone for understanding Category Theory 
Functors using standard data engineering concepts.

To understand Category Theory, you only need to know three things:
1. Objects (The nouns: Sets, Types, or SQL Tables)
2. Morphisms (The verbs/arrows: Functions, Pointers, or SQL Foreign Keys)
3. Functors (The translators: Maps that convert Objects to Objects, and 
   Morphisms to Morphisms, while PRESERVING the exact structural relationship).

Usage: python3 scripts/psycopg_functorial_bridge.py
"""

from dataclasses import dataclass
from typing import Dict, Any, TypeVar, Generic, Optional
import json

# -------------------------------------------------------------------
# CATEGORY 1: PostgreSQL (The Category of Relational Data)
# -------------------------------------------------------------------
# In this category:
# - An OBJECT is a Table (a set of rows).
# - A MORPHISM is a Foreign Key (an arrow pointing from one table to another).

@dataclass
class PostgresParentRow:
    """An Object in the Postgres Category (e.g. the 'parents' table)."""
    id: int
    data: str # JSONB

@dataclass
class PostgresChildRow:
    """An Object in the Postgres Category (e.g. the 'children' table)."""
    id: int
    parent_id: int  # This is the MORPHISM (Foreign Key) pointing to PostgresParentRow!
    numeric_value: float

class PostgresCategory:
    """Simulates a database engine."""
    @staticmethod
    def query_records():
        # Simulated database state
        parent = PostgresParentRow(id=1, data='{"state": "stable"}')
        child = PostgresChildRow(id=229, parent_id=1, numeric_value=1.618)
        return parent, child

# -------------------------------------------------------------------
# CATEGORY 2: Python (The Category of Object-Oriented State)
# -------------------------------------------------------------------
# In this category:
# - An OBJECT is a Class Instance (or a primitive like dict/float).
# - A MORPHISM is a Memory Reference (a variable pointing to another instance).

@dataclass
class PythonParent:
    """An Object in the Python Category."""
    uuid: int
    payload: dict

@dataclass
class PythonChild:
    """An Object in the Python Category."""
    uuid: int
    parent_ref: PythonParent  # This is the MORPHISM (Memory Reference) pointing to PythonParent!
    golden_approximation: float

# -------------------------------------------------------------------
# THE FUNCTOR: Psycopg3
# -------------------------------------------------------------------
# A Functor maps Category 1 to Category 2. 
# It MUST preserve the relationships (the Morphisms).

class PsycopgFunctor:
    """
    The Functor: PostgresCategory -> PythonCategory
    Notice how it translates the objects (Row -> Class) AND the morphism 
    (Foreign Key -> Memory Reference) flawlessly, preserving the structure!
    """
    @staticmethod
    def map_parent(row: PostgresParentRow) -> PythonParent:
        # Maps SQL JSONB to Python dict
        return PythonParent(uuid=row.id, payload=json.loads(row.data))

    @staticmethod
    def map_child(child_row: PostgresChildRow, parent_row: PostgresParentRow) -> PythonChild:
        # First, map the parent object
        py_parent = PsycopgFunctor.map_parent(parent_row)
        
        # Then, map the child object, translating the Foreign Key (parent_id)
        # directly into a Python memory reference (py_parent)
        return PythonChild(
            uuid=child_row.id,
            parent_ref=py_parent, # Structure Preserved! The Functor works.
            golden_approximation=child_row.numeric_value
        )

# -------------------------------------------------------------------
# CATEGORY 3: The Golden Fields (Adelic Ring pAQFT)
# -------------------------------------------------------------------

@dataclass
class AdelicState:
    """An Object in the Golden Field F_p."""
    p: int
    residue: int
    
class LocallyCovariantFunctor:
    """
    The pAQFT Functor: PythonCategory -> AdelicCategory
    Maps floating point approximations into exact discrete moduli.
    """
    @staticmethod
    def lift(obj: PythonChild, prime: int) -> AdelicState:
        # Scale the approximation by 1000 to capture decimals and reduce modulo p
        scaled = int(obj.golden_approximation * 1000)
        return AdelicState(p=prime, residue=scaled % prime)

# -------------------------------------------------------------------
# THE BRIDGE EXECUTION
# -------------------------------------------------------------------

def run_functorial_bridge():
    print("=== The Psycopg3 Functorial Bridge ===")
    
    # 1. Start in Postgres (Category 1)
    pg_parent, pg_child = PostgresCategory.query_records()
    print(f"\n[PostgreSQL Category]")
    print(f"Parent Object: {pg_parent}")
    print(f"Child Object:  {pg_child} (Morphism: parent_id={pg_child.parent_id})")
    
    # 2. Functor to Python (Category 2)
    py_child = PsycopgFunctor.map_child(pg_child, pg_parent)
    print(f"\n[Python Category]")
    print(f"Child Object:  uuid={py_child.uuid}, approx={py_child.golden_approximation}")
    print(f"Morphism Preserved! parent_ref points to -> {py_child.parent_ref}")
    
    # 3. Functor to Adelic Ring (Category 3)
    adelic_229 = LocallyCovariantFunctor.lift(py_child, 229)
    print(f"\n[Adelic Category (F_229)]")
    print(f"State: {adelic_229}")
    
    adelic_181 = LocallyCovariantFunctor.lift(py_child, 181)
    print(f"\n[Adelic Category (F_181)]")
    print(f"State: {adelic_181}")

if __name__ == "__main__":
    run_functorial_bridge()

import tempfile
import pytest
import os
import sys

# Obtener la ruta del directorio padre
directorio_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir el directorio al sys.path
sys.path.append(directorio_padre)

from db_manager import DBManager

@pytest.fixture(scope="module")
def db_file():
    # Use a temporary file for the database
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    yield path
    os.remove(path)

@pytest.fixture
def db(db_file):
    # Create a new DBManager for each test
    return DBManager(db_path=db_file)

def test_insert_and_get_all(db):
    data = {"fecha": "2024-06-01", "monto": 100, "categoria": "Alimentos"}
    row_id = db.insert_json(data)
    all_rows = db.get_all()
    assert len(all_rows) == 1
    assert all_rows[0]["id"] == row_id
    assert all_rows[0]["fecha"] == data["fecha"]
    assert all_rows[0]["monto"] == data["monto"]
    assert all_rows[0]["categoria"] == data["categoria"]

def test_get_by_id(db):
    data = {"fecha": "2024-06-02", "monto": 200, "categoria": "Transporte"}
    row_id = db.insert_json(data)
    row = db.get_by_id(row_id)
    assert row is not None
    assert row["id"] == row_id
    assert row["fecha"] == data["fecha"]
    assert row["monto"] == data["monto"]
    assert row["categoria"] == data["categoria"]

def test_update_by_id(db):
    data = {"fecha": "2024-06-03", "monto": 300, "categoria": "Ocio"}
    row_id = db.insert_json(data)
    updated_data = {"fecha": "2024-06-03", "monto": 350, "categoria": "Ocio"}
    result = db.update_by_id(row_id, updated_data)
    assert result is True
    row = db.get_by_id(row_id)
    assert row["monto"] == 350

def test_update_by_id_nonexistent(db):
    result = db.update_by_id(9999, {"fecha": "2024-06-04", "monto": 400, "categoria": "Otros"})
    assert result is False

def test_delete_by_id(db):
    data = {"fecha": "2024-06-05", "monto": 500, "categoria": "Salud"}
    row_id = db.insert_json(data)
    result = db.delete_by_id(row_id)
    assert result is True
    row = db.get_by_id(row_id)
    assert row is None

def test_delete_by_id_nonexistent(db):
    result = db.delete_by_id(9999)
    assert result is False
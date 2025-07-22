import json
import sqlite3
from typing import Any, Dict, List, Optional

class DBManager:
    def __init__(self, db_path: str = "cashflow.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL
                )
            """)
            conn.commit()

    def insert_json(self, data: Dict[str, Any]) -> int:
        json_data = json.dumps(data)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO transactions (data) VALUES (?)", (json_data,))
            conn.commit()
            return cursor.lastrowid

    def get_all(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, data FROM transactions")
            rows = cursor.fetchall()
            return [{"id": row[0], **json.loads(row[1])} for row in rows]

    def get_by_id(self, transaction_id: int) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, data FROM transactions WHERE id = ?", (transaction_id,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], **json.loads(row[1])}
            return None

    def update_by_id(self, transaction_id: int, data: Dict[str, Any]) -> bool:
        json_data = json.dumps(data)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE transactions SET data = ? WHERE id = ?",
                (json_data, transaction_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_by_id(self, transaction_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
            conn.commit()
            return cursor.rowcount > 0

# Ejemplo de uso:
# db = DBManager()
# id = db.insert_json({"fecha": "2024-06-01", "monto": 100, "categoria": "Alimentos"})
# print(db.get_all())
# print(db.get_by_id(id))
# db.update_by_id(id, {"fecha": "2024-06-01", "monto": 200, "categoria": "Alimentos"})
# db.delete_by_id(id)
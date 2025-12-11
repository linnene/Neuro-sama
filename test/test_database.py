import unittest
import sys
import os
from sqlalchemy import text
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool


# 确保能导入 src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from neuro_sama.core.database import engine
from neuro_sama.models.dialogue import Dialogue

class TestDatabase(unittest.TestCase):
    
    def test_real_db_connection(self):
        """
        测试真实配置的数据库引擎是否能正常连接并执行基本查询。
        这验证了 database.db 文件是否可访问/可创建。
        """
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                self.assertEqual(result.scalar(), 1)
        except Exception as e:
            self.fail(f"Real database connection failed: {e}")

    def test_model_crud_in_memory(self):
        """
        在内存数据库中测试 Dialogue 模型的增删改查。
        这验证了模型定义(Dialogue)与数据库模式是否匹配，且不污染真实数据库。
        """
        # 创建一个独立的内存数据库用于测试模型逻辑
        test_engine = create_engine(
            "sqlite:///:memory:", 
            connect_args={"check_same_thread": False}, 
            poolclass=StaticPool
        )
        SQLModel.metadata.create_all(test_engine)
        
        with Session(test_engine) as session:
            # 1. Create
            dialogue = Dialogue(
                prompt_speaker="Tester",
                prompt_content="Is this working?",
                response_speaker="System",
                response_content="Yes, it is!",
                prompt_meta={"test_id": 1},
                response_meta={"status": "ok"}
            )
            session.add(dialogue)
            session.commit()
            session.refresh(dialogue)
            
            self.assertIsNotNone(dialogue.id)
            
            # 2. Read
            read_dialogue = session.get(Dialogue, dialogue.id)
            self.assertIsNotNone(read_dialogue)
            self.assertEqual(read_dialogue.prompt_content, "Is this working?") # type: ignore
            self.assertEqual(read_dialogue.response_meta, {"status": "ok"}) # type: ignore

if __name__ == '__main__':
    unittest.main()

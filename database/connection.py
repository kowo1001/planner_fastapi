from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, List, Optional
from pydantic import BaseModel,BaseSettings
# from pydantic_settings import BaseSettings # pydantic > 2.0 버전 이상
from models.users import User
from models.events import Event

class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return
# get()은 ID를 인수로 받아 컬렉션에서 일치하는 레코드를 불러옴
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
# get_all()은 인수가 없으며 컬렉션에 있는 모든 레코드를 불러옴
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
# update() 메서드는 하나의 ID와 pydantic 스키마(모델)을 인수로 받음
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        # des_body = model_dump()
        des_body = {k:v for k,v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in
            des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    DATABASE_NAME: Optional[str] = "mydatabase" # 데이터베이스 이름 추가
    SECRET_KEY: Optional[str] = None

    async def init_db():
        test_settings = Settings()
        test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

        await test_settings.initialize_database()

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        # db = client.get_database("mydatabase")
        await init_beanie(database=client[self.DATABASE_NAME],
                          document_models=[Event, User])
    class Config:
        env_file = ".env"

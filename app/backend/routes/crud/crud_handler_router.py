from crud.base import CRUDHandler
from fastapi import APIRouter, Query


class CRUDHandlerRouter(APIRouter):
    def __init__(self, handler: CRUDHandler):
        self.handler = handler
        super().__init__(prefix=f"/crud/{handler.name}", tags=[handler.name])

        @self.get("/")
        async def get_list(start_id: int = Query(0, ge=0), limit: int = Query(100, ge=1)):
            read_objects = self.handler.list(start_id=start_id, limit=limit)
            return read_objects

        @self.get("/{object_id}")
        async def get_object(object_id: int):
            read_object = self.handler.get(object_id)
            return read_object

        @self.post("/")
        async def create_object(created_object: handler.create_schema):
            read_object = self.handler.create(created_object)
            return read_object

        @self.put("/{object_id}")
        async def update_object(updated_object: handler.update_schema, object_id: int):
            read_object = self.handler.update(object_id, updated_object)
            return read_object

        @self.delete("/{object_id}")
        async def delete_object(object_id: int):
            self.handler.delete(object_id)
            return {"detail": "Object deleted"}
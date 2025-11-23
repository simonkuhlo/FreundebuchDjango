from crud.base import CRUDHandler
from fastapi import APIRouter, Query


class CRUDHandlerRouter(APIRouter):
    def __init__(self, handler: CRUDHandler):
        self.handler = handler
        super().__init__(prefix=f"/{handler.name}")

        @self.get("/")
        async def get_list(start_id: int = Query(0, ge=0), limit: int = Query(100, ge=1)):
            read_objects = self.handler.list(start_id=start_id, limit=limit)
            return {"objects": read_objects}

        @self.get("/{object_id}")
        async def get_object(object_id: int):
            read_object = self.handler.get(object_id)
            return {"object": read_object}

        @self.post("/")
        async def create_user(create_object: handler.create_schema):
            read_object = self.handler.create(create_object)
            return {"object": read_object}

        @self.put("/{object_id}")
        async def update_user(update_object: handler.update_schema, object_id: int):
            read_object = self.handler.update(object_id, update_object)
            return {"object": read_object}

        @self.delete("/{object_id}")
        async def delete_user(object_id: int):
            self.handler.delete(object_id)
            return {"detail": "Object deleted"}
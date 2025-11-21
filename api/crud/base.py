from pydantic import BaseModel


class CrudHandler:

    def create(self, new_object:BaseModel):
        raise NotImplementedError()

    def read(self, object_id:int):
        raise NotImplementedError()
    
    def read_list(self):
        raise NotImplementedError()

    def update(self, object_id:int, updated_object:BaseModel):
        raise NotImplementedError()

    def delete(self, object_id:int):
        raise NotImplementedError()
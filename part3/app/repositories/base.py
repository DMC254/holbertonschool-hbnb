from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def list_all(self):
        pass

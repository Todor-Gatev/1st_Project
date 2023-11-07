from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self) -> str:
        robots_info = ' '.join(e.name for e in self.robots) if self.robots else "none"

        return (f"{self.name} Main Service:\n"
                f"Robots: {robots_info}")

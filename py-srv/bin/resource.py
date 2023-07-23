import falcon
import json
from sqlalchemy.orm import Session

from model import PopModel

class Resource():
    def __init__(self, session: Session):
        self.session = session

    def on_get(self, req, resp):
        pops = self.session.query(PopModel).all()
        results = [
            {
                "id": pop.id,
                "name": pop.name,
                "color": pop.color
            } for pop in pops]

        # Create a JSON representation of the resource
        resp.text = json.dumps({"results": results}, ensure_ascii=False)

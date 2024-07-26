from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from core.game import Game


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/')
async def home(request: Request):
    new_game = Game(slots=[])

    new_game.spin_roulette()
    # new_game.draw()
    # result = new_game.verify()

    return templates.TemplateResponse(
        request=request, name="index.html", context={"teste": "teste"}
    )

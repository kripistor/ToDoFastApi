from fastapi import Request, Form, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy import insert, delete, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND

from app import app, templates
from todo.database.models import Task
from todo.database.models.database import get_session


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task).order_by(Task.id.desc()))
    tasks = result.scalars().all()
    return templates.TemplateResponse("index.html", {"request": request, "task_list": tasks})


@app.post("/add_task")
async def add_task(title: str = Form(...), session: AsyncSession = Depends(get_session)):
    await session.execute(insert(Task).values(title=title))
    await session.commit()
    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@app.get('/update_task_complete/{task_id}')
async def update_task_complete(task_id: int, session: AsyncSession = Depends(get_session)):
    await session.execute(
        update(Task).where(Task.id == task_id).values(completed=True)
    )
    await session.commit()
    url = app.url_path_for('home')

    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@app.get('/update_task_uncomplete/{task_id}')
async def update_task_uncomplete(task_id: int, session: AsyncSession = Depends(get_session)):
    await session.execute(
        update(Task).where(Task.id == task_id).values(completed=False)
    )
    await session.commit()
    url = app.url_path_for('home')

    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@app.get("/delete_task/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    await session.execute(delete(Task).where(Task.id == task_id))
    await session.commit()
    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)

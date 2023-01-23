from fastapi import FastAPI, Depends, HTTPException, status
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request : schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}')
def delete(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete()
    db.commit()
    return "done!!"

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request = schemas.Blog, db: Session = Depends(get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first() :
        raise HTTPException("This {id} is not found ", 
                            status_code=status.HTTP_404_NOT_FOUND)
                            
    blog.update(request)
    db.commit()
    return "updated"

@app.get('/blog/{id}')
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException("This {id} is not available", 
                            status_code=status.HTTP_404_NOT_FOUND)
                            
    return blog
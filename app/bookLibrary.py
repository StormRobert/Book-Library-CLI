from typing import Optional
from tabulate import tabulate
from rich.console import Console
import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database import (
    get_all_books,
    add_book,
    update_book,
    delete_book,
    get_all_users,
    add_user,
    delete_user,
    get_all_checkouts,
    checkout_book,
    return_book,
    recommend_books
)
from models import Base

database_url = 'sqlite:///library.db'
engine = create_engine(database_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

app = typer.Typer()

console = Console()

@app.command()
def show_library():
    books = get_all_books(session)
    users = get_all_users(session)
    checkouts = get_all_checkouts(session)

    console.print("\n[bold green]Books:[/bold green]")
    display_table(books)

    console.print("\n[bold blue]Users:[/bold blue]")
    display_table(users)

    console.print("\n[bold magenta]Checkouts:[/bold magenta]")
    display_table(checkouts)

@app.command()
def new_book(title: str, author: str, publication_date: datetime, genre: str, availability: Optional[bool] = True):
    add_book(session, title, author, publication_date, genre, availability)
    console.print(f"[bold green]Book added successfully![/bold green]")

@app.command()
def modify_book(book_id: int, title: str, author: str, publication_date: datetime, genre: str): 
    update_book(session, book_id, title, author, publication_date, genre)
    console.print(f"[bold blue]Book updated successfully![/bold blue]")

@app.command()
def remove_book(book_id: int):
    delete_book(session, book_id)
    console.print(f"[bold red]Book deleted successfully![/bold red]")

@app.command()
def new_user(name: str, email: str, phone_number: int):
    add_user(session, name, email, phone_number)
    console.print(f"[bold blue]User added successfully![/bold blue]")

@app.command()
def remove_user(user_id: int):
    delete_user(session, user_id)
    console.print(f"[bold red]User deleted successfully![/bold red]")

@app.command()
def borrow_book(book_id: int, user_id: int, genre: str):
    checkout_book(session, book_id, user_id, genre)
    console.print(f"[bold green]Book checked out successfully![/bold green]")

@app.command()
def finish_book(checkout_id: int):
    return_book(session, checkout_id)
    console.print(f"[bold blue]Book returned successfully![/bold blue]")

@app.command()
def similar_books(user_id: int):
    sampled = recommend_books(session, user_id)
    console.print(f"[bold magenta]Books recommended successfully![/bold magenta]")
    displayy_table(sampled)

def display_table(data):
    headers = data[0].__dict__.keys() if data else []
    rows = [[getattr(item, header) for header in headers] for item in data]
    table = tabulate(rows, headers=headers, tablefmt="pretty")
    print(table)
   
def displayy_table(data):
    headers = data[0].__dict__.keys() if data else []
    rows = [[getattr(item, header) for header in headers] for item in data]
    table = tabulate(rows, headers=headers, tablefmt="pretty")
    print(table)
if __name__ == "__main__":
    app()

#!/usr/bin/env python3
import requests
import typer 

app = typer.Typer(help="CLI tool to fetch github user info and recent activty \n Eg. ./main.py user-info bagi6969")

GITHUB_api = "https://api.github.com"

@app.command()
def user_info(username: str):
    """
    Get basic info about a GitHub user.
    """
    url = f"{GITHUB_api}/users/{username}"
    response = requests.get(url)
    
    if response.status_code != 200:
        typer.echo(f"❌ Error code: {response.status_code}") 
        raise typer.Exit()
    
    data = response.json()
    typer.echo(f" {data['login']} ({data.get('name', 'No name')})")
    typer.echo(f" Location: {data.get('location', 'Unknown')}")
    typer.echo(f" Public Repos: {data['public_repos']}")
    typer.echo(f" Followers: {data['followers']}")
    typer.echo(f" Joined: {data['created_at']}")
    typer.echo(f" Profile: {data['html_url']}")

@app.command()
def recent_events(username: str, limit: int = 5):
    """Get recent public events from a user."""
    url = f"{GITHUB_api}/users/{username}/events/public"
    res = requests.get(url)
    events = res.json()[:limit]
    for e in events:
        typer.echo(f"{e['type']} on {e['created_at']}")

if __name__ == "__main__":
    app()

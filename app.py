import click
from termcolor import cprint
from jokes.jokesv2 import AllJokes


@click.command()
@click.option(
    "--category",
    default="Any",
    help="Joke category (options: Any, Programming, Misc, Dark, Pun, Spooky, Christmas). Provide as a string separated by commas if many categories e.g. Any,Programming,Misc,Dark",
)
@click.option(
    "--type",
    default="single",
    help="Joke type (options: single, twopart).",
)
@click.option(
    "--amount",
    default=1,
    help="Joke amount (The amount of jokes you want to generate)",
)
def generate_jokes(category: str, type: str, amount: int):
    jokes = AllJokes()

    provided_category = category.split(",") if category != "Any" else [category]

    provided_type = [type]

    new_joke = jokes.get_joke_json(
        joke_category=provided_category,
        joke_type=provided_type,
        joke_amount=amount,
    )

    print("\n")

    if provided_type == ["single"] and amount > 1:
        count = 1

        for joke in new_joke["jokes"]:
            cprint(f"{count}. {joke['joke']}\n", "green")

            count += 1

    elif provided_type == ["single"] and amount == 1:
        cprint(f"{amount}. {new_joke['joke']}", "green")

    elif provided_type == ["twopart"] and amount > 1:
        count = 1

        for joke in new_joke["jokes"]:
            cprint(f"{count}. {joke['setup']}", "green")
            cprint(f"{joke['delivery']}\n", "green")

            count += 1

    elif provided_type == ["twopart"] and amount == 1:
        cprint(f"{amount}. {new_joke['setup']}\n{new_joke['delivery']}", "green")

    print("\n")


if __name__ == "__main__":
    generate_jokes()

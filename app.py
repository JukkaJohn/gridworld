import click

from agent import Agent


@click.command()
@click.option('--rounds', default=100, help='Number of learning rounds.', type=int)
def grid(rounds: int):
    agent = Agent()
    agent.play(rounds=rounds)
    agent.print_q_values()


if __name__ == '__main__':
    grid()

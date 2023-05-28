import click

from repo.repos import Repo
from db_client.operation_es import OperationES
from service.tweet import TweetOperation
from db_client.client_elasticsearch import ClientES


es = ClientES()
operation_es = OperationES(es)
repo = Repo(es=operation_es)
client = TweetOperation(repo)


@click.group()
def cli():
    pass


@click.command()
@click.option('--shards', '-s', default=1, help='number of shards')
@click.option('--replicas', '-r', default=1, help='number of replicas')
@click.option('--index', '-i', help=' name of index')
def create_index(shards: int, replicas: int, index: str):
    client.create_index(number_of_replicas=replicas, number_of_shards=shards, index_name=index)


cli.add_command(create_index)
if __name__ == '__main__':
    cli()

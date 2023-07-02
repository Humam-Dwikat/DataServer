import sys
import click

sys.path.append("/home/humam/SimulateServer/")

from db_client.client_elasticsearch import ClientES
from libs.handler import CIOperationES

es = ClientES()
client = CIOperationES(es)


@click.group()
def cli():
    pass


@click.command()
@click.option('--shards', '-s', default=1, help='number of shards')
@click.option('--replicas', '-r', default=0, help='number of replicas')
@click.option('--index', '-i', help=' name of index')
def create_index(shards: int, replicas: int, index: str):
    client.create_index(number_of_replicas=replicas, number_of_shards=shards, index_name=index)
    click.echo('Index created')


@click.command()
@click.option('--index', '-i', help=' name of index')
def index_document(index: str):
    client.index_document(index_name=index)
    click.echo('document indexed')


cli.add_command(create_index)
cli.add_command(index_document)
if __name__ == '__main__':
    cli()

# Skeleton of a CLI

import click

import wagtail_extras


@click.command('wagtail_extras')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(wagtail_extras.has_legs)

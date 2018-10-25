import click
from sw4iot_orch_sdk import Sw4iotOrchSdk
from prettytable import PrettyTable

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug
    ctx.obj['ORCH_SDK'] = Sw4iotOrchSdk('0.0.0.0', 8000)


@cli.command()
@click.argument('name', type=str)
@click.pass_context
def add_slice(ctx, name):
    resp = ctx.obj['ORCH_SDK'].add_slice(name)
    click.echo(resp['message'])


@cli.command()
@click.argument('name', type=str)
@click.pass_context
def del_slice(ctx, name):
    resp = ctx.obj['ORCH_SDK'].del_slice(name)
    click.echo(resp['message'])


@cli.group()
@click.pass_context
def list(ctx):
    pass


@list.command()
@click.pass_context
def slices(ctx):
    resp = ctx.obj['ORCH_SDK'].get_slices()
    if resp['status'] == 200:
        table = PrettyTable(['slice', 'gateway', 'netmask', 'dns', 'address'])
        slices = resp['data']
        for slice in slices:
            table.add_row([slice['slice'], slice['gateway'], slice['netmask'], slice['dns'], slice['address']])
        click.echo(table)

@list.command()
@click.pass_context
def gateways(ctx):
    resp = ctx.obj['ORCH_SDK'].get_gateways()
    if resp['status'] == 200:
        table = PrettyTable(['gateway', 'address', 'agent port', 'slices', 'enabled'])
        gateways = resp['data']
        for gateway in gateways:
            table.add_row([gateway['name'], gateway['agent']['ip_address'], gateway['agent']['port'], ', '.join(gateway['slices']), gateway['enabled']])
        click.echo(table)


@cli.group()
@click.argument('name', type=str)
@click.pass_context
def slice(ctx, name):
    if name:
        ctx.obj['SLICE_NAME'] = name


@slice.command()
@click.pass_context
def add(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    click.echo('Slice is %s' % (ctx.obj['SLICE_NAME']))


@slice.command()
@click.pass_context
def list(ctx):
    click.echo('List of slices')


@cli.group()
@click.pass_context
def gateway(ctx):
    pass


@gateway.command()
@click.pass_context
def add(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    pass


if __name__ == '__main__':
    cli(obj={})

from keystone.backends.sqlalchemy import migration
from keystone.manage2 import base
from keystone.manage2 import common


@common.arg('--version',
    required=True,
    help='specify the desired database version')
class Command(base.BaseSqlalchemyCommand):
    """Upgrades the database to the specified version."""

    def upgrade_database(self, version):
        """Upgrade database to the specified version"""
        migration.upgrade(self.options, version=version)

    def run(self, args):
        """Process argparse args, and print results to stdout"""
        self.upgrade_database(version=args.version)

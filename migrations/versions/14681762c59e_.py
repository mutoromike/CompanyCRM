"""empty message

Revision ID: 14681762c59e
Revises: 
Create Date: 2019-11-29 12:04:03.782459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14681762c59e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deal_stage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stage_name', sa.String(length=20), nullable=False),
    sa.Column('display_order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lead_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source_name')
    )
    op.create_table('lead_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status_name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('status_name')
    )
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('can_view', sa.Boolean(), nullable=False),
    sa.Column('can_edit', sa.Boolean(), nullable=False),
    sa.Column('can_create', sa.Boolean(), nullable=False),
    sa.Column('can_delete', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_resources',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], )
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('avatar', sa.String(length=25), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_first_login', sa.Boolean(), nullable=False),
    sa.Column('is_user_active', sa.Boolean(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('address_line', sa.String(length=40), nullable=True),
    sa.Column('addr_state', sa.String(length=40), nullable=True),
    sa.Column('addr_city', sa.String(length=40), nullable=True),
    sa.Column('post_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=40), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=40), nullable=True),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('company_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('mobile', sa.String(length=20), nullable=True),
    sa.Column('address_line', sa.String(length=40), nullable=True),
    sa.Column('addr_state', sa.String(length=40), nullable=True),
    sa.Column('addr_city', sa.String(length=40), nullable=True),
    sa.Column('post_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=40), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('lead_source_id', sa.Integer(), nullable=True),
    sa.Column('lead_status_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['lead_source_id'], ['lead_source.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['lead_status_id'], ['lead_status.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('avatar', sa.String(length=25), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('mobile', sa.String(length=20), nullable=True),
    sa.Column('address_line', sa.String(length=40), nullable=True),
    sa.Column('addr_state', sa.String(length=40), nullable=True),
    sa.Column('addr_city', sa.String(length=40), nullable=True),
    sa.Column('post_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=40), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('deal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('expected_close_price', sa.Float(), nullable=False),
    sa.Column('expected_close_date', sa.DateTime(), nullable=True),
    sa.Column('deal_stage_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['deal_stage_id'], ['deal_stage.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deal')
    op.drop_table('contact')
    op.drop_table('lead')
    op.drop_table('account')
    op.drop_table('user')
    op.drop_table('roles_resources')
    op.drop_table('role')
    op.drop_table('resource')
    op.drop_table('lead_status')
    op.drop_table('lead_source')
    op.drop_table('deal_stage')
    # ### end Alembic commands ###
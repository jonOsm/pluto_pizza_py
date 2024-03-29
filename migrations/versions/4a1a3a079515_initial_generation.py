"""initial_generation

Revision ID: 4a1a3a079515
Revises: 
Create Date: 2023-03-28 19:25:30.844442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a1a3a079515'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cheese_amts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('base_price', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cheese_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crust_thicknesses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crust_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_sizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('base_price', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('base_price', sa.Float(), nullable=False),
    sa.Column('is_draft', sa.Boolean(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=50), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sauce_amts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sauce_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topping_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('email_verified', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('disabled', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=50), nullable=True),
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('province', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('extension', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_customizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_default', sa.Boolean(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('crust_type_id', sa.Integer(), nullable=False),
    sa.Column('crust_thickness_id', sa.Integer(), nullable=False),
    sa.Column('cheese_type_id', sa.Integer(), nullable=False),
    sa.Column('cheese_amt_id', sa.Integer(), nullable=False),
    sa.Column('sauce_type_id', sa.Integer(), nullable=False),
    sa.Column('sauce_amt_id', sa.Integer(), nullable=False),
    sa.Column('product_size_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['cheese_amt_id'], ['cheese_amts.id'], ),
    sa.ForeignKeyConstraint(['cheese_type_id'], ['cheese_types.id'], ),
    sa.ForeignKeyConstraint(['crust_thickness_id'], ['crust_thicknesses.id'], ),
    sa.ForeignKeyConstraint(['crust_type_id'], ['crust_types.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_size_id'], ['product_sizes.id'], ),
    sa.ForeignKeyConstraint(['sauce_amt_id'], ['sauce_amts.id'], ),
    sa.ForeignKeyConstraint(['sauce_type_id'], ['sauce_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toppings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('base_price', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['type_id'], ['topping_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_customization_toppings',
    sa.Column('product_customization_id', sa.Integer(), nullable=False),
    sa.Column('topping_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_customization_id'], ['product_customizations.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['topping_id'], ['toppings.id'], ),
    sa.PrimaryKeyConstraint('product_customization_id', 'topping_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_customization_toppings')
    op.drop_table('toppings')
    op.drop_table('product_customizations')
    op.drop_table('addresses')
    op.drop_table('users')
    op.drop_table('topping_types')
    op.drop_table('sauce_types')
    op.drop_table('sauce_amts')
    op.drop_table('products')
    op.drop_table('product_sizes')
    op.drop_table('crust_types')
    op.drop_table('crust_thicknesses')
    op.drop_table('cheese_types')
    op.drop_table('cheese_amts')
    # ### end Alembic commands ###

"""empty message

Revision ID: 8010b428dc3f
Revises: 
Create Date: 2024-02-23 01:40:41.439582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8010b428dc3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unidad_residencial',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre_unidad', sa.String(length=200), nullable=False),
    sa.Column('nit', sa.String(length=100), nullable=False),
    sa.Column('direccion', sa.String(length=100), nullable=False),
    sa.Column('telefono', sa.String(length=30), nullable=False),
    sa.Column('cant_apto', sa.Integer(), nullable=False),
    sa.Column('cant_torres', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('apartamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('torre', sa.String(length=10), nullable=False),
    sa.Column('num_apto', sa.String(length=10), nullable=False),
    sa.Column('num_habitantes', sa.Integer(), nullable=False),
    sa.Column('unidad_residencial_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['unidad_residencial_id'], ['unidad_residencial.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publicaciones',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('contenido', sa.String(length=500), nullable=False),
    sa.Column('creacion', sa.DateTime(), nullable=False),
    sa.Column('unidad_residencial_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['unidad_residencial_id'], ['unidad_residencial.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mascotas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('raza', sa.String(length=50), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apartamento_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['apartamento_id'], ['apartamento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('residente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombres', sa.String(length=100), nullable=False),
    sa.Column('apellidos', sa.String(length=100), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.Column('celular', sa.String(length=50), nullable=False),
    sa.Column('cedula', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('unidad_residencial_id', sa.Integer(), nullable=True),
    sa.Column('apartamento_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['apartamento_id'], ['apartamento.id'], ),
    sa.ForeignKeyConstraint(['unidad_residencial_id'], ['unidad_residencial.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('placa', sa.String(length=10), nullable=False),
    sa.Column('marca', sa.String(length=50), nullable=False),
    sa.Column('modelo', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=15), nullable=False),
    sa.Column('apartamento_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['apartamento_id'], ['apartamento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inicio', sa.DateTime(), nullable=False),
    sa.Column('final', sa.DateTime(), nullable=False),
    sa.Column('residente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['residente_id'], ['residente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservas')
    op.drop_table('vehiculos')
    op.drop_table('residente')
    op.drop_table('mascotas')
    op.drop_table('publicaciones')
    op.drop_table('apartamento')
    op.drop_table('user')
    op.drop_table('unidad_residencial')
    # ### end Alembic commands ###

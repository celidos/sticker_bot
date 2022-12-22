from sqlalchemy import Table, Column, Integer, Text, DDLElement
from sqlalchemy.schema import DDLElement


class CreateFtsTable(DDLElement):
    """Represents a CREATE VIRTUAL TABLE ... USING fts5 statement, for indexing
    a given table.

    """

    def __init__(self, table, version=5):
        self.table = table
        self.version = version


@compiles(CreateFtsTable)
def compile_create_fts_table(element, compiler, **kw):
    """
    """
    tbl = element.table
    version = element.version
    preparer = compiler.preparer
    sql_compiler = compiler.sql_compiler

    tbl_name = preparer.format_table(tbl)
    vtbl_name = preparer.quote(tbl.name + "_idx")

    text = "\nCREATE VIRTUAL TABLE "
    text += vtbl_name + " "
    text += "USING fts" + str(version) + "("

    separator = "\n"

    pk_column, = tbl.primary_key
    columns = [col for col in tbl.columns if col is not pk_column]

    for column in columns:
        text += separator
        separator = ", \n"
        text += "\t" + preparer.format_column(column)

        if not isinstance(column.type, String):
            text += " UNINDEXED"

    text += separator
    text += "\tcontent=" + sql_compiler.render_literal_value(
            tbl.name, String())

    text += separator
    text += "\tcontent_rowid=" + sql_compiler.render_literal_value(
            pk_column.name, String())

    text += "\n)\n\n"
    return text
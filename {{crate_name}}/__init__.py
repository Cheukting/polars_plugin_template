from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl
from polars.plugins import register_plugin_function

from {{crate_name}}._internal import __version__ as __version__

if TYPE_CHECKING:
    from {{crate_name}}._typing import IntoExpr, IntoExprColumn

PLUGIN_PATH = Path(__file__).parent

# Register your expressions below, one function per `#[polars_expr]` in
# `src/expressions.rs`. For example:
#
# def capitalize(expr: IntoExpr) -> pl.Expr:
#     """Capitalize String."""
#     return register_plugin_function(
#         plugin_path=PLUGIN_PATH,
#         function_name="capitalize",
#         args=expr,
#         is_elementwise=True,
#     )

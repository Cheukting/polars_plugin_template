"""Type aliases for the public API of this plugin.

Polars keeps these aliases in the private ``polars._typing`` module, so we
define our own here rather than importing from it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeAlias, Union

if TYPE_CHECKING:
    from datetime import date, datetime, time, timedelta
    from decimal import Decimal

    import polars as pl

    IntoExprColumn: TypeAlias = Union[pl.Expr, pl.Series, str]
    PythonLiteral: TypeAlias = Union[
        int, float, str, bool, bytes, date, time, datetime, timedelta, Decimal, list[Any]
    ]
    IntoExpr: TypeAlias = Union[PythonLiteral, IntoExprColumn, None]

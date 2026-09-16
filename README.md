# {{project-name}}

A Polars expression plugin, generated from the
[polars-plugin-101](https://github.com/Cheukting/polars-plugin-101) workshop
template with [cargo-generate](https://cargo-generate.github.io/cargo-generate/).

Everything here is the boilerplate that the workshop's *Step 1* and the
scaffolding parts of *Steps 2 and 3* would have you type out by hand. The
expression logic is up to you.

## What you have

- `Cargo.toml` — Rust dependencies: polars, pyo3, pyo3-polars, serde
- `pyproject.toml` — maturin build settings, with `module-name` wired to `{{crate_name}}._internal`
- `src/lib.rs` — the `_internal` PyO3 module and the Polars global allocator
- `src/expressions.rs` — empty; your `#[polars_expr]` functions go here
- `{{crate_name}}/__init__.py` — where you register each expression with Polars
- `{{crate_name}}/typing.py` — `IntoExpr` / `IntoExprColumn` aliases, so we never import the private `polars._typing`
- `{{crate_name}}/_internal.pyi` — type stub for the compiled module

## Getting started

Set up a virtual environment and install the build tools:

```
uv venv .venv
source .venv/bin/activate
python -m ensurepip --default-pip
uv pip install polars maturin
```

The `ensurepip` line is needed because `maturin develop` cannot find pip otherwise.

Then build:

```
maturin develop
```

That compiles the Rust, drops `_internal.abi3.so` into `{{crate_name}}/`, and
installs the package into the virtual environment.

## Writing your first expression

Add a function to `src/expressions.rs` — the file starts out empty, so bring
the imports with you:

```rust
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

#[polars_expr(output_type=Float64)]
fn to_farenheit(inputs: &[Series]) -> PolarsResult<Series> {
    let ca = inputs[0].f64()?;
    let out: Float64Chunked = ca.apply_values(|deg_c| deg_c * 9.0 / 5.0 + 32.0);
    Ok(out.into_series())
}
```

Register it in `{{crate_name}}/__init__.py`:

```python
def to_farenheit(expr: IntoExpr) -> pl.Expr:
    """Converting Celcius to Farenheit."""
    return register_plugin_function(
        plugin_path=PLUGIN_PATH,
        function_name="to_farenheit",
        args=expr,
        is_elementwise=True,
    )
```

Run `maturin develop` again, and use it:

```python
import polars as pl
from {{crate_name}} import to_farenheit

df = pl.DataFrame({"deg_c": [0.0, 21.5, 100.0]})
print(df.with_columns(deg_f=to_farenheit("deg_c")))
```

Note that `#[polars_expr]` functions are *not* added to the module in
`lib.rs`. The macro exports each one as a C function in the compiled library,
and Polars looks it up by name when `register_plugin_function` runs — which is
why `function_name` has to match the Rust function name exactly.

## Next steps

Work through the [workshop README](https://github.com/Cheukting/polars-plugin-101#readme)
for multi-column inputs, dtype dispatch, column-wise accumulation and kwargs.

If you want CI for wheel builds, `maturin generate-ci github` will write a
workflow for you.

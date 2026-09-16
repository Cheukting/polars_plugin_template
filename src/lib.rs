mod expressions;

use pyo3_polars::PolarsAllocator;

/// Polars plugin expressions implemented in Rust.
#[pyo3::pymodule]
mod _internal {
    use pyo3::prelude::*;

    #[pymodule_init]
    fn init(m: &Bound<'_, PyModule>) -> PyResult<()> {
        m.add("__version__", env!("CARGO_PKG_VERSION"))
    }
}

#[global_allocator]
static ALLOC: PolarsAllocator = PolarsAllocator::new();

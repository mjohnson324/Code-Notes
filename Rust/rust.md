Rustacean: a Rust Programmer

Useful Terminal Commands:
rustup update (to update rust toolchain installer)
rustc --version (see current version)
rustup doc (offline documentation)
rustc file_name (to compile code)

cargo new _name_ (start project with git repo and main.rs, --bin to specify binary)
cargo run (build and execute cargo project)
cargo build (to just build the)
cargo check (to see if a project checks out)
cargo update (to newer compatible versions)

Syntax:
main- 1st function in any Rust program
!- macro designation (metaprogramming, println!, etc.)
::<_type_>- turbofish, for explicit typing

Crates- rust code packages, like Ruby gems
Cargo- build system and package manager for rust
	-Default build folder is  for debugging, release is for production
	-Package section requires name, version, & authors
	-Cargo lock tracks dependencies and ensures consistent dependencies
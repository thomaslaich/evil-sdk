# Set NSMITHY_LOCAL=../smithy-dotnet to use a local checkout's staged codegen
# JAR and packed packages (run `just codegen pack` there first).

local := env("NSMITHY_LOCAL", "")
build_props := if local == "" { "" } else { "-p:NSmithyVersion=0.0.0-SNAPSHOT -p:NSmithyLocalFeed=" + join(absolute_path(local), "artifacts/packages") }

default:
    @just --list

# List every AWS service model with its protocols
list:
    python3 scripts/nsaws.py list

# Regenerate checked-in services (services.txt, or the given ids)
generate *ids:
    python3 scripts/nsaws.py generate {{ ids }}

# Build the checked-in services
build:
    dotnet build EvilSdk.slnx {{ build_props }}

# Generate and compile every service (or the given ids) into .sweep/ and write reports/
sweep *ids:
    python3 scripts/nsaws.py sweep {{ ids }}

# Pull the latest AWS models
update-models:
    git submodule update --remote --depth 1 aws-models

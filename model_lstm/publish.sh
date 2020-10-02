export $(cat ../.env | xargs)

set -e

warn() {
    echo "$@" 1>&2
}

die() {
    warn "$@"
    exit 1
}

# Remove previous builds
rm -f dist/*

# Gemfury only lets you publish one of sdist and wheel for free
# python setup.py sdist bdist_wheel || die "Building package failed."
python setup.py bdist_wheel || die "Building package failed."

for file in $(ls dist)
do
    echo "Uploading ${file} to index..."
    curl -F package=@dist/${file} https://${FURY_TOKEN}@push.fury.io/${FURY_USERNAME}/ || die "Uploading package failed."
done
echo "Package successfully published."
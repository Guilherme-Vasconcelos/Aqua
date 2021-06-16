#!/bin/sh

files=$(find ./hooks -mindepth 1)
for file in $files
do
    cp "$file" ./.git/hooks/
    file_basename=$(basename "$file")
    chmod +x "./.git/hooks/$file_basename"
done

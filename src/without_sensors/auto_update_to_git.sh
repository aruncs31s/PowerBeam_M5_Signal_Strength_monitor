#!/bin/env bash
while true; do
	git add -A && git commit -m "auto update" && git push origin main
	seep 320
done

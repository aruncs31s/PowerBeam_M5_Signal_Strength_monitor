#!/bin/bash
while true; do
	git add -A && git commit -m "auto update" && git push origin main
	/bin/seep 320
done

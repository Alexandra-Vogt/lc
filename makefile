failure:
	@echo "error, run make install or make uninstall"
install:
	mkdir -p $(HOME)/.lc-src
	cp -r src/* $(HOME)/.lc-src
	cp -r lc.sh $(HOME)/scripts/lc

uninstall:
	rm -rf $(HOME)/.lc-src
	rm $(HOME)//lc
test:
	python3 ./src/test_lunar_functions.py

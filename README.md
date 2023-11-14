# ownCompress
John Crickett's coding challenges ownCompressionTool

## How to install
```
git clone https://github.com/Perchinka/ownCompress.git
```
---

## How to use
You need to use -c or -d flags. (compress and decompress)

```bash
python3 main.py -h

usage: main.py [options] file

Compress or decompress a text file

positional arguments:
  file                  File to compress or decompress

options:
  -h, --help            show this help message and exit
  -c, --compress        Compress a text file
  -d, --decompress      Decompress a text file
  -o OUTPUT, --output OUTPUT
                        Output file name
```

Example:
```bash
python3 main.py test.txt -c
```
```sh
python3 main.py test.compressed -d
```
---

## Contributing
It does not have a wide functionality, but if you want to modify it, then fork :D

- Fork the repository.
- Create a new branch for your feature/fix: `git checkout -b feature-name`
- Make your changes.
- Commit your changes: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature-name`
- Submit a pull request.

GUID Tool
=========
A small console application to generate and convert between various forms of GUIDs. Note: base64 representations are in little endian form.

How to Install
--------------
You can install this script using pip:

```bash
$ sudo pip install guid-tool
```

If you do not have pip, try easy_install:

```bash
$ sudo easy_install guid-tool
```

Generating a GUID
-----------------
You can generate a new GUID in various forms by calling the script:

```bash
$ guid-tool
hex: 8895cf4e-5685-4c82-8391-addfd518ecc3
int: 181552864324031739326019292661926128835
b64: Ts+ViIVWgkyDka3f1Rjsww==
```

Converting GUID Forms
---------------------
You can convert between GUID forms by passing in a GUID in any of the three supported forms: hex, int, and base64:

```bash
$ guid-tool FfdySTMLp0SC89TitNdqhQ==
hex: 4972f715-0b33-44a7-82f3-d4e2b4d76a85
int: 97630576956601658369574553421172140677
b64: FfdySTMLp0SC89TitNdqhQ==

$ guid-tool 63d7070b-5a7a-46e4-9f8e-72ac8391f19f
hex: 63d7070b-5a7a-46e4-9f8e-72ac8391f19f
int: 132710058283670147193134380447756841375
b64: CwfXY3pa5EafjnKsg5Hxnw==
```

License
-------
Copyright (C) 2012 Daniel G. Taylor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

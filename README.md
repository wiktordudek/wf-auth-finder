<div align="center">
    <h1>WF Authentication Finder</h1>
    <p><strong>🔎 Find Warframe account ID and nonce with ease. </strong></p>
</div>

> [!WARNING]  
> Reverse engineering is strictly prohibited by the Warframe's ToS (Terms of Service). Please keep in mind that I am not responsible for any damage caused by use of this project.

## ❓ What Is That?

This project automates the extraction of Warframe account parameters (`accountId` and `nonce`) required to authenticate with its API endpoints. The script identifies the game process, then searches for the above-named parameters within the game's memory space, making the extraction as simple as possible.

## 🚀 Quick Start

<table>
<tr>
<td width="50%">
✨ with <code>uv</code> <i>(recommended)</I>

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python3 app.py
```

</td>
<td width="50%">
🐢 or with regular Python's <code>pip</code>

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

</td>
</tr>
</table>

## 🙋🏻‍♂️ Contribution

Contributions are welcome! If you've found a bug or have a suggestion for improvement, please open an issue or pull request.

## 📖 License

This project is licensed under the GNU General Public License v3.0 (GPLv3).\
You are free to use, modify, and distribute the code under the terms of this license.

See the [LICENSE](LICENSE) file for details.

## Credits

- me
- [PyMemoryEditor](https://github.com/JeanExtreme002/PyMemoryEditor)

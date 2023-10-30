# PayloadSlicer

`PayloadSlicer` is a Python-based utility crafted to facilitate the segmentation of long PowerShell payloads, making them suitable for inclusion within VBA macros in Microsoft Word. This ensures that your PowerShell code integrates smoothly within the VBA environment, broken down into user-defined chunk sizes.

## Features

- Compatible with both Python 2.7 and 3.x.
- Default chunk size set to 50, but customizable based on user preference.
- Intuitive command-line interface for ease of input and visibility.

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/LexiLominite/PayloadSlicer.git
   ```

2. Navigate to the cloned directory:

   ```
   cd PayloadSlicer
   ```

3. Execute the Python script:

   For Python 3:

   ```
   python3 payloadslicer.py
   ```

   For Python 2.7:

   ```
   python payloadslicer27.py
   ```

4. Follow the on-screen instructions. Input your payload and specify the desired chunk size when prompted.

## Example Output

```
┌──(root㉿kali)-[~]
└─# python3 payloadslicer.py
Input your payload here: powershell -e [edited_base64_content]
Enter the padding number [50 is default]: 
Str = Str "powershell -e JABzAD0AJwAxADkAMg..."
Str = Str "..."
...
```

*Note*: The base64 content has been edited in the example for brevity and security reasons.

## Contribution

Contributions are warmly welcomed! Fork the repository, make your changes, and then submit a pull request. If you come across any issues or have suggestions, feel free to open an issue.

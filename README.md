# Custom File Mover

A simple Python GUI tool that allows you to move a user-defined percentage of randomly selected files from a source directory into a new subfolder.

## Features

- Select any folder containing files
- Specify the percentage of files to move
- Create and name a new subfolder automatically
- Avoid filename conflicts with automatic renaming
- Easy-to-use graphical interface built with Tkinter

## How It Works

1. Choose a source folder using the file dialog.
2. Enter a name for the subfolder where files will be moved.
3. Enter a percentage (1–100) of files to move.
4. Click the "Move Files" button.

The tool will:
- Randomly select the specified percentage of files
- Create the subfolder if it doesn't exist
- Move selected files into the subfolder
- Rename files to avoid overwriting duplicates

## Requirements

- Python 3.x
- Tkinter (standard with most Python distributions)

## Run the Program

```bash
python outil_simplification.py

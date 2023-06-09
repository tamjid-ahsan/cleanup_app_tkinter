import tkinter as tk
from tkinter import filedialog
import os


def window1():
    # Create the main window
    window = tk.Tk()

    # Add the logo to the top bar & set attributes
    window.iconbitmap("./assets/logo.ico")
    window_width = 400  # Adjust this value as needed
    window.geometry(f"{window_width}x100")

    # Set a custom window title
    window.wm_title("Folder CleanUP")
    folder_label = tk.Label(window, text="Selected Folder:")
    folder_label.pack()

    folder_entry = tk.Entry(window, justify="right")
    folder_entry.pack()

    def select_folder():
        global selected_folder
        selected_folder = filedialog.askdirectory()
        if selected_folder:
            folder_entry.delete(0, tk.END)
            folder_entry.insert(tk.END, selected_folder)

    # Create a button to open the folder selection dialog
    select_button = tk.Button(window, text="Select Folder", command=select_folder)
    select_button.pack()

    def button_pressed(event):
        print(event, "remove_empty_directories Button pressed!")

        def remove_empty_directories(target_folder: str):
            # remove empty directories
            folders_path_list = [
                os.path.join(path, name)
                for path, subdirs, files in os.walk(target_folder)
                for name in subdirs
            ][::-1]
            folders_removed_ct = 0
            folders_removed = []
            verbose = False

            for folder_path in folders_path_list:
                try:
                    os.rmdir(folder_path)
                    if verbose:
                        print(f">>> Deleted folder: {folder_path}")
                    folders_removed_ct += 1
                    folders_removed.append(folder_path)
                except FileNotFoundError as e:
                    if verbose:
                        print(e)
                except PermissionError:
                    if verbose:
                        print("Do not have permission to delete file")
                except OSError as e:
                    if verbose:
                        print(e)
                        print("Must not remove folder")

            if verbose:
                print(f"{'*'*60}")

            if folders_removed_ct > 0:
                x = str([x.rsplit("\\")[-1] for x in folders_removed])[1:-1]
                return (
                    f"""Removed {folders_removed_ct} folders."""  # \nRemoved:\t{x}"""
                )
            else:
                return "No folder to remove"

        try:
            o = remove_empty_directories(selected_folder)
        except NameError as e:
            o = "Select directory first"
        except Exception as e:
            print(e)

        tk.messagebox.showinfo("remove_empty_directories".replace("_", " ").title(), o)
        return "break"

    remove_empty_directories = tk.Button(
        window, text="remove empty directories".title()
    )
    remove_empty_directories.bind("<ButtonPress>", button_pressed)
    remove_empty_directories.pack(side="left", padx=5)

    file_extension_cleaner = tk.Button(
        window, text="file_extension_cleaner".replace("_", " ").title()
    )
    file_extension_cleaner.pack(side="left", padx=5)

    def show_popup():
        tk.messagebox.showinfo(
            "Copyright",
            f"""Copyright 2020-2023. Tamjid Ahsan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""",
        )

    info_button = tk.Button(window, text="info", command=show_popup)
    info_button.pack(side="right", padx=5)

    window.mainloop()


if __name__ == "__main__":
    window1()
    # if selected_folder:
    #     target_folder = selected_folder
    #     print("Selected Folder:", selected_folder)


# TO-DO
# - formatting
# - refactor
# - make 'file_extension_cleaner' working
# - comment properly
# - log management
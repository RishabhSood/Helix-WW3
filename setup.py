import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["trump.png", "WW3music.mp3", "warback.jpg"]}},
    executables = executables

    )
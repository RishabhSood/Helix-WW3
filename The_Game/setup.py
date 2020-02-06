import cx_Freeze

executables = [cx_Freeze.Executable("game.pyw")]

cx_Freeze.setup(
    name="World War III",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["trump.png","thefont.ttf", "cs_regular.ttf", "WW3music.mp3", "warback.jpg", "uswins.mp3", "chinatheme.mp3", "function_lib.py", "score.txt", "ww3_log.txt", "usr_details.txt"]}},
    executables = executables

    )

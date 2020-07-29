import click
from os import system
from subprocess import Popen
from alive_progress import alive_bar


@click.command()
@click.option(
    "-u",
    "--upload",
    help="Upload your notes & script additions to GitHub",
    is_flag=True,
)
@click.option(
    "-a",
    "--add",
    type=str,
    help="Add a new libary to the scripts. Will automatically sudo-apt install install it.",
    default=None,
)
@click.option(
    "-d", "--download", help="Download your config repo", type=str, default=None
)
def main(**kwargs):
    print(kwargs)
    opening()
    if kwargs["upload"]:
        upload()
    elif kwargs["add"] is not None:
        add()
    elif kwargs["download"] is not None:
        download(kwargs["download"])
    print(kwargs)


def upload():
    # goodbye!
    system(
        "cd ~/Documents/thm && git add . && git commit -m 'end of session' && git push"
    )


def add():
    None


def download(url):
    # Git clones ya files babe xxx
    # cds to home
    # TODO make this download
    # system("cd ~/Documents")
    system("cd ~/Documents/")
    # git clones ya fancy repo
    system(f"git clone https://github.com/{url}")
    system("cat thm/.BASHRC >> ~/.BASHRC")

    # installs ur scripts via shell
    # TODO multi thread this
    # gets list
    f = open("thm/scripts.sh", "r").readlines()

    # multi threaded installs
    with alive_bar(len(f)) as bar:
        for cmd in f:
            Popen(cmd, shell=True)
            bar()


# system("/thm/scripts.sh")


def opening():
    print(
        """
           .         __  __   ___    
         .'|        |  |/  `.'   `.  
     .| <  |        |   .-.  .-.   ' 
   .' |_ | |        |  |  |  |  |  | 
 .'     || | .'''-. |  |  |  |  |  | 
'--.  .-'| |/.'''. \|  |  |  |  |  | 
   |  |  |  /    | ||  |  |  |  |  | 
   |  |  | |     | ||__|  |__|  |__| 
   |  '.'| |     | |                 
   |   / | '.    | '.                
   `'-'  '---'   '---'   
            """
    )
    print("https://github.com/brandonskerritt\n")


if __name__ == "__main__":
    main()

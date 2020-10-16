from BRImage.commandline import cli

def main():
    args = cli.parse_args()
    if args.subcommand is None:
        print("No arguments supplied.")
    else:
        args.runner(args)

if __name__ == "__main__":
    main()

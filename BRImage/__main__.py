from BRImage.commandline import cli

if __name__ == "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        print("No arguments supplied.")
    else:
        args.runner(args)

import  argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="my match script"
    )
    parser.add_argument('num1', help="number 1")
    parser.add_argument('num2', help="number 2")
    parser.add_argument('operation', help = "provide operator")
    args =parser.parse_args()
    print(args)
    result = None
    if args.operation == '+':
        result = args.num1 + args.num2
    print(result)



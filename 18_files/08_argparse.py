import argparse

parser = argparse.ArgumentParser(description="A simple calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument(
    "operation",
    type=str,
    choices=["add", "sub", "mul", "div"],
    help="Operation to perform",
)

args = parser.parse_args()

print(args)

if args.operation == "add":
    result = args.num1 + args.num2
    print(f"The sum of {args.num1} and {args.num2} is {result}")
elif args.operation == "sub":
    result = args.num1 - args.num2
    print(f"The difference of {args.num1} and {args.num2} is {result}")
elif args.operation == "mul":
    result = args.num1 * args.num2
    print(f"The product of {args.num1} and {args.num2} is {result}")
elif args.operation == "div":
    result = args.num1 / args.num2
    print(f"The quotient of {args.num1} and {args.num2} is {result}")
else:
    print("Invalid operation")

import argparse
from converter import translate_to_french


def cli():
    parser = argparse.ArgumentParser(description="Convert numbers to French words")
    parser.add_argument("number", type=int, help="Number to convert")
    parser.add_argument(
        "--lang",
        type=str,
        default="fr",
        choices=["fr", "bg"],
        help="Language Variant: fr - French (default), bg - Belgian",
    )
    args = parser.parse_args()

    print(translate_to_french(args.number, args.lang))


if __name__ == "__main__":
    cli()
